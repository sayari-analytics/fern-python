# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Enum(str, enum.Enum):
    """
    from seed import Enum

    Enum.THREE
    """

    ONE = "ONE"
    """
    The first enum value.
    """

    TWO = "TWO"
    THREE = "THREE"

    def visit(
        self,
        one: typing.Callable[[], T_Result],
        two: typing.Callable[[], T_Result],
        three: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Enum.ONE:
            return one()
        if self is Enum.TWO:
            return two()
        if self is Enum.THREE:
            return three()
