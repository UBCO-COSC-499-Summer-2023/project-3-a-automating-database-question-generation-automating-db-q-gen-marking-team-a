$(document).ready(function () {
    //* QUESTION SETUP
    const executeRelalg = relalg_bundle.executeRelalg;
    const Relation = relalg_bundle.Relation;

    // database setup
    const dbSchema = document.getElementById("database");
    const dbValue = dbSchema.getAttribute("value");
    const dbArray = dbValue.split(";");
    const dataset = [dbArray.length];
    for (var i = 0; i < dbArray.length; i++){   
        dataset[i] = executeRelalg(dbArray.at(i), {});
    }
    // Creating dropbtn (Schema) tables
    for(var i = 0; i < dataset.length; i++) {
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

    //* needed elemnents for rendering.
    var treeElm = $("#tree");
    var outputElm = $("#output");
    var errorElm = $("#error");
    var execBtn = $("#execute");
    execBtn.on("click", executeEditorContents);
    


    //* FUNCTION DEFINITIONS
    
    //* FUNCTIONS - USER ACTIONS
    // opens Schema list for selected schema.
    window.openMenu = function (val) {
        closeMenus();
        document.getElementById('schema-' + val.id.slice(4)).classList.toggle('show');
    }
    // closes menus when mouse is clicked elsewhere
    window.onclick = function (e) {
        if (!e.target.matches('.dropbtn')) {
            closeMenus()
        }
    }

    // function to close the modals of the schemas, basically hides each field in the modal
    // helper function for above two window methods.
    function closeMenus() {
        let dropdowns = document.getElementsByClassName('dropdown-content');
        for (let i = 0; i < dropdowns.length; i++) {
            if (dropdowns[i].classList.contains('show')) {
                dropdowns[i].classList.remove('show')
            }
        }
    }

    // adds functionality for onclick
    function updateCodeMirror(data){
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
    function executeEditorContents() {
        //! d1 and d2 cannot be used to replace "S" and "P"
        //? How can we fix the "S" and "P" issue
        var d1 = dataset.at(0)._schema._relAliases.at(0);
        var d2 = dataset.at(1)._schema._relAliases.at(0);

        try {
            const PR = executeRelalg(editor.getValue(), { "S" : dataset[0], "P" : dataset[1]}); // gets query results
            treeElm.contents().remove(); // clears Tree previous results
            createOutputTable(PR); // creates and renders new output table
            treeElm.append(createRecList(PR)); // creates and renders new tree
        } catch (err) {
            createErrorOutput(err); // creates and renders error in event user has incorrect RA query 
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
        let schemaView = "<button type='button' onmouseover='openMenu(this)' onClick='updateCodeMirror(\""+dataSchema._relAliases[0]+"\");' class='dropbtn' id='btn-" + dataSchema._relAliases[0] + "'>" + dataSchema._relAliases[0]
            + "</button> <div class='dropdown-content' id='schema-" + dataSchema._relAliases[0] + "'>"

        // Creates the submenue element for the table, onclick each member of the table will add itself to the editor
        for (var i = 0; i < dataSchema._names.length; i++) {
            let field = "<div classname='submenu' onClick='updateCodeMirror(\""+dataSchema._names[i]+"\");' id='schema-" + dataSchema._relAliases[0] + "'>" + dataSchema._names[i] +", " + dataSchema._types[i] + "</div>"
            schemaView += field;
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
        table.append(createTableHeader(output.getResult()._schema._names)); // creates table headers
        table.append(createTableRows(output.getResult()._rows)); // fills table rows
        outputElm.append(table);
    }

    // Function that creates the table header
    function createTableHeader(columns) {
        var header = $("<thead></thead>");
        var headerRow = $("<tr></tr>");

        // reads each header
        for (var i = 0; i < columns.length; i++) {
            var th = $("<th></th>").text(columns[i]);
            headerRow.append(th);
        }
        header.append(headerRow);
        return header;
    }

    // Function that creates the table rows for a table
    function createTableRows(rows) {
        var rowElements = [];
        // reads each row in rows and adds them to the row element array.
        rows.forEach(function (row) {
            var tr = $("<tr></tr>");
            row.forEach(function (value) {
                var td = $("<td></td>").text(value);
                tr.append(td);
            });
            rowElements.push(tr);
        });
        return rowElements;
    }

    //* Recursive function that creates the RelaX output Tree
    function createRecList(output){
        var container = $("<div style='margin: 5px'></div>"); // Creates container holding section of tree
        var button = $("<div></div>"); // creates first node of this secton tree

        // fills node attributes
        button.attr("id", "button-"+output._functionName);
        button.addClass("btn btn-primary exec-button selection");
        button.text(output._codeInfo.text);
        // allows each node to return the output at that point of execution 
        button.on("click", function() { createOutputTable(output); });
        
        // Checks to see if there are 2, 1, or no Children
        if ((output._child != null) && (output._child2 != null)) {
            container.append(button); // adds the main node
            // creates flex container.for children - allowing for side by side rendering
            var newContainer = $("<div></div>");
            newContainer.addClass("flex-container")
            
            // adds the child nodes
            newContainer.append(createRecList(output._child));
            newContainer.append(createRecList(output._child2));
            container.append(newContainer); // appends flex container to above container
            return container;
        } else if (output._child != null) { 
            container.append(button); // adds the main node.
            container.append(createRecList(output._child)); // adds the child node
            return container; 
        } else {
            return container.append(button); // adds the main node
        } 
    }
});
