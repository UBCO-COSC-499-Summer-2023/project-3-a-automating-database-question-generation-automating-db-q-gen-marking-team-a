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

    var commandsElm = $("#commands");

    var outputElm = $("#output");

    var errorElm = $("#error");

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

        console.log(sqlCode);

        outputElm.contents().remove();
        errorElm.contents().remove();

        var results;

        try {
           results = db.exec(sqlCode);
           //console.log("Query results: ", results);
           outputElm.append(createTable(results));

        } catch (e) {
            console.log(e);
            errorElm.text(e);
        }

    }

    // Functions that runs when the button is clicked
    // Executes the sql code
    function executeEditorContents() {

        execute(editor.getValue());

    }

    //Function that creates the table
    function createTable(results) {

        for (var i = 0; i < results.length; i++) {
            console.log(results[i]);

            var table = $("<table></table>");

            table.append(createTableHeader(results[i].columns));
            table.append(createTableRows(results[i].values));

            outputElm.append(table);

        }
    }


    
    // Function that creates the table header
    // Not sure if this is the best way to do this
    // Needs to be tested
    function createTableHeader(columns) {

        //console.log(columns);
        //SELECT * FROM pragma_table_info('airplane');

        var headerRow = $("<tr></tr>");
        Object.keys(columns).forEach(function (columnName) {
            var th = $("<th></th>").text(columns[columnName]);
            headerRow.append(th);
        });
        return headerRow;

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