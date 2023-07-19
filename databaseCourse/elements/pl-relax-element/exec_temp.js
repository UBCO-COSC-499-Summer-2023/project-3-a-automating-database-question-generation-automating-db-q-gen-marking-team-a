// Contents of exec_relalg_bundle.js

const fs = require('fs');

// Read relalg_bundle.js content as a string
const relalgBundleCode = fs.readFileSync(process.env.RELALG_BUNDLE_PATH, 'utf8');

// Execute relalg_bundle.js code
eval(relalgBundleCode);

// Import the necessary functions and objects from relalg_bundle
const executeRelalg = relalg_bundle.executeRelalg;
const Relation = relalg_bundle.Relation;

// Function to execute relational algebra query and return the result
function execute_Relalg_JS(query, dataStuff) {
    const PR = executeRelalg(query, dataStuff);
    return PR;
}

// Export the execute_Relalg_JS function so that it can be called from Python
module.exports = {
    execute_Relalg_JS: execute_Relalg_JS
};
