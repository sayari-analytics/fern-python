# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .options import Options as literal_types_options_Options

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def ok(self, value: typing_extensions.Literal[True]) -> CreateOptionsResponse:
        return CreateOptionsResponse(__root__=_CreateOptionsResponse.Ok(type="ok", value=value))

    def options(self, value: literal_types_options_Options) -> CreateOptionsResponse:
        return CreateOptionsResponse(
            __root__=_CreateOptionsResponse.Options(**value.dict(exclude_unset=True), type="options")
        )


class CreateOptionsResponse(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_CreateOptionsResponse.Ok, _CreateOptionsResponse.Options]:
        return self.__root__

    def visit(
        self,
        ok: typing.Callable[[typing_extensions.Literal[True]], T_Result],
        options: typing.Callable[[literal_types_options_Options], T_Result],
    ) -> T_Result:
        if self.__root__.type == "ok":
            return ok(self.__root__.value)
        if self.__root__.type == "options":
            return options(literal_types_options_Options(**self.__root__.dict(exclude_unset=True, exclude={"type"})))

    __root__: typing_extensions.Annotated[
        typing.Union[_CreateOptionsResponse.Ok, _CreateOptionsResponse.Options], pydantic.Field(discriminator="type")
    ]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _CreateOptionsResponse:
    class Ok(pydantic.BaseModel):
        type: typing_extensions.Literal["ok"]
        value: typing_extensions.Literal[True]

    class Options(literal_types_options_Options):
        type: typing_extensions.Literal["options"]

        class Config:
            allow_population_by_field_name = True


CreateOptionsResponse.update_forward_refs()
