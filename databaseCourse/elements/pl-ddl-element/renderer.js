// sql.js API docs found here: https://sql.js.org/documentation/Statement.html#%255B%2522getAsObject%2522%255D

$(document).ready(function () {

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

    /*
    //
    // Functions regarding the rendering of the Database Schema -------------------------------------------------------------------
    // modeled after the schema & dropdowns visualization found in autoEr
    */

    // Function that shows DB schema/tables
    function showDBTables() {

        dbSchemaElm.contents().remove();

        $.each(tables, function (index, table) {

            let sqlQuery = `SELECT name, type FROM pragma_table_info("${table}");`;
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
        + "<button type='button' onClick='openMenu(this)' class='dropbtn' id='btn-" + tableName + "'>" + tableName 
        + "</button> <div class='dropdown-content' id='schema-" + tableName + "'>"

        // create a row for each field in the table
        for (var i = 0; i < schemaFields[0].values.length; i++) {
            let field = "<div style='text-align:center;padding:0.2em;border:0.2px solid white;' classname='submenu' id='schema-" 
            + tableName + "'>" + schemaFields[0].values[i][0] 
            + " , " +  schemaFields[0].values[i][1] + "</div>"
            schemaView+=(field)
        }

        schemaView += "</div></div>"
        return schemaView
    }

    /*
    //
    // Functions regarding the dropdowns' visbility ---------------------------------------------------------------------------
    // modeled after the dropdowns found in autoEr
    */

    // function to show the dropdown of the selected schema
    window.openMenu = function(tableName){
        // so that only the dropdown of one schema is open at a time
        closeMenus();
        let schemaDropdownId = 'schema-' + tableName.id.slice(4)
        document.getElementById(schemaDropdownId).classList.toggle('show');
    }

    // function to close any and all dropdowns that are showing
    function closeMenus(){
        let allDropDownsClass = 'dropdown-content'
        let dropdowns = document.getElementsByClassName(allDropDownsClass);
        for(let i = 0; i < dropdowns.length; i++){
            if(dropdowns[i].classList.contains('show')){
                dropdowns[i].classList.remove('show')
            }
        }
    }

    // close and and all open dropdowns if the user clicks away from schema table name buttons
    window.onclick = function(e){
        if(!e.target.matches('.dropbtn')){
            closeMenus()
        }
    }


    /*
    //
    // Functions regarding the SQL editor execute button -------------------------------------------------------------------
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
            outputElm.append(output.map(item => (item !== undefined ? item : "") + "<br>").join(""));
        }
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

        var table = $("<table></table>");

        table.append(createTableHeader(columns));

        for (var i = 0; i < results.length; i++) {

            table.append(createTableRows(results[i].values));

        }

        outputElm.append(table);

    }

    // Function that creates the table header
    function createTableHeader(columns) {


        var header = $("<thead></thead>");
        var headerRow = $("<tr></tr>");

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

});

module.exports = tableCreate;