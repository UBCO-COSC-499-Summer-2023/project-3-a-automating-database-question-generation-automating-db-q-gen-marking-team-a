const fs = require('fs');

// Read relalg_bundle.js content as a string
const relalgBundleCode = fs.readFileSync('relalg_bundle.js', 'utf8');

// Execute relalg_bundle.js code
eval(relalgBundleCode);

// Import the necessary functions and objects from relalg_bundle
const executeRelalg = relalg_bundle.executeRelalg;
const Relation = relalg_bundle.Relation;

// Define the execute_Relalg_JS function
function execute_Relalg_JS(query, dataStuff) {
    const PR = executeRelalg(query, dataStuff);
    return PR;
}

// Call the execute_Relalg_JS function with arguments if needed
// const result = execute_Relalg_JS(query, dataStuff);
