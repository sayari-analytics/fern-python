# This file was auto-generated by Fern from our API Definition.

from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper


class CClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def foo(self) -> None:
        _response = self._client_wrapper.httpx_client.request(
            "POST", self._client_wrapper.get_base_url(), headers=self._client_wrapper.get_headers(), timeout=60
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncCClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def foo(self) -> None:
        _response = await self._client_wrapper.httpx_client.request(
            "POST", self._client_wrapper.get_base_url(), headers=self._client_wrapper.get_headers(), timeout=60
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
