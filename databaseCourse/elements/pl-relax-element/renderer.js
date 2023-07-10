$(document).ready(function () {
    //* QUESTION SETUP
    const executeRelalg = relalg_bundle.executeRelalg;
    const Relation = relalg_bundle.Relation;

    // database setup
    const dbSchema = document.getElementById("database");
    const dbValue = dbSchema.getAttribute("value");
    const dbArray = dbValue.split(";");
    const dataset = [dbArray.length];
    for (var i = 0; i < dbArray.length; i++){   
        dataset[i] = executeRelalg(dbArray.at(i), {});
    }
    // Creating dropbtn (Schema) tables
    for(var i = 0; i < dataset.length; i++) {

        dbSchema.innerHTML += createSchemaTables(dataset.at(i)._schema)
    }

    //* USER INTERACTIONS

    // Creates codemirror code block
    var editorInit = $("#RelaXEditor");
    var editor = CodeMirror.fromTextArea(editorInit[0], {
        mode: 'text/RelaX',
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

    //* needed elements for rendering.
    var treeElm = $("#tree");
    var outputElm = $("#output");
    var errorElm = $("#error");
    var execBtn = $("#execute");
    execBtn.on("click", executeEditorContents);
    


    //* FUNCTION DEFINITIONS
    
    //* FUNCTIONS - USER ACTIONS
    // adds functionality for onclick
    function updateCodeMirror(data){
        var doc = editor.getDoc(); // gets the information of the editor
        doc.replaceRange(data, doc.getCursor()); // adds data at position of cursor
        editor.focus();             // focuses the user on the editor
        editor.setCursor(doc.getCursor()); // sets the cursor directly after the newly added char
    }
    // helper function to allow for HTML calling.
    window.updateCodeMirror = function (data) {
        updateCodeMirror(data);
    }
    
    // Execute the RelaX Query
    function executeEditorContents() {
        //! d1 and d2 cannot be used to replace "S" and "P"
        //? How can we fix the "S" and "P" issue
        var d1 = dataset.at(0)._schema._relAliases.at(0);
        var d2 = dataset.at(1)._schema._relAliases.at(0);

        try {
            const PR = executeRelalg(editor.getValue(), { "Customer" : dataset[0], "Product" : dataset[1], "Shipment" : dataset[2], "ShippedProduct" : dataset[3] }); // gets query results
            treeElm.contents().remove(); // clears Tree previous results
            createOutputTable(PR); // creates and renders new output table
            var treeDiv = $('<div class="tree"></div>');
            var ulDiv = $("<ul></ul>");
            
            ulDiv.append(createRecList(PR)); // creates and renders new tree
            treeDiv.append(ulDiv);
            treeElm.append(treeDiv);
        } catch (err) {
            createErrorOutput(err.stack); // creates and renders error in event user has incorrect RA query 
        }
    }
0

    //* FUNCTIONS - RENDERING
    function createSchemaTables(dataSchema) {
        // Checks if table exists, exits if not
        if (dataSchema.length === 0) {
            return;
        }
        // Creates the button HTML element for the table; onclick it adds the tablename to Editor, onhover it shows the schema of the table.
        let schemaView = "<div class='schemaTable'><button type='button' onmouseover='' onClick='updateCodeMirror(\""+dataSchema._relAliases[0]+"\");' class='dropbtn' id='btn-" + dataSchema._relAliases[0] + "'>" + dataSchema._relAliases[0]
            + "</button> <div class='dropdown-content' id='schema-" + dataSchema._relAliases[0] + "'>"

        // get column widths for styling purposes
        let maxColNameLength = 0;
        let maxColTypeLength = 0;

        for (var i = 0; i < dataSchema._names.length; i++) {
            let colName = `${dataSchema._names[i]}`;
            let colType = `${dataSchema._types[i]}`;

            if (colName.length > maxColNameLength) {
                maxColNameLength = colName.length + 2;
            }

            if (colType.length > maxColTypeLength) {
                maxColTypeLength = colType.length + 2;
            }
        }

        // Creates the submenue element for the table, onclick each member of the table will add itself to the editor
        for (var i = 0; i < dataSchema._names.length; i++) {
            let field = `<div style="text-align: center; border: 1px solid white; padding: 0.2em; display: flex; justify-content: space-around;" classname='submenu' id='schema-${dataSchema._relAliases[0]}'>`;
            let name = `<span onClick='updateCodeMirror("${dataSchema._names[i]}")' style='cursor: pointer; width: ${maxColNameLength}ch;'>${dataSchema._names[i]}</span>`;
            let type = `<span style='cursor: pointer; width: ${maxColTypeLength}ch;'>${dataSchema._types[i].toUpperCase()}</span>`;

            schemaView += field + name + type + '</div>';
        }

        schemaView += "</div>"
        return schemaView

    }

    // Clears output fields and renders error
    function createErrorOutput(err) {
        errorElm.contents().remove();
        outputElm.contents().remove();
        treeElm.contents().remove();
        errorElm.append(err);

    }

    // clears error and table fields and renders new table
    function createOutputTable(output) {
        outputElm.contents().remove();
        errorElm.contents().remove();

        var table = $("<table></table>"); // creates new table element to be filled
        table.append(createTableContent(output.getResult()._schema, output.getResult()._rows)); // creates table headers
        //table.append(createTableRows(output.getResult()._rows)); // fills table rows
        outputElm.append(table);
    }

    // Function that creates the table header
    function createTableContent(columnSchema, rows) {
        var header = $("<thead></thead>");
        var headerRow = $("<tr></tr>");
        var rowElements = [];
        var ifDateChecker = [];
        // reads each header
        for (var i = 0; i < columnSchema._names.length; i++) {
            var th = $("<th></th>").text(columnSchema._names[i]);
            if(columnSchema._types[i] == 'date')
                ifDateChecker.push(i);
            headerRow.append(th);
        }
        header.append(headerRow);
        rowElements.push(header);
        // reads each row in rows and adds them to the row element array.
        rows.forEach(function (row) {
            var tr = $("<tr></tr>");
            for (var i = 0; i < row.length; i++) {
                if(ifDateChecker.includes(i)) {
                    const date = new Date(row[i]);
                    const year = date.getFullYear();
                    const month = String(date.getMonth() + 1).padStart(2, '0');
                    const day = String(date.getDate()).padStart(2, '0');

                    var td = $("<td></td>").text(`${year}-${month}-${day}`);
                } else {
                    var td = $("<td></td>").text(row[i]);
                }

                tr.append(td);
            }
            rowElements.push(tr);
        });
        return rowElements;
    }

    //* Recursive function that creates the RelaX output Tree
    function createRecList(output){
        var container = $("<li></li>"); // Creates container holding section of tree
        var button = $("<div></div>"); // creates first node of this secton tree

        // fills node attributes
        button.attr("id", "button-"+output._functionName);
        button.attr("class", "node");
        var text = output._functionName
        if (text === '_inlineRelation8') {
            button.append(output._codeInfo.text); 
        } else {
            button.append(output.getFormulaHtml(false));
        }
        // allows each node to return the output at that point of execution 
        button.on("click", function() { createOutputTable(output); });
        
        // Checks to see if there are 2, 1, or no Children
        if ((output._child != null) && (output._child2 != null)) {
            container.append(button); // adds the main node
            // creates flex container.for children - allowing for side by side rendering
            var newUlDiv = $("<ul></ul>");
            var newLiDiv = $("<li></li>");

            // adds the child nodes

            newLiDiv.append(createRecList(output._child));
            newLiDiv.append(createRecList(output._child2));
            newUlDiv.append(newLiDiv);
            container.append(newUlDiv); // appends flex container to above container
            return container;
        } else if (output._child != null) { 
            var newUlDiv = $("<ul></ul>");
            var newLiDiv = $("<li></li>");
            
            container.append(button); // adds the main node.
            
            newLiDiv.append(createRecList(output._child)); // adds the child node
            newUlDiv.append(newLiDiv);
            container.append(newUlDiv);
            return container; 
        } else {
            return container.append(button); // adds the main node
        } 
    }
});


/**
 * 				<li>
					<div
						className={classNames({
							'node': true,
							'active': n === activeNode,
						})}
						onClick={() => setActiveNode && setActiveNode(n)}
					>
						<Popover
							title={<div>{fromVariableMarker}<div dangerouslySetInnerHTML={{ __html: n.getFormulaHtml(true, false) }}></div></div>}
							body={popoverBody}
							placement="right"
							trigger="hover"
						>

							<a className="formula">
								{fromVariableMarker}<span dangerouslySetInnerHTML={{ __html: n.getFormulaHtml(false, false) }} /><br/>
								<span className="resultCountLabel">{`${n.getResultNumRows()} row${n.getResultNumRows() === 1 ? '' : 's'}`}</span>
							</a>

						</Popover>
					</div>
					{child || child2
						? (
							<ul>
								{child}
								{child2}
							</ul>
						)
						: null
					}
				</li>
			);
		};
 */