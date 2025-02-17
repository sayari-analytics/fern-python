# This file was auto-generated by Fern from our API Definition.

from ...core.api_error import ApiError
from .nested_object_with_required_field import NestedObjectWithRequiredField


class NestedObjectWithRequiredFieldError(ApiError):
    def __init__(self, body: NestedObjectWithRequiredField):
        super().__init__(status_code=400, body=body)
