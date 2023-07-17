from __future__ import annotations

from typeguard import typechecked
import pandas as pd

import relational_algebra as ra


class Not(ra.Formula):
    """
    This class represents a negation
    """

    @typechecked
    def __init__(self, child: ra.Formula) -> None:
        super().__init__(children=[child])

    @typechecked
    def __repr__(self) -> str:
        if isinstance(self.children[0], ra.And | ra.Or):
            return f"\\neg({self.children[0]})"
        return f"\\neg {self.children[0]}"

    @typechecked
    def to_series(self, relation: ra.Relation) -> pd.Series:
        return ~self.children[0].to_series(relation)
