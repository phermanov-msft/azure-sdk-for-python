# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, cast, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._diagnostics_operations import build_create_request, build_get_request

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class DiagnosticsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.selfhelp.aio.SelfHelpMgmtClient`'s
        :attr:`diagnostics` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def _create_initial(
        self,
        scope: str,
        diagnostics_resource_name: str,
        diagnostic_resource_request: Optional[Union[_models.DiagnosticResource, IO[bytes]]] = None,
        **kwargs: Any
    ) -> _models.DiagnosticResource:
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DiagnosticResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(diagnostic_resource_request, (IOBase, bytes)):
            _content = diagnostic_resource_request
        else:
            if diagnostic_resource_request is not None:
                _json = self._serialize.body(diagnostic_resource_request, "DiagnosticResource")
            else:
                _json = None

        _request = build_create_request(
            scope=scope,
            diagnostics_resource_name=diagnostics_resource_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("DiagnosticResource", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("DiagnosticResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_create(
        self,
        scope: str,
        diagnostics_resource_name: str,
        diagnostic_resource_request: Optional[_models.DiagnosticResource] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.DiagnosticResource]:
        """Creates a diagnostic for the specific resource using solutionId from discovery solutions.
        :code:`<br/>`Diagnostics are powerful solutions that access product resources or other relevant
        data and provide the root cause of the issue and the steps to address the
        issue.:code:`<br/>`:code:`<br/>`.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param diagnostics_resource_name: Unique resource name for insight resources. Required.
        :type diagnostics_resource_name: str
        :param diagnostic_resource_request: The required request body for this insightResource
         invocation. Default value is None.
        :type diagnostic_resource_request: ~azure.mgmt.selfhelp.models.DiagnosticResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either DiagnosticResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.selfhelp.models.DiagnosticResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create(
        self,
        scope: str,
        diagnostics_resource_name: str,
        diagnostic_resource_request: Optional[IO[bytes]] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.DiagnosticResource]:
        """Creates a diagnostic for the specific resource using solutionId from discovery solutions.
        :code:`<br/>`Diagnostics are powerful solutions that access product resources or other relevant
        data and provide the root cause of the issue and the steps to address the
        issue.:code:`<br/>`:code:`<br/>`.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param diagnostics_resource_name: Unique resource name for insight resources. Required.
        :type diagnostics_resource_name: str
        :param diagnostic_resource_request: The required request body for this insightResource
         invocation. Default value is None.
        :type diagnostic_resource_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either DiagnosticResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.selfhelp.models.DiagnosticResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create(
        self,
        scope: str,
        diagnostics_resource_name: str,
        diagnostic_resource_request: Optional[Union[_models.DiagnosticResource, IO[bytes]]] = None,
        **kwargs: Any
    ) -> AsyncLROPoller[_models.DiagnosticResource]:
        """Creates a diagnostic for the specific resource using solutionId from discovery solutions.
        :code:`<br/>`Diagnostics are powerful solutions that access product resources or other relevant
        data and provide the root cause of the issue and the steps to address the
        issue.:code:`<br/>`:code:`<br/>`.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param diagnostics_resource_name: Unique resource name for insight resources. Required.
        :type diagnostics_resource_name: str
        :param diagnostic_resource_request: The required request body for this insightResource
         invocation. Is either a DiagnosticResource type or a IO[bytes] type. Default value is None.
        :type diagnostic_resource_request: ~azure.mgmt.selfhelp.models.DiagnosticResource or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either DiagnosticResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.selfhelp.models.DiagnosticResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DiagnosticResource] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_initial(
                scope=scope,
                diagnostics_resource_name=diagnostics_resource_name,
                diagnostic_resource_request=diagnostic_resource_request,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("DiagnosticResource", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.DiagnosticResource].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.DiagnosticResource](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    @distributed_trace_async
    async def get(self, scope: str, diagnostics_resource_name: str, **kwargs: Any) -> _models.DiagnosticResource:
        """Get the diagnostics using the 'diagnosticsResourceName' you chose while creating the
        diagnostic.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param diagnostics_resource_name: Unique resource name for insight resources. Required.
        :type diagnostics_resource_name: str
        :return: DiagnosticResource or the result of cls(response)
        :rtype: ~azure.mgmt.selfhelp.models.DiagnosticResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.DiagnosticResource] = kwargs.pop("cls", None)

        _request = build_get_request(
            scope=scope,
            diagnostics_resource_name=diagnostics_resource_name,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("DiagnosticResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
