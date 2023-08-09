$(document).ready(function () {
    //* QUESTION SETUP
    const executeRelalg = relalg_bundle.executeRelalg;
    const Relation = relalg_bundle.Relation;

    // database setup
    const dbSchema = document.getElementById("database");
    const dbValue = dbSchema.getAttribute("value");
    const dbArray = dbValue.split(";");
    const dataset = [dbArray.length];
    for (var i = 0; i < dbArray.length; i++) {
        dataset[i] = executeRelalg(dbArray.at(i), {});
    }
    // Creating dropbtn (Schema) tables
    for (var i = 0; i < dataset.length; i++) {
        dbSchema.innerHTML += createSchemaTables(dataset.at(i)._schema)
    }

    //* USER INTERACTIONS

    // Creates codemirror code block
    var editorInit = $("#RelaXEditor");
    var editor = CodeMirror.fromTextArea(editorInit[0], {
        mode: 'text/RelaX',
        viewportMargin: Infinity,
        indentWithTabs: true,
        smartIndent: true,
        lineNumbers: true,
        matchBrackets: true,
        autofocus: true,
        extraKeys: {
            "Ctrl-Enter": executeEditorContents,
        }
    });

    //* needed elements for rendering.
    var treeElm = $("#tree");
    var outputElm = $("#output");
    var errorElm = $("#error");
    var execBtn = $("#execute");
    execBtn.on("click", executeEditorContents);

    // setup editor with previous submission
    



    //* FUNCTION DEFINITIONS

    // Function that renders HTML tags in string nodes found in body
    function applyHTMLTagsToWords(tagName) {

        // Create a regular expression to match the opening and closing tags
        // (.*?) matches everything between the tags
        // g enables global search
        var regex = new RegExp('<' + tagName + '>(.*?)</' + tagName + '>', 'g');

        // Find all text nodes in the body (not including empty text nodes)
        var textNodes = $('body').find('*').addBack().contents().filter(function () {
            return this.nodeType === 3 && this.nodeValue.trim() !== '';
        });

        // Iterate over the text nodes and apply tags to the matched strings
        textNodes.each(function () {

            var node = this;
            var replacedText = node.nodeValue.replace(regex, function (match, capturedText) {
                return '<' + tagName + '>' + capturedText + '</' + tagName + '>';
            });
            $(node).replaceWith(replacedText);
        });

        return $('body').html();
    }
    
    
    // Function that applies onClick functionality for specified targets
    function applyOnClick() {
        var regex = new RegExp('<click>(.*?)</click>', 'g');

        // Find all text nodes in the body (not including empty text nodes)
        var textNodes = $('body').find('*').addBack().contents().filter(function () {
            return this.nodeType === 3 && this.nodeValue.trim() !== '';
        });

        // Iterate over the text nodes and apply tags to the matched strings
        textNodes.each(function () {

            var node = this;
            var replacedText = node.nodeValue.replace(regex, function (match, capturedText) {
                return `<span  style="cursor: pointer;" onclick="updateCodeMirror('${capturedText}')">${capturedText}</span>`;
            });
            $(node).replaceWith(replacedText);
        });

        return $('body').html();
    }


    // Apply Functionality
    var onClickFormatting = applyOnClick()
    // Apply HTML tags to certain parts of strings
    var boldedWords = applyHTMLTagsToWords('b');
    var italicWords = applyHTMLTagsToWords('i');
    var emphWords = applyHTMLTagsToWords('em');
    var strongWords = applyHTMLTagsToWords('strong');

    // element for previous submission div
    var previousSubmissionElm = $("#previousSubmission");

    // insert previous submission into editor
    function updateCodeMirrorPreviousSubmission() {
        var doc = editor.getDoc(); //gets the information of the editor
        doc.setValue(previousSubmissionElm.text().trim());
        previousSubmissionElm.remove();
    }
    // calls update code mirror with previous submission
    updateCodeMirrorPreviousSubmission();

    //* FUNCTIONS - USER ACTIONS
    // adds functionality for onclick
    function updateCodeMirror(data) {
        var doc = editor.getDoc(); // gets the information of the editor
        doc.replaceRange(data, doc.getCursor()); // adds data at position of cursor
        editor.focus();             // focuses the user on the editor
        editor.setCursor(doc.getCursor()); // sets the cursor directly after the newly added char
    }
    // helper function to allow for HTML calling.
    window.updateCodeMirror = function (data) {
        updateCodeMirror(data);
    }

    // Execute the RelaX Query
    var activeNode = null;

    function executeEditorContents() {
        // loading datasets into relax
        var dataStuff = {};
        for (var i = 0; i < dataset.length; i++) {
            var key = dataset.at(i)._schema._relAliases.at(0);
            dataStuff[key] = dataset[i];
        }


        try {
            activeNode = null;

            const PR = executeRelalg(editor.getValue(), dataStuff); // gets query results
            treeElm.contents().remove(); // clears Tree previous results
            createOutputTable(PR); // creates and renders new output table
            var treeDiv = $('<div class="tree"></div>');
            var ulDiv = $("<ul></ul>");
            ulDiv.append(createRecList(PR)); // creates and renders new tree
            treeDiv.append(ulDiv);
            treeElm.append(treeDiv);
        } catch (err) {
            console.error(err)
            if (err.name === 'SyntaxError')
                createErrorOutput(err.message); // creates and renders error in event user has incorrect RA query 
            else
                createErrorOutput(err);
        }
    }
    0

    //* FUNCTIONS - RENDERING
    function createSchemaTables(dataSchema) {
        // Checks if table exists, exits if not
        if (dataSchema.length === 0) {
            return;
        }
        // Creates the button HTML element for the table; onclick it adds the tablename to Editor, onhover it shows the schema of the table.
        let schemaView = "<div class='schemaTable'><button type='button' onmouseover='' onClick='updateCodeMirror(\"" + dataSchema._relAliases[0] + "\");' class='dropbtn' id='btn-" + dataSchema._relAliases[0] + "'>" + dataSchema._relAliases[0]
            + "</button> <div class='dropdown-content' id='schema-" + dataSchema._relAliases[0] + "'>"

        // get column widths for styling purposes
        let maxColNameLength = 0;
        let maxColTypeLength = 0;

        for (var i = 0; i < dataSchema._names.length; i++) {
            let colName = `${dataSchema._names[i]}`;
            let colType = `${dataSchema._types[i]}`;

            if (colName.length > maxColNameLength) {
                maxColNameLength = colName.length + 2;
            }

            if (colType.length > maxColTypeLength) {
                maxColTypeLength = colType.length + 2;
            }
        }

        // adds headers to the schema tables
        let field = `<div style="text-align: center; border: 1px solid white; padding: 0.2em; display: flex; justify-content: space-around;" class='submenu' id='schema-${dataSchema._relAliases[0]}'>`;
        let name = `<span style='font-weight: bold; width: ${maxColNameLength}ch;'>Columns</span>`;
        let type = `<span style='font-weight: bold; width: ${maxColTypeLength}ch;'>Types</span>`;

        schemaView += field + name + type + '</div>';

        // Creates the submenue element for the table, onclick each member of the table will add itself to the editor
        for (var i = 0; i < dataSchema._names.length; i++) {
            let field = `<div style="text-align: center; border: 1px solid white; padding: 0.2em; display: flex; justify-content: space-around;" class='submenu' id='schema-${dataSchema._relAliases[0]}'>`;
            let name = `<span onClick='updateCodeMirror("${dataSchema._names[i]}")' style='cursor: pointer; width: ${maxColNameLength}ch;'>${dataSchema._names[i]}</span>`;
            let type = `<span style=' width: 8ch;'>${dataSchema._types[i].toUpperCase()}</span>`;

            schemaView += field + name + type + '</div>';
        }

        schemaView += "</div>"
        return schemaView

    }

    // Clears output fields and renders error
    function createErrorOutput(err) {
        errorElm.contents().remove();
        outputElm.contents().remove();
        treeElm.contents().remove();
        errorElm.append(err);

    }

    // clears error and table fields and renders new table
    function createOutputTable(output) {
        outputElm.contents().remove();
        errorElm.contents().remove();

        var table = $("<table></table>"); // creates new table element to be filled
        table.append(createTableHeader(output.getResult()._schema, output.getResult()._rows)); // creates table headers
        table.append(createTableRows(output.getResult()._rows)); // fills table rows
        outputElm.append(table);
    }
    var ifDateChecker = [];
    // Function that creates the table header
    function createTableHeader(columnSchema, rows) {
        ifDateChecker = [];
        var header = $("<thead></thead>");
        var headerRow = $("<tr></tr>");
        // reads each header
        for (var i = 0; i < columnSchema._names.length; i++) {

            (function (column) {

                var th = $("<th></th>").text(columnSchema._names[i]);

                th.on("click", function () {
                    sortTable(this, column);
                });

                if (columnSchema._types[i] == 'date')
                    ifDateChecker.push(i);

                headerRow.append(th);
            })(i);
        }
        header.append(headerRow);
        return header;
    }

    function createTableRows(rows) {
        var tbody = $("<tbody></tbody>");
        var rowElements = [];
        // reads each row in rows and adds them to the row element array.
        rows.forEach(function (row) {
            var tr = $("<tr></tr>");
            for (var i = 0; i < row.length; i++) {
                if (ifDateChecker.includes(i)) {
                    const date = new Date(row[i]);
                    const year = date.getFullYear();
                    const month = String(date.getMonth() + 1).padStart(2, '0');
                    const day = String(date.getDate()).padStart(2, '0');

                    var td = $("<td></td>").text(`${year}-${month}-${day}`);
                } else {
                    var td = $("<td></td>").text(row[i]);
                }

                tr.append(td);
            }
            rowElements.push(tr);
        });
        tbody.append(rowElements);
        return tbody;
    }

    // function that sorts output tables when column names are clicked on
    function sortTable(element, column) {

        const $table = $(element).closest("table");
        const $tbody = $table.find("tbody");
        const rows = $tbody.find("tr").toArray();
        const currentDirection = $table.data("sort-direction");
        let direction;
        let arrow;

        if (currentDirection === "asc" && $table.data("sort-column") === column) {
            // First click on the same column, reverse the sort direction
            direction = "desc";
            arrow = $('<i class="fa fa-angle-down"></i>');
        } else {
            // First click on a column or different column, sort in ascending order
            direction = "asc";
            arrow = $('<i class="fa fa-angle-up"></i>');
        }

        $table.data("sort-direction", direction);
        $table.data("sort-column", column);

        // Remove any existing arrows from all header cells
        $table.find("th svg, th span").remove();

        // add arrow to the element th in the direction it should be
        const arrowWithSpace = $('<span>&nbsp;</span>').append(arrow);
        $(element).closest('th').append(arrowWithSpace);


        // sorting function
        rows.sort((a, b) => {
            const aValue = a.cells.item(column).innerHTML;
            const bValue = b.cells.item(column).innerHTML;

            const isANumber = !isNaN(parseFloat(aValue)) && isFinite(aValue);
            const isBNumber = !isNaN(parseFloat(bValue)) && isFinite(bValue);

            if (isANumber && isBNumber) {
                return direction === "asc" ? parseFloat(aValue) - parseFloat(bValue) : parseFloat(bValue) - parseFloat(aValue);
            }

            if (!isANumber && !isBNumber) {
                return direction === "asc" ? aValue.localeCompare(bValue) : bValue.localeCompare(aValue);
            }

            return isANumber ? -1 : 1;
        });

        $tbody.empty();
        rows.forEach(row => $tbody.append(row));
    }


    //* Recursive function that creates the RelaX output Tree
    function createRecList(output) {
        var container = $("<li></li>"); // Creates container holding section of tree
        var button = $("<div></div>"); // creates first node of this secton tree

        // fills node attributes
        button.attr("id", "button-" + output._functionName);
        if (activeNode == null) {
            button.attr("class", "node active");
            activeNode = button;
        } else {
            button.attr("class", "node");
        }

        var text = output._functionName
        if (text === '_inlineRelation8') {
            button.append(output._codeInfo.text);
        } else {
            button.append(output.getFormulaHtml(false));
        }
        dropdown = createTreeNodeDropdown(output);
        button.append(dropdown)
        // allows each node to return the output at that point of  execution 
        button.on("click", function () {
            activeNode.attr("class", "node");
            button.attr("class", "node active");
            activeNode = button;
            createOutputTable(output);
        });

        // Checks to see if there are 2, 1, or no Children
        if ((output._child != null) && (output._child2 != null)) {
            container.append(button); // adds the main node
            // creates flex container.for children - allowing for side by side rendering
            var newUlDiv = $("<ul></ul>");
            var newLiDiv = $("<li></li>");

            // adds the child nodes

            newLiDiv.append(createRecList(output._child));
            newLiDiv.append(createRecList(output._child2));
            newUlDiv.append(newLiDiv);
            container.append(newUlDiv); // appends flex container to above container
            return container;
        } else if (output._child != null) {
            var newUlDiv = $("<ul></ul>");
            var newLiDiv = $("<li></li>");

            container.append(button); // adds the main node.

            newLiDiv.append(createRecList(output._child)); // adds the child node
            newUlDiv.append(newLiDiv);
            container.append(newUlDiv);
            return container;
        } else {
            return container.append(button); // adds the main node
        }
    }

});

function createTreeNodeDropdown(output) {

    // Creates the submenue element for the table, onclick each member of the table will add itself to the editor
    var maxColNameLength = 0;
    var maxColTypeLength = 0;
    var dropdown = $("<div class='tree-popup'><em>columns:</em></div>")
    var columns = output.getSchema().getColumns().map(function (col, i) {


        if (col.toString().length > maxColNameLength) {
            maxColNameLength = output.getSchema().getName(i).length + 3;
        }
        if (output.getSchema().getType(i).length > maxColTypeLength) {
            maxColTypeLength = output.getSchema().getType(i).length + 2;
        }


        var div = $(`<div class='submenu'>`)
        div.attr("style", "text-align: center; border: 1px solid white; padding: 0.2em; display: flex; justify-content: space-around;");
        div.attr("class", "submenu");
        return div;
    });

    for (var i = 0; i < columns.length; i++) {
        let name = `<span style='width: ${maxColNameLength}ch; font-size: 16px;'>${output.getSchema().getName(i)}</span>`;
        let type = `<span style='width: 8 ch; font-size: 16px;'><small>${output.getSchema().getType(i).toUpperCase()}</small></span>`;
        columns[i].append(name);
        columns[i].append(type);

    }

    dropdown.append(columns);
    // dropdown.append($("<ul></ul>").append(columns));
    if (output.hasMetaData('naturalJoinConditions')) {
        var naturalJoinConditions = output.getMetaData('naturalJoinConditions');


        var listItems = naturalJoinConditions.map(function (condition) {

            var div = $(`<div class='submenu'>`)
            div.attr("style", "text-align: center; border: 1px solid white; padding: 0.2em; display: flex; justify-content: space-around;");
            div.attr("class", "submenu");

            var condSpan = $(`<span style='font-size: 16px;'>${condition.getFormulaHtml()}</span>`)
            div.append(condSpan)
            return div;
        });

        var joinSpan = '<span style="width: 24ch; display: block; margin: auto">Natural Join Conditions:</span>';
        dropdown.append(joinSpan);
        dropdown.append(listItems);
    }
    if (output.getMetaData('isInlineRelation') === true && n.hasMetaData('inlineRelationDefinition')) {
        dropdown.append(output.getMetaData('<span>inlineRelationDefinition</span>'))
    }
    dropdown.append(`<small>${output.getResultNumRows()} row${output.getResultNumRows() === 1 ? '' : 's'}</small>`)


    return dropdown;
}