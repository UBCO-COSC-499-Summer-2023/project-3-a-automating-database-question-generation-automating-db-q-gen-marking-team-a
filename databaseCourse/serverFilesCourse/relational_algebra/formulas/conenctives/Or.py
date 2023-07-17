from __future__ import annotations

from typeguard import typechecked
import pandas as pd

import relational_algebra as ra


class Or(ra.Formula):
    """
    This class represents a disjunction
    """

    @typechecked
    def __init__(self, left_child: ra.Formula, right_child: ra.Formula) -> None:
        super().__init__(children=[left_child, right_child])

    @typechecked
    def __repr__(self) -> str:
        left = self.children[0]
        right = self.children[1]

        if isinstance(self.children[0], Or):
            left = (
                f"{self.children[0].children[0]} \\land {self.children[0].children[1]}"
            )
        elif not isinstance(self.children[0], ra.Not | ra.ATOM_TYPES):
            left = f"({left})"

        if isinstance(self.children[1], Or):
            right = (
                f"{self.children[1].children[0]} \\land {self.children[1].children[1]}"
            )
        elif not isinstance(self.children[1], ra.Not | ra.ATOM_TYPES):
            right = f"({right})"

        return f"{left} \\lor {right}"

    @typechecked
    def to_series(self, relation: ra.Relation) -> pd.Series:
        return self.children[0].to_series(relation) | self.children[1].to_series(
            relation
        )
