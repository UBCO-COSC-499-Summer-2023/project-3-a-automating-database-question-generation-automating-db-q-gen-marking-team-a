// sql.js API docs found here: https://sql.js.org/documentation/Statement.html#%255B%2522getAsObject%2522%255D

$(document).ready(function () {

    let config = {
        locateFile: () => {
            "https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/sql-wasm.wasm"
        }
    }

    var db;
    // Initialize the db with sql.js
    initSqlJs(config).then(function (SQL) {
        console.log("sql.js initialized 🎉");

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

    // Execute the sql code
    // Create table
    // TODO: Refactor all code that creates tables using sql.js API
    function execute(sqlCode) {

        outputElm.contents().remove();
        errorElm.contents().remove();

        try {

            for (const statement of db.iterateStatements(sqlCode)) {
                const sqlStatement = statement.getSQL();

                let tableColumnNames = statement.getColumnNames();
                //console.log(tableColumnNames);

                let sqlStatementResult = db.exec(sqlStatement);

                // give user feedback based on type of sql statement
                showSqlStatementFeedback(sqlStatement, tableColumnNames, sqlStatementResult);

            }

        } catch (e) {
            console.log(e);
            errorElm.append(e);
        }

    }

    // Functions that runs when the button is clicked
    // Executes the sql code
    function executeEditorContents() {

        execute(editor.getValue());

    }

    // Function that shows DB schema/tables
    function showDBTables() {

        $.each(tables, function (index, table) {

            let sqlQuery = 'SELECT * FROM pragma_table_info("{table}")';

        })


    }

    // Function that gets the type of SQL statement executed
    function showSqlStatementFeedback(sqlStatement, tableColumnNames, sqlStatementResult) {

        var regex = /(CREATE TABLE|DROP TABLE|INSERT INTO|DELETE FROM|UPDATE|SELECT)/i;
        var match = sqlStatement.match(regex);

        if (match) {

            let table = getTableName(sqlStatement);

            switch (match[0].toUpperCase()) {

                case "CREATE TABLE":
                    // do something for "CREATE TABLE" match
                    tables.push(table);
                    outputElm.append(`Created table: ${table} successfully.\n`);
                    break;
                case "DROP TABLE":
                    // do something for "DROP TABLE" match
                    outputElm.append(`Dropped table: ${table} successfully.\n`);
                    break;
                case "INSERT INTO":
                    // do something for "INSERT INTO" match
                    outputElm.append(`Inserted into table: ${table} successfully.\n`);
                    break;
                case "DELETE FROM":
                    // do something for "DELETE FROM" match
                    outputElm.append(`Deleted from table: ${table} successfully.\n`);
                    break;
                case "UPDATE":
                    // do something for "UPDATE" match
                    outputElm.append(`Updated table: ${table} successfully.\n`);
                    break;
                case "SELECT":
                    outputElm.append(createOutputTable(tableColumnNames, sqlStatementResult));
                    break;
                default:
                    // handle unknown keyword here
                    break;
            }
        }
    }

    // Function that gets the table name from a SELECT SQL statement
    function getTableName(sqlStatement) {

        // TODO

      }

    //Function that creates the table
    function createOutputTable(columns, results) {

        //console.log(columns);
        //console.log(results);

        var table = $("<table></table>");

        table.append(createTableHeader(columns));

        for (var i = 0; i < results.length; i++) {

            table.append(createTableRows(results[i].values));

        }

        outputElm.append(table);

    }

    // Function that creates the table header
    // Not sure if this is the best way to do this
    // Needs to be tested
    function createTableHeader(columns) {

        //console.log(columns);

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
    // Not sure if this is the best way to do this
    // Needs to be tested
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