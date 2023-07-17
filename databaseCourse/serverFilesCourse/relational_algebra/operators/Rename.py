from __future__ import annotations

import sqlite3
from typing import Optional

from typeguard import typechecked

import relational_algebra as ra


class Rename(ra.Operator):
    """
    This class represents a rename in relational algebra
    """

    @typechecked
    def __init__(self, child: ra.Operator | str, mapping: dict[str, str] | str) -> None:
        if isinstance(child, str):
            child = ra.Relation(child)
        super().__init__(children=[child])
        self.mapping = mapping

    @typechecked
    def __repr__(self) -> str:
        if isinstance(self.mapping, str):
            return f"\\rho_{{{self.mapping}}}({self.children[0]})"
        else:
            # there cannot be \ in f-string in f-string (says formatter)
            tmp = [f"{v} \\leftarrow {k}" for k, v in self.mapping.items()]
            return f"\\rho_{{{','.join(tmp)}}}({self.children[0]})"

    @typechecked
    def evaluate(self, sql_con: Optional[sqlite3.Connection] = None) -> ra.Relation:
        relation = self.children[0].evaluate(sql_con)

        new_relation = None
        attribute_mapping = dict()

        # create the new attribute mapping
        if isinstance(self.mapping, str):
            # rename the relation
            new_relation = ra.Relation(self.mapping)
            relation_attribute_names = relation.get_attribute_names(relation.attributes)
            assert relation_attribute_names is not None
            for attribute in relation_attribute_names:
                names, attr = attribute.split(".")
                old_names = list()
                for name in names.split("+"):
                    if name != relation.name:
                        old_names.append(name)

                if len(old_names) == 0:
                    new_attribute = f"{new_relation.name}.{attr}"
                else:
                    old_names.append(new_relation.name)
                    new_attribute = f"{'+'.join(old_names)}.{attr}"
                attribute_mapping[attribute] = new_attribute
        else:
            # rename the attributes
            new_relation = ra.Relation(relation.name)
            new_mapping = {}
            for key, value in self.mapping.items():
                # check if key is attribute in the relation
                key = relation.get_attribute_name(key)
                if key is None:
                    raise KeyError(
                        f"The attribute {key} is not in the relation {relation.name}"
                    )
                # check if value is not already an attribute in the relation
                v = relation.get_attribute_name(value)
                if v is not None:
                    raise ValueError(
                        f"The attribute {value} is already in the relation {relation.name}"
                    )
                # check if key is not already in the mapping
                if key in new_mapping.keys():
                    raise KeyError(f"The attribute {key} is already in the mapping")
                # check if value is not already in the mapping
                if value in new_mapping.values():
                    raise ValueError(f"The attribute {value} is already in the mapping")
                # rename the attribute
                new_mapping[key] = f"{new_relation.name}.{value}"
            relation_attribute_names = relation.get_attribute_names(relation.attributes)
            assert relation_attribute_names is not None
            for attribute in relation_attribute_names:
                if attribute in new_mapping.keys():
                    new_attribute = new_mapping[attribute]
                else:
                    new_attribute = attribute
                attribute_mapping[attribute] = new_attribute

        new_relation.was_evaluated = True

        # create the new relation
        new_relation.add_attributes(attribute_mapping.values())

        # add rows
        new_relation.dataframe = relation.dataframe.copy().rename(
            columns=attribute_mapping
        )

        # drop duplicates
        new_relation.dataframe.drop_duplicates(inplace=True)
        return new_relation
