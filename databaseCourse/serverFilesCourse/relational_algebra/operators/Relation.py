from __future__ import annotations

import sqlite3
import pandas as pd
import numpy as np
from typing import Iterable, Optional

from typeguard import typechecked

import relational_algebra as ra


class Relation(ra.Operator):
    """
    This class represents a relation in relational algebra
    """

    @typechecked
    def __init__(self, name: str) -> None:
        """
        Parameters
        ----------
        name : str
            The name of the relation
        """
        super().__init__(children=[])
        self.name = name
        self.dataframe = pd.DataFrame()
        self.was_evaluated = False

    @typechecked
    def __repr__(self) -> str:
        return f"(\\text{{{self.name}}})"

    @typechecked
    def tabulate(self) -> str:
        """
        Return the relation as a Markdown table

        Returns
        -------
        str
            The relation as a Markdown table
        """
        table = ""
        table += (
            "| "
            + " | ".join(self.get_minimal_attribute_names(self.attributes))
            + " |\n"
        )
        table += "| " + " | ".join(["---"] * len(self.attributes)) + " |\n"
        for row in self.dataframe.itertuples(index=False):
            table += "| " + " | ".join([str(x) for x in row]) + " |\n"
        return table

    @typechecked
    def evaluate(self, sql_con: Optional[sqlite3.Connection] = None) -> Relation:
        if sql_con is None:
            self.was_evaluated = True
            return self

        if self.was_evaluated:
            return self

        # get the attributes
        cursor = sql_con.cursor()
        cursor.execute(f"PRAGMA table_info({self.name})")
        self.add_attributes([row[1] for row in cursor.fetchall()], add_name=True)
        # get the rows
        cursor.execute(f"SELECT * FROM {self.name}")
        self.add_rows(cursor.fetchall())
        self.was_evaluated = True
        return self

    @typechecked
    def add_attribute(self, attribute: str, add_name: bool = True) -> None:
        """
        Add an attribute to the relation

        Parameters
        ----------
        attribute : str
            The attribute to add
        add_name : bool
            Whether to add the name of the relation to the attribute
        """
        assert len(self.rows) == 0
        if add_name:
            if "." not in attribute:
                attribute = f"{self.name}.{attribute}"
            else:
                attribute = f"{self.name}+{attribute}"
        self.dataframe[attribute] = pd.Series(dtype=object)
        self.was_evaluated = True

    @typechecked
    def add_attributes(self, attributes: Iterable[str], add_name: bool = True) -> None:
        """
        Add attributes to the relation

        Parameters
        ----------
        attributes : Iterable[str]
            The attributes to add
        add_name : bool
            Whether to add the name of the relation to the attributes
        """
        for attribute in attributes:
            self.add_attribute(attribute, add_name=add_name)

    @typechecked
    def add_row(
        self, row: tuple[ra.PRIMITIVE_TYPES, ...] | list[ra.PRIMITIVE_TYPES]
    ) -> None:
        """
        Adds a row to the relation

        Parameters
        ----------
        row : tuple[ra.PRIMITIVE_TYPES, ...] | list[ra.PRIMITIVE_TYPES]
            The row to add to the relation
        """
        row = list(row)
        if len(list(self.dataframe.columns)) != len(row):
            raise Exception(
                f"Row ({row}) does not have the same number of attributes ({list(self.dataframe.columns)}) as the relation {self.name}"
            )
        self.dataframe = (
            pd.concat(
                [pd.DataFrame([row], columns=self.dataframe.columns), self.dataframe]
            )
            .drop_duplicates(inplace=False)
            .replace({np.nan: None})
        )
        self.was_evaluated = True

    @typechecked
    def add_rows(
        self,
        rows: list[tuple[ra.PRIMITIVE_TYPES, ...]]
        | set[tuple[ra.PRIMITIVE_TYPES, ...]]
        | list[list[ra.PRIMITIVE_TYPES]],
    ) -> None:
        """
        Adds multiple rows to the relation

        Parameters
        ----------
        rows : list[tuple[ra.PRIMITIVE_TYPES, ...]] | set[tuple[ra.PRIMITIVE_TYPES, ...]] | list[list[ra.PRIMITIVE_TYPES]]
            The rows to add to the relation
        """
        # for row in rows:
        #    if len(list(self.dataframe.columns)) != len(row):
        #        raise Exception(
        #            f"Row ({row}) does not have the same number of attributes ({list(self.dataframe.columns)}) as the relation {self.name}"
        #        )

        self.dataframe = (
            pd.concat(
                [pd.DataFrame(rows, columns=self.dataframe.columns), self.dataframe]
            )
            .drop_duplicates(inplace=False)
            .replace({np.nan: None})
        )

    @typechecked
    def get_attribute_name(self, attribute: str) -> Optional[str]:
        """
        Returns the name of the attribute

        Parameters
        ----------
        attribute : str
            The attribute

        Returns
        -------
        Optional[str]
            The name of the attribute
        """
        candidates = list()
        if "." not in attribute:
            for attr in list(self.dataframe.columns):
                if attr.split(".")[-1].lower() == attribute.lower():
                    candidates.append(attr)
        else:
            na, at = attribute.split(".")
            for attr in list(self.dataframe.columns):
                names, a = attr.split(".")
                any = False
                for n in names.split("+"):
                    for nn in na.split("+"):
                        if n.lower() == nn.lower() and a.lower() == at.lower():
                            any = True
                if any:
                    candidates.append(attr)

        if len(candidates) == 0:
            return None
        if len(candidates) > 1:
            raise Exception(
                f"Multiple candidates for attribute {attribute}: {candidates}"
            )
        return candidates[0]

    @typechecked
    def get_attribute_names(
        self, attributes: list[str] | tuple[str, ...]
    ) -> Optional[list[str]]:
        """
        Returns the names of the attributes

        Parameters
        ----------
        attributes : list[str] | tuple[str, ...]
            The attributes

        Returns
        -------
        Optional[list[str]]
            The names of the attributes
        """
        result = [self.get_attribute_name(attribute) for attribute in attributes]
        if None in result:
            return None
        return result

    @typechecked
    def get_minimal_attribute_name(self, attribute: str) -> Optional[str]:
        """
        Returns the minimal attribute name (i.e. the attribute name without the relation name)

        Parameters
        ----------
        attribute : str
            The attribute name

        Returns
        -------
        Optional[str]
            The minimal attribute name
        """
        result = self.get_attribute_name(attribute)
        if result is None:
            return None
        if "." in result:
            return result.split(".")[-1]
        return result

    @typechecked
    def get_minimal_attribute_names(
        self, attributes: list[str] | tuple[str, ...]
    ) -> Optional[list[str]]:
        """
        Returns the minimal attribute names (i.e. the attribute names without the relation names)

        Parameters
        ----------
        attributes : list[str] | tuple[str, ...]
            The attribute names

        Returns
        -------
        Optional[list[str]]
            The minimal attribute names
        """
        result = [
            self.get_minimal_attribute_name(attribute) for attribute in attributes
        ]
        if None in result:
            return None
        return result

    @typechecked
    def __getitem__(self, attributes: str | tuple[str, ...] | list[str]) -> Relation:
        """
        Returns a projection of the relation

        Parameters
        ----------
        attributes : str | tuple[str, ...] | list[str]
            The attributes to project

        Returns
        -------
        Relation
            The projection of the relation
        """
        if isinstance(attributes, str):
            attr = list()
            attr.append(attributes)
            attributes = attr
        if isinstance(attributes, tuple):
            attributes = list(attributes)

        attribute_names = self.get_attribute_names(attributes)
        if attribute_names is None:
            raise KeyError(f"Attribute not found in: {attributes}")

        # create new relation using the same name and values of given attributes only
        new_relation = Relation(self.name)
        new_relation.was_evaluated = True
        new_relation.dataframe = self.dataframe[attribute_names].copy()
        # drop duplicates
        new_relation.dataframe.drop_duplicates(inplace=True)
        return new_relation

    @typechecked
    def union_compatibility(self, other: Relation) -> Optional[list[str]]:
        """
        Checks if two relations are compatible for a union operation.
        If so, the names of the attributes are returned.

        Parameters
        ----------
        other : Relation
            The other relation

        Returns
        -------
        Optional[str]
            The names of the attributes
        """
        if len(list(self.dataframe.columns)) != len(list(other.dataframe.columns)):
            return None
        for attr1, attr2 in zip(
            list(self.dataframe.columns), list(other.dataframe.columns)
        ):
            attr1_minimal = self.get_minimal_attribute_name(attr1)
            attr2_minimal = other.get_minimal_attribute_name(attr2)
            if attr1_minimal != attr2_minimal or attr1 is None or attr2 is None:
                return None
        return self.get_minimal_attribute_names(list(self.dataframe.columns))

    @property
    def attributes(self) -> list[str]:
        return list(self.dataframe.columns)

    @property
    def rows(self) -> set[tuple[ra.PRIMITIVE_TYPES, ...]]:
        return set(map(tuple, self.dataframe.values.tolist()))
