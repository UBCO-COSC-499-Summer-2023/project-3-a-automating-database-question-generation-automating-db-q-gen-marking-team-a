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

    // Function that shows DB schema/tables
    function showDBTables() {

        dbSchemaElm.contents().remove();

        $.each(tables, function (index, table) {

            let sqlQuery = `SELECT name, type FROM pragma_table_info("${table}");`;
            let sqlResult = db.exec(sqlQuery);
            
            // create table of sql result and append to dbSchemaElm
            dbSchemaElm.append(createSchemaTables(sqlResult, table));


        })
    }

    // Function that creates tables that showcase schema
    function createSchemaTables(results, tableName){

        let table = $("<table></table>");
        let header = $("<thead></thead>");
        let headerRow = $("<tr></tr>");
        let tableHeader = $(`<th colspan="2">${tableName}</th>`);
        headerRow.append(tableHeader);
        header.append(headerRow);
        table.append(header);

        for (var i = 0; i < results.length; i++) {
            table.append(createTableRows(results[i].values));
        }
        return table;

    }


    /*
    //
    // Functions regarding the SQL editor execute button
    //
    */

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

                let sqlStatementResult = db.exec(sqlStatement);

                // give user feedback based on type of sql statement
                showSqlStatementFeedback(sqlStatement, tableColumnNames, sqlStatementResult);

                // update DB schema
                showDBTables();
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
                    table = getTableName(/DROP TABLE\s+IF EXISTS?\s?(\w+)/i, sqlStatement);
                    const index = tables.indexOf(table);
                    if (index > -1) {
                        tables.splice(index, 1);
                    }
                    console.log(tables);
                    output.push(`Dropped table: ${table} successfully.`);
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
    // Not sure if this is the best way to do this
    // Needs to be tested
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



/* Testing Queries 


CREATE TABLE airplane ( id CHAR(10) , model CHAR(20), manufacture_date DATE );

CREATE TABLE dept (
   deptId integer,
   deptName varchar(40),
   deptLocation varchar(50),
   primary key (deptId)
);

CREATE TABLE courseDept (
   deptId integer,
   cname varchar(40),   
   primary key (deptId, cname),
   FOREIGN KEY (cname) REFERENCES course (cname) ON UPDATE CASCADE,
   FOREIGN KEY (deptId) REFERENCES dept (deptId) ON UPDATE CASCADE
); 

CREATE TABLE emp (
 eno CHAR(5) NOT NULL,
 ename VARCHAR(30),
 bdate DATE,
 title CHAR(2),			
 salary DECIMAL(9,2),
 supereno CHAR(5),
 dno CHAR(5),
 PRIMARY KEY (eno)
);
CREATE TABLE proj (
 pno CHAR(5) NOT NULL,
 pname VARCHAR(40),
 budget DECIMAL(9,2),
 dno  CHAR(5), 
 PRIMARY KEY (pno),
 CONSTRAINT FK_proj_dept FOREIGN KEY (dno) REFERENCES dept(dno) ON DELETE SET NULL);



DROP TABLE IF EXISTS employees;
CREATE TABLE employees( id          integer,  name    text,
                          designation text,     manager integer,
                          hired_on    date,     salary  integer,
                          commission  float,    dept    integer);

  INSERT INTO employees VALUES (1,'JOHNSON','ADMIN',6,'1990-12-17',18000,NULL,4);
  INSERT INTO employees VALUES (2,'HARDING','MANAGER',9,'1998-02-02',52000,300,3);
  INSERT INTO employees VALUES (3,'TAFT','SALES I',2,'1996-01-02',25000,500,3);
  INSERT INTO employees VALUES (4,'HOOVER','SALES I',2,'1990-04-02',27000,NULL,3);
  INSERT INTO employees VALUES (5,'LINCOLN','TECH',6,'1994-06-23',22500,1400,4);
  INSERT INTO employees VALUES (6,'GARFIELD','MANAGER',9,'1993-05-01',54000,NULL,4);
  INSERT INTO employees VALUES (7,'POLK','TECH',6,'1997-09-22',25000,NULL,4);
  INSERT INTO employees VALUES (8,'GRANT','ENGINEER',10,'1997-03-30',32000,NULL,2);
  INSERT INTO employees VALUES (9,'JACKSON','CEO',NULL,'1990-01-01',75000,NULL,4);
  INSERT INTO employees VALUES (10,'FILLMORE','MANAGER',9,'1994-08-09',56000,NULL,2);
  INSERT INTO employees VALUES (11,'ADAMS','ENGINEER',10,'1996-03-15',34000,NULL,2);
  INSERT INTO employees VALUES (12,'WASHINGTON','ADMIN',6,'1998-04-16',18000,NULL,4);
  INSERT INTO employees VALUES (13,'MONROE','ENGINEER',10,'2000-12-03',30000,NULL,2);
  INSERT INTO employees VALUES (14,'ROOSEVELT','CPA',9,'1995-10-12',35000,NULL,1);

SELECT designation,COUNT(*) AS nbr, (AVG(salary)) AS avg_salary FROM employees GROUP BY designation ORDER BY avg_salary DESC;
SELECT name,hired_on FROM employees ORDER BY hired_on;







*/