const createTableRows = require("../../databaseCourse/elements/pl-sql-element/renderer");
const createTableHeader = require("../../databaseCourse/elements/pl-sql-element/renderer")
const createSchemaTables = require("../../databaseCourse/elements/pl-sql-element/renderer")
const rendererModule = require("../../databaseCourse/elements/pl-sql-element/renderer")

// createTableRows Tests -------------------------------------------------------

// 1. tests that the function produces an empty array when the input is null
test("createTableRows - no rows", ()=>{
    expect(createTableRows()).toBeNull()
})
// 2. n number of inputs
test("createTableRows - 1 row", ()=>{
    expect(createTableRows(["example"])).toBeNull()
})
// 3. Different type of input?


// createTableHeader Tests -------------------------------------------------------



// createSchemaTableHeader Tests -------------------------------------------------



// getTableName Tests ------------------------------------------------------------