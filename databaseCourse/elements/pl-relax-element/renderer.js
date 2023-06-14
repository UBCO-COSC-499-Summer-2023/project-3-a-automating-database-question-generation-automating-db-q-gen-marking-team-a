//const { update } = require("./relalg_bundle");

$(document).ready(function () {
    //QUESTION SETUP
    var relaxInput = document.getElementById("relax_input")
    // console.log(relaxInput)
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
    function panelPress(str) {
    }
    


    var editorInit = $("#RelaX-editor");

    var editor = CodeMirror.fromTextArea(editorInit[0], {
        mode: 'text/x-mysql',
        viewportMargin: Infinity,
        indentWithTabs: true,
        smartIndent: true,
        lineNumbers: true,
        matchBrackets: true,
        autofocus: true,
        extraKeys: {
            //"Ctrl-Enter": executeEditorContents,
        }
    });

    function updateCodeMirror(data){
        var doc = editor.getDoc();
        var cursor = doc.getCursor(); // gets the line number in the cursor position
        doc.replaceRange(data, cursor); // adds a new line
    }

    // Execute the sql code
    // Create table
    // TODO: Refactor all code that creates tables using sql.js API
    function execute(sqlCode) {

        outputElm.contents().remove();

        let results = db.exec(sqlCode);
        console.log(results)

        outputElm.append(createTable(results));

    }

    const executeRelalg = relalg_bundle.executeRelalg;
    const Relation = relalg_bundle.Relation;

    //console.log();

    const S = executeRelalg(`{
		S.b, S.d
		a,   100
		b,   300
		c,   400
		d,   200
		e,   150
	}`, {});

    const Q = executeRelalg(`π b,d (S)`, {"S": S});

    
});