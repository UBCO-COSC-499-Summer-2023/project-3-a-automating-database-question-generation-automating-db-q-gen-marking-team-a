from __future__ import annotations

import sqlite3
from typing import Optional

from typeguard import typechecked

import relational_algebra as ra


class Selection(ra.Operator):
    """
    This class represents a select in relational algebra
    """

    @typechecked
    def __init__(self, child: ra.Operator | str, condition: ra.Formula) -> None:
        if isinstance(child, str):
            child = ra.Relation(child)
        super().__init__(children=[child])
        self.condition = condition

    @typechecked
    def __repr__(self) -> str:
        return f"\\sigma_{{{self.condition}}}({self.children[0]})"

    @typechecked
    def evaluate(self, sql_con: Optional[sqlite3.Connection] = None) -> ra.Relation:
        relation = self.children[0].evaluate(sql_con)
        # create the new relation
        return self.condition.selection(relation)
