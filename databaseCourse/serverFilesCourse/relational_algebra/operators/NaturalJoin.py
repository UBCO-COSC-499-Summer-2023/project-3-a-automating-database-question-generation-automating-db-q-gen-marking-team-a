from __future__ import annotations

import sqlite3
from typing import Optional

from typeguard import typechecked

import relational_algebra as ra


class NaturalJoin(ra.Operator):
    """
    This class represents a natural join in relational algebra
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
        return f"({self.children[0]} \\bowtie {self.children[1]})"

    @typechecked
    def evaluate(self, sql_con: Optional[sqlite3.Connection] = None) -> ra.Relation:
        left_relation = self.children[0].evaluate(sql_con)
        right_relation = self.children[1].evaluate(sql_con)
        # determine attribute names
        left_attributes = left_relation.get_minimal_attribute_names(
            left_relation.attributes
        )
        right_attributes = right_relation.get_minimal_attribute_names(
            right_relation.attributes
        )
        # check if attributes are not null
        assert left_attributes is not None
        assert right_attributes is not None
        # determine new attribute names and name mapping
        left_attribute_mapping = dict()
        right_attribute_mapping = dict()
        common_attributes = list()
        for attribute in left_attributes:
            new_attribute = f"{left_relation.name}+{right_relation.name}.{attribute}"
            left_attribute_mapping[
                left_relation.get_attribute_name(attribute)
            ] = new_attribute
        for attribute in right_attributes:
            new_attribute = f"{left_relation.name}+{right_relation.name}.{attribute}"
            right_attribute_mapping[
                right_relation.get_attribute_name(attribute)
            ] = new_attribute
            if new_attribute in left_attribute_mapping.values():
                common_attributes.append(new_attribute)

        # create new relation
        new_relation = ra.Relation(f"{left_relation.name}+{right_relation.name}")
        new_relation.was_evaluated = True
        # add rows
        left_dataframe = left_relation.dataframe.copy().rename(
            columns=left_attribute_mapping
        )
        right_dataframe = right_relation.dataframe.copy().rename(
            columns=right_attribute_mapping
        )
        if len(common_attributes) == 0:
            new_relation.dataframe = left_dataframe.merge(right_dataframe, how="cross")
        else:
            new_relation.dataframe = left_dataframe.merge(
                right_dataframe, how="inner", on=common_attributes
            )
        # drop duplicates
        new_relation.dataframe.drop_duplicates(inplace=True)
        return new_relation
