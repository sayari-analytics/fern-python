# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime


class Node(pydantic.BaseModel):
    """
    from seed import Node, Tree

    Node(
        name="root",
        nodes=[Node(name="left"), Node(name="right")],
        trees=[Tree(nodes=[Node(name="left"), Node(name="right")])],
    )
    """

    name: str
    nodes: typing.Optional[typing.List[Node]]
    trees: typing.Optional[typing.List[Tree]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}


from .tree import Tree  # noqa: E402

Node.update_forward_refs()
