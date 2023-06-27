$(document).ready(function () {
    //* QUESTION SETUP
    const executeRelalg = relalg_bundle.executeRelalg;
    const Relation = relalg_bundle.Relation;
    // find all relations used in this branch (recursively)
    const dbSchema = document.getElementById("database");

    const dbValue = dbSchema.getAttribute("value");
    const dbArray = dbValue.split(";");
    // database setup
    const dataset = [dbArray.length];
    for (var i = 0; i < dbArray.length; i++){   
        dataset[i] = executeRelalg(dbArray.at(i), {});
    }
    // const S = executeRelalg(dbArray.at(0), {});
    // const P = executeRelalg(dbArray.at(1), {});
    
    // const collection = document.getElementsByClassName("card-body submission-body");
    // collection.item(0).append("Hello")
    
    //for(elem in dataset) {

    //}
    //renderDatasSet()



    
    console.log(dataset.length)
    for(var i = 0; i < dataset.length; i++) {
        dbSchema.innerHTML += createSchemaTables(dataset.at(i)._schema)
    }

    

    function createSchemaTables(dataSchema) {
        // if tables have no rows, means table does not exist
        if (dataSchema.length === 0) {
            return;
        }
        let schemaView = "<button type='button' onmouseover='openMenu(this)' onClick='updateCodeMirror(\""+dataSchema._relAliases[0]+"\");' class='dropbtn' id='btn-" + dataSchema._relAliases[0] + "'>" + dataSchema._relAliases[0]
            + "</button> <div class='dropdown-content' id='schema-" + dataSchema._relAliases[0] + "'>"

        for (var i = 0; i < dataSchema._names.length; i++) {
            let field = "<div classname='submenu' onClick='updateCodeMirror(\""+dataSchema._names[i]+"\");' id='schema-" + dataSchema._relAliases[0] + "'>" + dataSchema._names[i] +", " + dataSchema._types[i] + "</div>"
            console.log(i)
            schemaView += (field)
        }

        schemaView += "</div>"
        return schemaView

    }

    window.openMenu = function (val) {
        closeMenus();
        document.getElementById('schema-' + val.id.slice(4)).classList.toggle('show');
    }

    // function to close the modals of the schemas, basically hides each field in the modal
    function closeMenus() {
        let dropdowns = document.getElementsByClassName('dropdown-content');
        for (let i = 0; i < dropdowns.length; i++) {
            if (dropdowns[i].classList.contains('show')) {
                dropdowns[i].classList.remove('show')
            }
        }
    }
    window.onclick = function (e) {
        if (!e.target.matches('.dropbtn')) {
            closeMenus()
        }
    }
    // adds onclick functionality for the top bar of the relax editor
    document.getElementById("popWrapper_i4m1hevx8hm").onclick = function() { updateCodeMirror("π"); }
    document.getElementById("popWrapper_zk54ccpfgr9").onclick = function() { updateCodeMirror("σ"); }
    document.getElementById("popWrapper_opmskf8udx").onclick = function() { updateCodeMirror("ρ"); }
    document.getElementById("popWrapper_vqmsrbz4lhh").onclick = function() { updateCodeMirror("←"); }
    document.getElementById("popWrapper_r4e8qivo9x").onclick = function() { updateCodeMirror("→"); }
    document.getElementById("popWrapper_rm8nadc63ta").onclick = function() { updateCodeMirror("τ"); }
    document.getElementById("popWrapper_yelfh6roevh").onclick = function() { updateCodeMirror("γ"); }
    document.getElementById("popWrapper_lv4upm1exe").onclick = function() { updateCodeMirror("∧"); }
    document.getElementById("popWrapper_wihrg7pw86c").onclick = function() { updateCodeMirror("∨"); }
    document.getElementById("popWrapper_mx0q4np8lms").onclick = function() { updateCodeMirror("¬"); }
    document.getElementById("popWrapper_iwcqg10p7gn").onclick = function() { updateCodeMirror("="); }
    document.getElementById("popWrapper_qfox1fuq55").onclick = function() { updateCodeMirror("≠"); }
    document.getElementById("popWrapper_3ixqdjahm8v").onclick = function() { updateCodeMirror("≥"); }
    document.getElementById("popWrapper_tc2rsc59fbq").onclick = function() { updateCodeMirror("≤"); }
    document.getElementById("popWrapper_q8ve1atlpu").onclick = function() { updateCodeMirror("∩"); }
    document.getElementById("popWrapper_o60hh3goasp").onclick = function() { updateCodeMirror("∪"); }
    document.getElementById("popWrapper_ytckmx1p4tk").onclick = function() { updateCodeMirror("÷"); }
    document.getElementById("popWrapper_2131akj8rbn").onclick = function() { updateCodeMirror("-"); }
    document.getElementById("popWrapper_bcy1hzhtzbq").onclick = function() { updateCodeMirror("⨯"); }
    document.getElementById("popWrapper_jgzn81np8i").onclick = function() { updateCodeMirror("⨝"); }
    document.getElementById("popWrapper_99cz04sajcd").onclick = function() { updateCodeMirror("⟕"); }
    document.getElementById("popWrapper_wrwiiwklzc").onclick = function() { updateCodeMirror("⟖"); }
    document.getElementById("popWrapper_xzmnvtls6zk").onclick = function() { updateCodeMirror("⟗"); }
    document.getElementById("popWrapper_7lmq0e5lt2k").onclick = function() { updateCodeMirror("⋉"); }
    document.getElementById("popWrapper_h8t7el4tebi").onclick = function() { updateCodeMirror("⋊"); }
    document.getElementById("popWrapper_ntphproh2gh").onclick = function() { updateCodeMirror("▷"); }
    document.getElementById("popWrapper_aq5dkivxzhk").onclick = function() { updateCodeMirror("="); }
    document.getElementById("popWrapper_r2u4dj6ind").onclick = function() { updateCodeMirror("--"); }
    document.getElementById("popWrapper_2znla6h967q").onclick = function() { updateCodeMirror("/*"); }
    document.getElementById("popWrapper_2aod06t35hu").onclick = function() { updateCodeMirror("{}"); }
    document.getElementById("popWrapper_ieljbcakzad").onclick = function() { updateCodeMirror("Date()"); }

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
    window.updateCodeMirror = function (data) {
        updateCodeMirror(data);
    }
    // adds functionality for onclick
    function updateCodeMirror(data){
        var doc = editor.getDoc(); //gets the information of the editor
        doc.replaceRange(data, doc.getCursor()); // adds data at position of cursor
        editor.focus();
        editor.setCursor(doc.getCursor());
    }


    var treeElm = $("#tree");
    var outputElm = $("#output");
    var errorElm = $("#error");
    var execBtn = $("#execute");
    execBtn.on("click", executeEditorContents);

    // Execute the RelaX Query
    function executeEditorContents() {
        var d1 = dataset.at(0)._schema._relAliases.at(0);
        var d2 = dataset.at(1)._schema._relAliases.at(0);
        console.log(d1, d2);
        console.log(editor.getValue());
        try {
            const PR = executeRelalg(editor.getValue(), { "S" : dataset[0], "P" : dataset[1]});
            console.log(PR);
            treeElm.contents().remove();
            createOutputTable(PR);
            treeElm.append(createRecList(PR));
        } catch (err) {
            createErrorOutput(err)
        }
    }
    
    function createErrorOutput(err) {
        errorElm.contents().remove();
        outputElm.contents().remove();
        treeElm.contents().remove();
        errorElm.append(err);
        errorElm.append(err.stack);

    }

    function createOutputTable(output) {
        outputElm.contents().remove();
        errorElm.contents().remove();

        var table = $("<table></table>");
        table.append(createTableHeader(output.getResult()._schema._names));
        table.append(createTableRows(output.getResult()._rows));
        outputElm.append(table);
    }

    // Function that creates the table header

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

    function createRecList(output){
        console.log("hello")
        var container = $("<div style='margin: 5px'></div>");

        var button = $("<div></div>");
        button.attr("id", "button-"+output._functionName);
        button.addClass("btn btn-primary exec-button selection");
        button.text(output._codeInfo.text);
        button.on("click", function() {
            // Call the predefined function with the input parameter
            createOutputTable(output);
        });
        
        if ((output._child != null) && (output._child2 != null)) {
            container.append(button);
            
            var newContainer = $("<div></div>");
            newContainer.addClass("flex-container")

            newContainer.append(createRecList(output._child));
            newContainer.append(createRecList(output._child2));
            container.append(newContainer);
            return container;
        } else if (output._child != null) {
            container.append(button);
            container.append(createRecList(output._child));
            return container;
        } else {
            return container.append(button);
        } 
    }
});

/*
      let schemaView = "<button type='button' onClick='openMenu(this)' class='dropbtn' id='btn-" + dataSchema._relAliases[0] + "'>" + dataSchema._relAliases[0]
            + "</button> <div class='dropdown-content' id='schema-" + dataSchema._relAliases[0] + "'>"

        for (var i = 0; i < dataSchema._names.length; i++) {
            let field = "<div classname='submenu' id='schema-" + dataSchema._relAliases[0] + "'>" + dataSchema._names[i] +", " + dataSchema._types[i] + "</div>"
            console.log(i)
            schemaView += (field)
        }

        schemaView += "</div>"
        */