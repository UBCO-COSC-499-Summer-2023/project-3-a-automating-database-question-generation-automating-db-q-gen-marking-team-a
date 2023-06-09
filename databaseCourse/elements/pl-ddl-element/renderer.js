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

    //var input = $("#commands");

    function execute(sqlCode){

        outputElm.contents().remove();

        let results = db.exec(sqlCode);
        console.log(results)

        outputElm.append(createTable(results));

    }

    function executeEditorContents() {

        execute(editor.getValue());

    }


    function createTable(results) {
        for (var i = 0; i < results.length; i++) {
            console.log(results[i]);

            var table = $("<table></table>");

            table.append(createTableHeader(results[i].columns));
            table.append(createTableRows(results[i].values));

            outputElm.append(table);
        }
    }

    function createTableHeader(columns) {
        var headerRow = $("<tr></tr>");
        Object.keys(columns).forEach(function (columnName) {
            var th = $("<th></th>").text(columns[columnName]);
            headerRow.append(th);
        });
        return headerRow;
    }

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

    // Add syntax highlighting to the textarea
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

});