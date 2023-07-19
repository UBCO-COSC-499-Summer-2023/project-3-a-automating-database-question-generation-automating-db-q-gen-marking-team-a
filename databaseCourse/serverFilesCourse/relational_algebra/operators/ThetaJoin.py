from __future__ import annotations

import sqlite3
from typing import Optional

from typeguard import typechecked

import relational_algebra as ra


class ThetaJoin(ra.Operator):
    """
    This class represents a theta join in relational algebra
    """

    @typechecked
    def __init__(
        self,
        left_child: ra.Operator | str,
        right_child: ra.Operator | str,
        formula: ra.Formula,
    ) -> None:
        if isinstance(left_child, str):
            left_child = ra.Relation(left_child)
        if isinstance(right_child, str):
            right_child = ra.Relation(right_child)
        super().__init__(children=[left_child, right_child])
        self.formula = formula

    @typechecked
    def __repr__(self) -> str:
        return f"({self.children[0]} \\bowtie_{{{self.formula}}} {self.children[1]})"

    @typechecked
    def evaluate(self, sql_con: Optional[sqlite3.Connection] = None) -> ra.Relation:
        left_relation = self.children[0].evaluate(sql_con)
        right_relation = self.children[1].evaluate(sql_con)
        return ra.Selection(
            ra.CrossProduct(left_relation, right_relation), self.formula
        ).evaluate()
