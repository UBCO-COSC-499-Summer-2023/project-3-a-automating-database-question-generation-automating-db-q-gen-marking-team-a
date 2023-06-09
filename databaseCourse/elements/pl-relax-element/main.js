
    //QUESTION SETUP
    // var relaxInput = document.getElementById("relax_input")
    // console.log(relaxInput)
    //const relalg_bundle = require("relalg_bundle.js");

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
    console.log("nerd");
    console.log(Q.getResult());

