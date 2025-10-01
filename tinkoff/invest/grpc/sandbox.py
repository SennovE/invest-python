from dataclasses import dataclass
from typing import Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest._grpc_helpers import message_field
from tinkoff.invest.grpc import sandbox_pb2, sandbox_pb2_grpc
from tinkoff.invest.grpc.common import MoneyValue
from tinkoff.invest.grpc.operations import (
    GetOperationsByCursorRequest,
    GetOperationsByCursorResponse,
    OperationsRequest,
    OperationsResponse,
    PortfolioRequest,
    PortfolioResponse,
    PositionsRequest,
    PositionsResponse,
    WithdrawLimitsRequest,
    WithdrawLimitsResponse,
)
from tinkoff.invest.grpc.orders import (
    CancelOrderRequest,
    CancelOrderResponse,
    GetMaxLotsRequest,
    GetMaxLotsResponse,
    GetOrdersRequest,
    GetOrdersResponse,
    GetOrderStateRequest,
    OrderState,
    PostOrderAsyncRequest,
    PostOrderAsyncResponse,
    PostOrderRequest,
    PostOrderResponse,
    ReplaceOrderRequest,
)
from tinkoff.invest.grpc.users import GetAccountsRequest, GetAccountsResponse
from tinkoff.invest.logging import get_tracking_id_from_call, log_request


class SandboxService(BaseService):
    """// Методы для работы с песочницей T-Invest API"""
    _protobuf = sandbox_pb2
    _protobuf_grpc = sandbox_pb2_grpc
    _protobuf_stub = _protobuf_grpc.SandboxServiceStub

    def open_sandbox_account(self, request: 'OpenSandboxAccountRequest'
        ) ->'OpenSandboxAccountResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            OpenSandboxAccountRequest())
        response, call = self._stub.OpenSandboxAccount.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'OpenSandboxAccount')
        return protobuf_to_dataclass(response, OpenSandboxAccountResponse)

    def get_sandbox_accounts(self, request: 'GetAccountsRequest'
        ) ->'GetAccountsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response, call = self._stub.GetSandboxAccounts.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSandboxAccounts')
        return protobuf_to_dataclass(response, GetAccountsResponse)

    def close_sandbox_account(self, request: 'CloseSandboxAccountRequest'
        ) ->'CloseSandboxAccountResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CloseSandboxAccountRequest())
        response, call = self._stub.CloseSandboxAccount.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'CloseSandboxAccount')
        return protobuf_to_dataclass(response, CloseSandboxAccountResponse)

    def post_sandbox_order(self, request: 'PostOrderRequest'
        ) ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderRequest())
        response, call = self._stub.PostSandboxOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'PostSandboxOrder')
        return protobuf_to_dataclass(response, PostOrderResponse)

    def post_sandbox_order_async(self, request: 'PostOrderAsyncRequest'
        ) ->'PostOrderAsyncResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderAsyncRequest())
        response, call = self._stub.PostSandboxOrderAsync.with_call(request
            =protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'PostSandboxOrderAsync')
        return protobuf_to_dataclass(response, PostOrderAsyncResponse)

    def replace_sandbox_order(self, request: 'ReplaceOrderRequest'
        ) ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            ReplaceOrderRequest())
        response, call = self._stub.ReplaceSandboxOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'ReplaceSandboxOrder')
        return protobuf_to_dataclass(response, PostOrderResponse)

    def get_sandbox_orders(self, request: 'GetOrdersRequest'
        ) ->'GetOrdersResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrdersRequest())
        response, call = self._stub.GetSandboxOrders.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSandboxOrders')
        return protobuf_to_dataclass(response, GetOrdersResponse)

    def cancel_sandbox_order(self, request: 'CancelOrderRequest'
        ) ->'CancelOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CancelOrderRequest())
        response, call = self._stub.CancelSandboxOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'CancelSandboxOrder')
        return protobuf_to_dataclass(response, CancelOrderResponse)

    def get_sandbox_order_state(self, request: 'GetOrderStateRequest'
        ) ->'OrderState':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderStateRequest())
        response, call = self._stub.GetSandboxOrderState.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSandboxOrderState')
        return protobuf_to_dataclass(response, OrderState)

    def get_sandbox_positions(self, request: 'PositionsRequest'
        ) ->'PositionsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PositionsRequest())
        response, call = self._stub.GetSandboxPositions.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSandboxPositions')
        return protobuf_to_dataclass(response, PositionsResponse)

    def get_sandbox_operations(self, request: 'OperationsRequest'
        ) ->'OperationsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            OperationsRequest())
        response, call = self._stub.GetSandboxOperations.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSandboxOperations')
        return protobuf_to_dataclass(response, OperationsResponse)

    def get_sandbox_operations_by_cursor(self, request:
        'GetOperationsByCursorRequest') ->'GetOperationsByCursorResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOperationsByCursorRequest())
        response, call = self._stub.GetSandboxOperationsByCursor.with_call(
            request=protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call),
            'GetSandboxOperationsByCursor')
        return protobuf_to_dataclass(response, GetOperationsByCursorResponse)

    def get_sandbox_portfolio(self, request: 'PortfolioRequest'
        ) ->'PortfolioResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PortfolioRequest())
        response, call = self._stub.GetSandboxPortfolio.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSandboxPortfolio')
        return protobuf_to_dataclass(response, PortfolioResponse)

    def sandbox_pay_in(self, request: 'SandboxPayInRequest'
        ) ->'SandboxPayInResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            SandboxPayInRequest())
        response, call = self._stub.SandboxPayIn.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'SandboxPayIn')
        return protobuf_to_dataclass(response, SandboxPayInResponse)

    def get_sandbox_withdraw_limits(self, request: 'WithdrawLimitsRequest'
        ) ->'WithdrawLimitsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            WithdrawLimitsRequest())
        response, call = self._stub.GetSandboxWithdrawLimits.with_call(request
            =protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSandboxWithdrawLimits'
            )
        return protobuf_to_dataclass(response, WithdrawLimitsResponse)

    def get_sandbox_max_lots(self, request: 'GetMaxLotsRequest'
        ) ->'GetMaxLotsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMaxLotsRequest())
        response, call = self._stub.GetSandboxMaxLots.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSandboxMaxLots')
        return protobuf_to_dataclass(response, GetMaxLotsResponse)


@dataclass
class OpenSandboxAccountRequest:
    name: Optional[str] = message_field(1, optional=True)


@dataclass
class OpenSandboxAccountResponse:
    account_id: str = message_field(1)


@dataclass
class CloseSandboxAccountRequest:
    account_id: str = message_field(1)


@dataclass
class CloseSandboxAccountResponse:
    pass


@dataclass
class SandboxPayInRequest:
    account_id: str = message_field(1)
    amount: 'MoneyValue' = message_field(2)


@dataclass
class SandboxPayInResponse:
    balance: 'MoneyValue' = message_field(1)
