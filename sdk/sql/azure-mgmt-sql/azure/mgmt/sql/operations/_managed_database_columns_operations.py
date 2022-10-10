# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, List, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_by_database_request(
    resource_group_name: str,
    managed_instance_name: str,
    database_name: str,
    subscription_id: str,
    *,
    schema: Optional[List[str]] = None,
    table: Optional[List[str]] = None,
    column: Optional[List[str]] = None,
    order_by: Optional[List[str]] = None,
    skiptoken: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-11-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/columns",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "managedInstanceName": _SERIALIZER.url("managed_instance_name", managed_instance_name, "str"),
        "databaseName": _SERIALIZER.url("database_name", database_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if schema is not None:
        _params["schema"] = [_SERIALIZER.query("schema", q, "str") if q is not None else "" for q in schema]
    if table is not None:
        _params["table"] = [_SERIALIZER.query("table", q, "str") if q is not None else "" for q in table]
    if column is not None:
        _params["column"] = [_SERIALIZER.query("column", q, "str") if q is not None else "" for q in column]
    if order_by is not None:
        _params["orderBy"] = [_SERIALIZER.query("order_by", q, "str") if q is not None else "" for q in order_by]
    if skiptoken is not None:
        _params["$skiptoken"] = _SERIALIZER.query("skiptoken", skiptoken, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_table_request(
    resource_group_name: str,
    managed_instance_name: str,
    database_name: str,
    schema_name: str,
    table_name: str,
    subscription_id: str,
    *,
    filter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-11-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/columns",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "managedInstanceName": _SERIALIZER.url("managed_instance_name", managed_instance_name, "str"),
        "databaseName": _SERIALIZER.url("database_name", database_name, "str"),
        "schemaName": _SERIALIZER.url("schema_name", schema_name, "str"),
        "tableName": _SERIALIZER.url("table_name", table_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str,
    managed_instance_name: str,
    database_name: str,
    schema_name: str,
    table_name: str,
    column_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-11-01-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/columns/{columnName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "managedInstanceName": _SERIALIZER.url("managed_instance_name", managed_instance_name, "str"),
        "databaseName": _SERIALIZER.url("database_name", database_name, "str"),
        "schemaName": _SERIALIZER.url("schema_name", schema_name, "str"),
        "tableName": _SERIALIZER.url("table_name", table_name, "str"),
        "columnName": _SERIALIZER.url("column_name", column_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class ManagedDatabaseColumnsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.sql.SqlManagementClient`'s
        :attr:`managed_database_columns` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_database(
        self,
        resource_group_name: str,
        managed_instance_name: str,
        database_name: str,
        schema: Optional[List[str]] = None,
        table: Optional[List[str]] = None,
        column: Optional[List[str]] = None,
        order_by: Optional[List[str]] = None,
        skiptoken: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.DatabaseColumn"]:
        """List managed database columns.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param managed_instance_name: The name of the managed instance. Required.
        :type managed_instance_name: str
        :param database_name: The name of the database. Required.
        :type database_name: str
        :param schema: Default value is None.
        :type schema: list[str]
        :param table: Default value is None.
        :type table: list[str]
        :param column: Default value is None.
        :type column: list[str]
        :param order_by: Default value is None.
        :type order_by: list[str]
        :param skiptoken: An opaque token that identifies a starting point in the collection. Default
         value is None.
        :type skiptoken: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DatabaseColumn or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.sql.models.DatabaseColumn]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-11-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.DatabaseColumnListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_database_request(
                    resource_group_name=resource_group_name,
                    managed_instance_name=managed_instance_name,
                    database_name=database_name,
                    subscription_id=self._config.subscription_id,
                    schema=schema,
                    table=table,
                    column=column,
                    order_by=order_by,
                    skiptoken=skiptoken,
                    api_version=api_version,
                    template_url=self.list_by_database.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("DatabaseColumnListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_database.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/columns"}  # type: ignore

    @distributed_trace
    def list_by_table(
        self,
        resource_group_name: str,
        managed_instance_name: str,
        database_name: str,
        schema_name: str,
        table_name: str,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.DatabaseColumn"]:
        """List managed database columns.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param managed_instance_name: The name of the managed instance. Required.
        :type managed_instance_name: str
        :param database_name: The name of the database. Required.
        :type database_name: str
        :param schema_name: The name of the schema. Required.
        :type schema_name: str
        :param table_name: The name of the table. Required.
        :type table_name: str
        :param filter: An OData filter expression that filters elements in the collection. Default
         value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DatabaseColumn or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.sql.models.DatabaseColumn]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-11-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.DatabaseColumnListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_table_request(
                    resource_group_name=resource_group_name,
                    managed_instance_name=managed_instance_name,
                    database_name=database_name,
                    schema_name=schema_name,
                    table_name=table_name,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    api_version=api_version,
                    template_url=self.list_by_table.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("DatabaseColumnListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_table.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/columns"}  # type: ignore

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        managed_instance_name: str,
        database_name: str,
        schema_name: str,
        table_name: str,
        column_name: str,
        **kwargs: Any
    ) -> _models.DatabaseColumn:
        """Get managed database column.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param managed_instance_name: The name of the managed instance. Required.
        :type managed_instance_name: str
        :param database_name: The name of the database. Required.
        :type database_name: str
        :param schema_name: The name of the schema. Required.
        :type schema_name: str
        :param table_name: The name of the table. Required.
        :type table_name: str
        :param column_name: The name of the column. Required.
        :type column_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DatabaseColumn or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.DatabaseColumn
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-11-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.DatabaseColumn]

        request = build_get_request(
            resource_group_name=resource_group_name,
            managed_instance_name=managed_instance_name,
            database_name=database_name,
            schema_name=schema_name,
            table_name=table_name,
            column_name=column_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("DatabaseColumn", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/columns/{columnName}"}  # type: ignore
