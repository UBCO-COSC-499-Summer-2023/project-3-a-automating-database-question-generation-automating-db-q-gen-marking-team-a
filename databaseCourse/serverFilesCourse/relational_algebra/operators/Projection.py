from __future__ import annotations

import sqlite3
from typing import Optional

from typeguard import typechecked

import relational_algebra as ra


class Projection(ra.Operator):
    """
    This class represents a projection in relational algebra
    """

    @typechecked
    def __init__(
        self, child: ra.Operator | str, attributes: str | tuple[str, ...] | list[str]
    ) -> None:
        if isinstance(child, str):
            child = ra.Relation(child)
        super().__init__(children=[child])
        if isinstance(attributes, str):
            attr = list()
            attr.append(attributes)
            attributes = attr
        self.attributes = attributes

    @typechecked
    def __repr__(self) -> str:
        return f"\\pi_{{{','.join(self.attributes)}}}({self.children[0]})"

    @typechecked
    def evaluate(self, sql_con: Optional[sqlite3.Connection] = None) -> ra.Relation:
        child_relation = self.children[0].evaluate(sql_con)
        return child_relation[tuple(self.attributes)]
