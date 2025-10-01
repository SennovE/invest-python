from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import List, Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest._grpc_helpers import message_field
from tinkoff.invest.grpc import users_pb2, users_pb2_grpc
from tinkoff.invest.grpc.common import MoneyValue, Quotation
from tinkoff.invest.logging import get_tracking_id_from_call, log_request


class UsersService(BaseService):
    """/*С помощью сервиса можно получить: <br/> 1.
                       список счетов пользователя; <br/> 2. маржинальные показатели по счeту.*/"""
    _protobuf = users_pb2
    _protobuf_grpc = users_pb2_grpc
    _protobuf_stub = _protobuf_grpc.UsersServiceStub

    def get_accounts(self, request: 'GetAccountsRequest'
        ) ->'GetAccountsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response, call = self._stub.GetAccounts.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetAccounts')
        return protobuf_to_dataclass(response, GetAccountsResponse)

    def get_margin_attributes(self, request: 'GetMarginAttributesRequest'
        ) ->'GetMarginAttributesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMarginAttributesRequest())
        response, call = self._stub.GetMarginAttributes.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetMarginAttributes')
        return protobuf_to_dataclass(response, GetMarginAttributesResponse)

    def get_user_tariff(self, request: 'GetUserTariffRequest'
        ) ->'GetUserTariffResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetUserTariffRequest())
        response, call = self._stub.GetUserTariff.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetUserTariff')
        return protobuf_to_dataclass(response, GetUserTariffResponse)

    def get_info(self, request: 'GetInfoRequest') ->'GetInfoResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetInfoRequest())
        response, call = self._stub.GetInfo.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetInfo')
        return protobuf_to_dataclass(response, GetInfoResponse)


@dataclass
class GetAccountsRequest:
    status: Optional['AccountStatus'] = message_field(1, optional=True)


@dataclass
class GetAccountsResponse:
    accounts: List['Account'] = message_field(1)


@dataclass
class Account:
    id: str = message_field(1)
    type: 'AccountType' = message_field(2)
    name: str = message_field(3)
    status: 'AccountStatus' = message_field(4)
    opened_date: datetime = message_field(5)
    closed_date: datetime = message_field(6)
    access_level: 'AccessLevel' = message_field(7)


class AccountType(IntEnum):
    ACCOUNT_TYPE_UNSPECIFIED = 0
    ACCOUNT_TYPE_TINKOFF = 1
    ACCOUNT_TYPE_TINKOFF_IIS = 2
    ACCOUNT_TYPE_INVEST_BOX = 3
    ACCOUNT_TYPE_INVEST_FUND = 4


class AccountStatus(IntEnum):
    ACCOUNT_STATUS_UNSPECIFIED = 0
    ACCOUNT_STATUS_NEW = 1
    ACCOUNT_STATUS_OPEN = 2
    ACCOUNT_STATUS_CLOSED = 3
    ACCOUNT_STATUS_ALL = 4


@dataclass
class GetMarginAttributesRequest:
    account_id: str = message_field(1)


@dataclass
class GetMarginAttributesResponse:
    liquid_portfolio: 'MoneyValue' = message_field(1)
    starting_margin: 'MoneyValue' = message_field(2)
    minimal_margin: 'MoneyValue' = message_field(3)
    funds_sufficiency_level: 'Quotation' = message_field(4)
    amount_of_missing_funds: 'MoneyValue' = message_field(5)
    corrected_margin: 'MoneyValue' = message_field(6)


@dataclass
class GetUserTariffRequest:
    pass


@dataclass
class GetUserTariffResponse:
    unary_limits: List['UnaryLimit'] = message_field(1)
    stream_limits: List['StreamLimit'] = message_field(2)


@dataclass
class UnaryLimit:
    limit_per_minute: int = message_field(1)
    methods: List[str] = message_field(2)


@dataclass
class StreamLimit:
    limit: int = message_field(1)
    streams: List[str] = message_field(2)
    open: int = message_field(3)


@dataclass
class GetInfoRequest:
    pass


@dataclass
class GetInfoResponse:
    prem_status: bool = message_field(1)
    qual_status: bool = message_field(2)
    qualified_for_work_with: List[str] = message_field(3)
    tariff: str = message_field(4)
    user_id: str = message_field(9)
    risk_level_code: str = message_field(12)


class AccessLevel(IntEnum):
    ACCOUNT_ACCESS_LEVEL_UNSPECIFIED = 0
    ACCOUNT_ACCESS_LEVEL_FULL_ACCESS = 1
    ACCOUNT_ACCESS_LEVEL_READ_ONLY = 2
    ACCOUNT_ACCESS_LEVEL_NO_ACCESS = 3
