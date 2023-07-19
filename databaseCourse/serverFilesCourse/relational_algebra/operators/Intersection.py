from __future__ import annotations

import sqlite3
from typing import Optional

from typeguard import typechecked

import relational_algebra as ra


class Intersection(ra.Operator):
    """
    This class represents an intersection in relational algebra
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
        return f"({self.children[0]} \\cap {self.children[1]})"

    @typechecked
    def evaluate(self, sql_con: Optional[sqlite3.Connection] = None) -> ra.Relation:
        left_relation = self.children[0].evaluate(sql_con)
        right_relation = self.children[1].evaluate(sql_con)
        # check if union compatible
        attributes = left_relation.union_compatibility(right_relation)
        if attributes is None:
            raise ValueError(
                f"The relations {left_relation.name} and {right_relation.name} are not union compatible"
            )
        attributes = list(
            map(lambda attribute: f"{left_relation.name}.{attribute}", attributes)
        )
        # create the new relation
        new_relation = ra.Relation(left_relation.name)
        new_relation.was_evaluated = True
        left_dataframe = left_relation.dataframe.copy().rename(
            columns=dict(zip(left_relation.attributes, attributes))
        )
        right_dataframe = right_relation.dataframe.copy().rename(
            columns=dict(zip(right_relation.attributes, attributes))
        )
        # add the rows
        new_relation.dataframe = left_dataframe.merge(right_dataframe, how="inner")
        # drop duplicates
        new_relation.dataframe.drop_duplicates(inplace=True)
        return new_relation
