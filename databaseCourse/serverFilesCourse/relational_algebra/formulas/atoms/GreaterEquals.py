from __future__ import annotations

from typeguard import typechecked
import pandas as pd

import relational_algebra as ra


class GreaterEquals(ra.Formula):
    """
    This class represents a the comparison '>='
    """

    @typechecked
    def __init__(self, left: ra.PRIMITIVE_TYPES, right: ra.PRIMITIVE_TYPES) -> None:
        super().__init__(children=[])
        self.left = left
        self.right = right
        if not (isinstance(left, str) or isinstance(right, str)):
            raise ValueError(
                "At least one of the arguments must be a string referring to an attribute"
            )

    @typechecked
    def __repr__(self) -> str:
        return f"{self.left} \\geq {self.right}"

    @typechecked
    def to_series(self, relation: ra.Relation) -> pd.Series:
        left_is_attr = False
        left_value = self.left
        if isinstance(self.left, str):
            # check if left is an attribute
            left_attr = relation.get_attribute_name(self.left)
            if left_attr is not None:
                left_is_attr = True
                left_value = relation.dataframe[left_attr]

        right_is_attr = False
        right_value = self.right
        if isinstance(self.right, str):
            # check if right is an attribute
            right_attr = relation.get_attribute_name(self.right)
            if right_attr is not None:
                right_is_attr = True
                right_value = relation.dataframe[right_attr]

        if not left_is_attr and not right_is_attr:
            raise ValueError(
                "At least one of the arguments must be a string referring to an attribute"
            )

        return left_value >= right_value
