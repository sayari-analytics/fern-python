# This file was auto-generated by Fern from our API Definition.

from ...core.exceptions.fern_http_exception import FernHTTPException
from ..types.unauthorized_request_error_body import UnauthorizedRequestErrorBody


class UnauthorizedRequest(FernHTTPException):
    def __init__(self, error: UnauthorizedRequestErrorBody):
        super().__init__(status_code=401, name="UnauthorizedRequest", content=error)
