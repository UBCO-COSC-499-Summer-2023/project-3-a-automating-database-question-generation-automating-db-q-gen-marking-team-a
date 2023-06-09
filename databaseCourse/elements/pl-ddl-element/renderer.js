$(document).ready(function () {

    let config = {
        locateFile: () => {
            "https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/sql-wasm.wasm"
        }
    }

    var execBtn = $("#execute");
    console.log(execBtn);
    execBtn.on("click", execute);

    var db;

    var outputElm = $("#output");

    initSqlJs(config).then(function (SQL) {
        console.log("sql.js initialized 🎉");

        db = new SQL.Database();

        let input = $("#commands").val();

        let results = db.exec(input);
        console.log(results)

        outputElm.append(createTable(results));

    });

    function execute(){

        outputElm.contents().remove();

        let input = $("#commands").val();

        let results = db.exec(input);
        console.log(results)

        outputElm.append(createTable(results));

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


});