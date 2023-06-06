const relalg_bundle = require("./relalg_bundle");

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

const Q = executeRelalg(`pi b,d (S)`, {"S": S});

console.log(Q.getResult());