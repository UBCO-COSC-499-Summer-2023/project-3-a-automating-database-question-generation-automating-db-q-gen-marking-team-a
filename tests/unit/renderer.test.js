const tableCreate = require('../../databaseCourse/elements/pl-ddl-element/renderer')

test("makes table properly", ()=>{
    expect(tableCreate()).toBe(false)
})