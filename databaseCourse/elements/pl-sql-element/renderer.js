// sql.js API docs found here: https://sql.js.org/documentation/Statement.html#%255B%2522getAsObject%2522%255D

$(document).ready(function () {

    // Function to load the required database for the question
    window.onload = function () {
        dbInitElm = $("#db-init");
        // turns on foreign keys
        execute("PRAGMA foreign_keys = ON;");
        if (dbInitElm.text().length > 0) {
            execute(dbInitElm.text());
        }
        dbInitElm.remove();

        updateCodeMirrorPreviousSubmission();

    }

    /*
    //
    // Initializing sql.js and wasm--------------------------------------------------------------------------------------------
    //
    */

    // wasm file required for sql.js
    let config = {
        locateFile: () => {
            "https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/sql-wasm.wasm"
        }
    }

    var db;
    // Initialize the db with sql.js
    initSqlJs(config).then(function (SQL) {
        db = new SQL.Database();
    });

    var execBtn = $("#execute");
    execBtn.on("click", executeEditorContents);

    const commandsElm = $("#commands");

    const outputElm = $("#output");

    const errorElm = $("#error");

    const dbSchemaElm = $("#db-schema");

    previousSubmissionElm = $("#previousSubmission");

    const tables = [];

    // Add syntax highlighting to the textarea
    // Also transforms the textarea into a CodeMirror editor
    var editor = CodeMirror.fromTextArea(commandsElm[0], {
        mode: 'text/x-mysql',
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

    // Load previous submission into editor
    
    

    /*
    //
    // Functions regarding rendering the Question correctly -------------------------------------------------------------------
    // 
    */
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

    /*
    //
    // Functions regarding the rendering of the Database Schema -------------------------------------------------------------------
    // modeled after the schema & dropdowns visualization found in autoEr
    */

    // Function that shows DB schema/tables
    function showDBTables() {

        dbSchemaElm.contents().remove();

        $.each(tables, function (index, table) {

            let sqlQuery = `SELECT name, type, pk FROM pragma_table_info("${table}");`;
            let sqlResult = db.exec(sqlQuery);

            // create table of sql result and append to dbSchemaElm
            dbSchemaElm.append(createSchemaTables(sqlResult, table));
        })

        if (dbSchemaElm.contents().length === 0) {
            dbSchemaElm.append("No tables found");
        }

    }

    // Function that creates tables that showcase schema fields
    function createSchemaTables(schemaFields, tableName) {

        // if tables have no rows, means table does not exist
        if (schemaFields.length === 0) {
            return;
        }

        // creates html button for the table as well as layout for dropdown
        let schemaView = "<div class='schemaTable'>"
            + `<button type='button' onclick='addTableToEditor("${tableName}")' class='dropbtn' id='btn-" + tableName + "'>` + tableName
            + "</button> <div onmouseleave='' class='dropdown-content' id='schema-" + tableName + "'>"

        let foreignKeys = getForeignKey(tableName);

        // get column widths for styling purposes
        let maxColNameLength = 0;
        let maxColTypeLength = 0;
        let maxColKeyLength = 0;

        for (const row of schemaFields[0].values) {
            let keys = getKeysString(row, foreignKeys);

            let colName = `${row[0]}`;
            let colType = `${row[1]}`;
            let colKey = `${keys}`;

            if (colName.length > maxColNameLength) {
                maxColNameLength = colName.length + 2;
            }

            if (colType.length > maxColTypeLength) {
                maxColTypeLength = colType.length + 2;
            }

            if (colKey.length > maxColKeyLength) {
                maxColKeyLength = colKey.length + 2;
            }
        }

        // adds headers to schema table
        let field = `<div style="text-align: center; border: 1px solid white; padding: 0.2em; display: flex; justify-content: space-around;" class="submenu" id="schema-${tableName}">`;
        let colName = `<span style=" font-weight: bold; width: ${maxColNameLength}ch;">Columns</span>`;
        let colType = `<span style=" font-weight: bold; width: ${maxColTypeLength}ch;">Types</span>`;
        let colKey = `<span style=" font-weight: bold; width: ${maxColKeyLength}ch;">Keys</span>`;

        field += colName + colType + colKey + '</div>';

        schemaView += field;

        // populates each row of scehma table
        for (const row of schemaFields[0].values) {

            let keys = getKeysString(row, foreignKeys);

            let field = `<div style="text-align: center; border: 1px solid white; padding: 0.2em; display: flex; justify-content: space-around;" class="submenu" id="schema-${tableName}">`;
            let colName = `<span onclick="addColumnToEditor('${tableName}', '${row[0]}')" style=" cursor: pointer; width: ${maxColNameLength}ch;">${row[0]}</span>`;
            let colType = `<span style=" width: ${maxColTypeLength}ch;">${row[1]}</span>`;
            let colKey = `<span style=" width: ${maxColKeyLength}ch;">${keys}</span>`;

            field += colName + colType + colKey + '</div>';

            schemaView += field;
        }

        schemaView += "</div></div>"
        return schemaView
    }

    // function that returns a string indicating the type of keys
    function getKeysString(row, foreignKeys) {

        let keyString = "";

        if (row[2] > 0 && foreignKeys.includes(row[0])) {
            keyString = " {PK, FK}"
        } else if (row[2] > 0) {
            keyString = " {PK}"
        } else if (foreignKeys.includes(row[0])) {
            keyString = " {FK}"
        }

        return keyString;

    }

    // Function that returns an array of all foreign keys in passed in table
    function getForeignKey(tableName) {

        let foreignKeys = [];
        let sqlQuery = `SELECT * FROM pragma_foreign_key_list("${tableName}");`;
        let sqlResult = db.exec(sqlQuery);

        if (sqlResult.length === 0) {
            return foreignKeys;
        }

        // put all foreign keys in an array from value index 3
        for (var row of sqlResult[0].values) {
            const columnName = row[3];
            foreignKeys.push(columnName);
        }

        return foreignKeys;

    }

    /*
    //
    // Functions regarding the SQL editor  -------------------------------------------------------------------
    //
    */

    // Execute the sql code
    // Create table
    function execute(sqlCode) {

        // clear all previous results
        outputElm.contents().remove();
        errorElm.contents().remove();

        // iterate through all statements in editor
        // execute each statement sequentially
        try {

            for (const statement of db.iterateStatements(sqlCode)) {
                const sqlStatement = statement.getSQL();

                // get column names
                let tableColumnNames = statement.getColumnNames();

                // execute sql statement
                let sqlStatementResult = db.exec(sqlStatement);

                // give user feedback based on type of sql statement
                showSqlStatementFeedback(sqlStatement, tableColumnNames, sqlStatementResult);

                // update DB schema
                showDBTables();
            }

        } catch (e) {
            errorElm.append(e);
            console.log(e);
        }
    }

    // Functions that runs when the button is clicked
    // Executes the sql code
    function executeEditorContents() {

        execute(editor.getValue());

    }

    // Function that shows the user feedback based on the SQL queries they run
    function showSqlStatementFeedback(sqlStatement, tableColumnNames, sqlStatementResult) {
        const regex = /(CREATE TABLE|DROP TABLE|INSERT INTO|DELETE FROM|UPDATE|SELECT)/i;
        const match = sqlStatement.match(regex);

        if (match) {
            let table;
            const output = [];

            switch (match[0].toUpperCase()) {
                case "CREATE TABLE":
                    table = getTableName(/CREATE TABLE\s+(\w+)/i, sqlStatement);
                    tables.push(table); // add table to array of DB tables
                    output.push(`Created table: ${table} successfully.`);
                    break;

                case "DROP TABLE":
                    table = getTableName(/DROP TABLE(?:\s+IF EXISTS)?\s+(\w+)/i, sqlStatement);
                    output.push(`Dropped table: ${table} successfully.`);
                    const index = tables.indexOf(table);
                    if (index > -1) {
                        tables.splice(index, 1); // remove table from DB tables array
                    }
                    break;

                case "INSERT INTO":
                    table = getTableName(/INSERT INTO\s+(\w+)/i, sqlStatement);
                    output.push(`Inserted into table: ${table} successfully.`);
                    break;

                case "DELETE FROM":
                    table = getTableName(/DELETE FROM\s+(\w+)/i, sqlStatement);
                    output.push(`Deleted from table: ${table} successfully.`);
                    break;

                case "UPDATE":
                    table = getTableName(/UPDATE\s+(\w+)/i, sqlStatement);
                    output.push(`Updated table: ${table} successfully.`);
                    break;

                case "SELECT":
                    output.push(createOutputTable(tableColumnNames, sqlStatementResult));
                    break;

                default:
                    break;
            }
            // if query wasn't run from the editor, output equals "Database initialized."
            if (editor.getValue() == "") {
                if (outputElm.text() != "Database initialized.") {
                    outputElm.text("Database initialized.");
                }
            } else {
                outputElm.append(output.map(item => (item !== undefined ? item : "") + "<br>").join(""));
            }
        }
    }

    // function that allows you to click the table and add it to editor
    window.addTableToEditor = function (tableName) {
        updateCodeMirror(`${tableName}`);
    }

    // function that allows you to click the column type and add it to editor
    window.addColumnToEditor = function (tableName, columnName) {

        updateCodeMirror(`${columnName}`);
    }

    // adds table.column to editor at cursor location
    function updateCodeMirror(data) {
        var doc = editor.getDoc(); //gets the information of the editor
        doc.replaceRange(data, doc.getCursor()); // adds data at position of cursor
        editor.focus();
        editor.setCursor(doc.getCursor());
    }

    // insert previous submission into editor
    function updateCodeMirrorPreviousSubmission() {
        var doc = editor.getDoc(); //gets the information of the editor
        doc.setValue(previousSubmissionElm.text().trim());
        previousSubmissionElm.remove();
    }

    /*
    //
    // Functions regarding the output table generation -----------------------------------------------------------------------
    //
    */

    // Function that gets the table name from a SELECT SQL statement
    function getTableName(regex, sqlStatement) {


        var match = sqlStatement.match(regex);

        if (match && match.length > 1) {
            return match[1];
        } else {
            return null; // or handle the case where table name is not found
        }
    }


    //Function that creates the output table
    function createOutputTable(columns, results) {

        var div = $("<div></div>");
        div.addClass("scrollable")
        var table = $("<table></table>");
        table.addClass("output-tables")


        table.append(createTableHeader(columns));

        for (var i = 0; i < results.length; i++) {

            table.append(createTableRows(results[i].values));

        }

        div.append(table);
        outputElm.append(div);

    }

    // Function that creates the table header
    function createTableHeader(columns) {

        var header = $("<thead></thead>");
        var headerRow = $("<tr></tr>");

        for (var i = 0; i < columns.length; i++) {

            // used to snapshot the i value to pass to sortTable
            (function (column) {
                var th = $("<th></th>").text(columns[column]);

                th.on("click", function () {
                    sortTable(this, column);
                });

                headerRow.append(th);
            })(i);
        }

        header.append(headerRow);
        return header;
    }

    // Function that creates the table rows for a table
    function createTableRows(rows) {

        let numRows = rows.length;
        let limitRows = 200;

        // limit the number of rows being created in DOM for performance
        if (numRows > limitRows) {
            rows.length = limitRows;
        }

        var tbody = $("<tbody></tbody>");
        var rowElements = [];
        rows.forEach(function (row) {
            var tr = $("<tr></tr>");
            row.forEach(function (value) {
                // round to 2 decimal places
                if (typeof value == 'number' && !Number.isInteger(value)) {
                    value = value.toFixed(2);
                }

                // add null text if field is null, 0 should show "0"
                if (value == null) {
                    value = "NULL";
                }

                var td = $("<td></td>").text(value);
                tr.append(td);
            });
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


});