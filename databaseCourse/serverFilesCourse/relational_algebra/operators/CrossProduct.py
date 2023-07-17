from __future__ import annotations

import sqlite3
from typing import Optional

from typeguard import typechecked

import relational_algebra as ra


class CrossProduct(ra.Operator):
    """
    This class represents a cross product in relational algebra
    """

    @typechecked
    def __init__(
        self, left_child: ra.Operator | str, right_child: ra.Operator | str
    ) -> None:
        if isinstance(left_child, str):
            left_child = ra.Relation(left_child)
        if isinstance(right_child, str):
            right_child = ra.Relation(right_child)
        super().__init__(children=[left_child, right_child])

    @typechecked
    def __repr__(self) -> str:
        return f"({self.children[0]} \\times {self.children[1]})"

    @typechecked
    def evaluate(self, sql_con: Optional[sqlite3.Connection] = None) -> ra.Relation:
        left_relation = self.children[0].evaluate(sql_con)
        right_relation = self.children[1].evaluate(sql_con)

        # create the new relation
        new_relation = ra.Relation(f"{left_relation.name}+{right_relation.name}")
        new_relation.was_evaluated = True
        # add the rows
        new_relation.dataframe = left_relation.dataframe.copy().merge(
            right_relation.dataframe.copy(), how="cross"
        )
        # drop duplicates
        new_relation.dataframe.drop_duplicates(inplace=True)
        return new_relation
