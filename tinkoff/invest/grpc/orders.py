from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import AsyncIterable, Iterable, List, Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest._errors import (
    handle_aio_request_error,
    handle_aio_request_error_gen,
    handle_request_error,
    handle_request_error_gen,
)
from tinkoff.invest._grpc_helpers import message_field
from tinkoff.invest.grpc import orders_pb2, orders_pb2_grpc
from tinkoff.invest.grpc.common import (
    ErrorDetail,
    MoneyValue,
    Ping,
    PriceType,
    Quotation,
    ResponseMetadata,
    ResultSubscriptionStatus,
)
from tinkoff.invest.logging import (
    get_tracking_id_from_call,
    get_tracking_id_from_coro,
    log_request,
)


class OrdersStreamService(BaseService):
    """//TradesStream — стрим сделок пользователя"""
    _protobuf = orders_pb2
    _protobuf_grpc = orders_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OrdersStreamServiceStub

    @handle_request_error_gen('TradesStream')
    def trades_stream(self, request: 'TradesStreamRequest') ->Iterable[
        'TradesStreamResponse']:
        for response in self._stub.TradesStream(request=
            dataclass_to_protobuf(request, self._protobuf.
            TradesStreamRequest()), metadata=self._metadata):
            yield protobuf_to_dataclass(response, TradesStreamResponse)

    @handle_request_error_gen('OrderStateStream')
    def order_state_stream(self, request: 'OrderStateStreamRequest'
        ) ->Iterable['OrderStateStreamResponse']:
        for response in self._stub.OrderStateStream(request=
            dataclass_to_protobuf(request, self._protobuf.
            OrderStateStreamRequest()), metadata=self._metadata):
            yield protobuf_to_dataclass(response, OrderStateStreamResponse)


class AsyncOrdersStreamService(BaseService):
    _protobuf = orders_pb2
    _protobuf_grpc = orders_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OrdersStreamServiceStub

    @handle_aio_request_error_gen('TradesStream')
    async def trades_stream(self, request: 'TradesStreamRequest'
        ) ->AsyncIterable['TradesStreamResponse']:
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            TradesStreamRequest())
        async for response in self._stub.TradesStream(request=
            protobuf_request, metadata=self._metadata):(yield
            protobuf_to_dataclass(response, TradesStreamResponse))

    @handle_aio_request_error_gen('OrderStateStream')
    async def order_state_stream(self, request: 'OrderStateStreamRequest'
        ) ->AsyncIterable['OrderStateStreamResponse']:
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            OrderStateStreamRequest())
        async for response in self._stub.OrderStateStream(request=
            protobuf_request, metadata=self._metadata):(yield
            protobuf_to_dataclass(response, OrderStateStreamResponse))


class OrdersService(BaseService):
    """/* Сервис предназначен для работы с торговыми поручениями:<br/> **1**.
                        выставление;<br/> **2**. отмена;<br/> **3**. получение статуса;<br/> **4**.
                        расчет полной стоимости;<br/> **5**. получение списка заявок.*/"""
    _protobuf = orders_pb2
    _protobuf_grpc = orders_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OrdersServiceStub

    @handle_request_error('PostOrder')
    def post_order(self, request: 'PostOrderRequest') ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderRequest())
        response, call = self._stub.PostOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'PostOrder')
        return protobuf_to_dataclass(response, PostOrderResponse)

    @handle_request_error('PostOrderAsync')
    def post_order_async(self, request: 'PostOrderAsyncRequest'
        ) ->'PostOrderAsyncResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderAsyncRequest())
        response, call = self._stub.PostOrderAsync.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'PostOrderAsync')
        return protobuf_to_dataclass(response, PostOrderAsyncResponse)

    @handle_request_error('CancelOrder')
    def cancel_order(self, request: 'CancelOrderRequest'
        ) ->'CancelOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CancelOrderRequest())
        response, call = self._stub.CancelOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'CancelOrder')
        return protobuf_to_dataclass(response, CancelOrderResponse)

    @handle_request_error('GetOrderState')
    def get_order_state(self, request: 'GetOrderStateRequest') ->'OrderState':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderStateRequest())
        response, call = self._stub.GetOrderState.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetOrderState')
        return protobuf_to_dataclass(response, OrderState)

    @handle_request_error('GetOrders')
    def get_orders(self, request: 'GetOrdersRequest') ->'GetOrdersResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrdersRequest())
        response, call = self._stub.GetOrders.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetOrders')
        return protobuf_to_dataclass(response, GetOrdersResponse)

    @handle_request_error('ReplaceOrder')
    def replace_order(self, request: 'ReplaceOrderRequest'
        ) ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            ReplaceOrderRequest())
        response, call = self._stub.ReplaceOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'ReplaceOrder')
        return protobuf_to_dataclass(response, PostOrderResponse)

    @handle_request_error('GetMaxLots')
    def get_max_lots(self, request: 'GetMaxLotsRequest'
        ) ->'GetMaxLotsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMaxLotsRequest())
        response, call = self._stub.GetMaxLots.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetMaxLots')
        return protobuf_to_dataclass(response, GetMaxLotsResponse)

    @handle_request_error('GetOrderPrice')
    def get_order_price(self, request: 'GetOrderPriceRequest'
        ) ->'GetOrderPriceResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderPriceRequest())
        response, call = self._stub.GetOrderPrice.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetOrderPrice')
        return protobuf_to_dataclass(response, GetOrderPriceResponse)


class AsyncOrdersService(BaseService):
    """//PostOrder — выставить заявку"""
    _protobuf = orders_pb2
    _protobuf_grpc = orders_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OrdersServiceStub

    @handle_aio_request_error('PostOrder')
    async def post_order(self, request: 'PostOrderRequest'
        ) ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderRequest())
        response_coro = self._stub.PostOrder(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'PostOrder'
            )
        return protobuf_to_dataclass(response, PostOrderResponse)

    @handle_aio_request_error('PostOrderAsync')
    async def post_order_async(self, request: 'PostOrderAsyncRequest'
        ) ->'PostOrderAsyncResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderAsyncRequest())
        response_coro = self._stub.PostOrderAsync(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'PostOrderAsync')
        return protobuf_to_dataclass(response, PostOrderAsyncResponse)

    @handle_aio_request_error('CancelOrder')
    async def cancel_order(self, request: 'CancelOrderRequest'
        ) ->'CancelOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CancelOrderRequest())
        response_coro = self._stub.CancelOrder(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'CancelOrder')
        return protobuf_to_dataclass(response, CancelOrderResponse)

    @handle_aio_request_error('GetOrderState')
    async def get_order_state(self, request: 'GetOrderStateRequest'
        ) ->'OrderState':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderStateRequest())
        response_coro = self._stub.GetOrderState(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetOrderState')
        return protobuf_to_dataclass(response, OrderState)

    @handle_aio_request_error('GetOrders')
    async def get_orders(self, request: 'GetOrdersRequest'
        ) ->'GetOrdersResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrdersRequest())
        response_coro = self._stub.GetOrders(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'GetOrders'
            )
        return protobuf_to_dataclass(response, GetOrdersResponse)

    @handle_aio_request_error('ReplaceOrder')
    async def replace_order(self, request: 'ReplaceOrderRequest'
        ) ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            ReplaceOrderRequest())
        response_coro = self._stub.ReplaceOrder(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'ReplaceOrder')
        return protobuf_to_dataclass(response, PostOrderResponse)

    @handle_aio_request_error('GetMaxLots')
    async def get_max_lots(self, request: 'GetMaxLotsRequest'
        ) ->'GetMaxLotsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMaxLotsRequest())
        response_coro = self._stub.GetMaxLots(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetMaxLots')
        return protobuf_to_dataclass(response, GetMaxLotsResponse)

    @handle_aio_request_error('GetOrderPrice')
    async def get_order_price(self, request: 'GetOrderPriceRequest'
        ) ->'GetOrderPriceResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderPriceRequest())
        response_coro = self._stub.GetOrderPrice(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetOrderPrice')
        return protobuf_to_dataclass(response, GetOrderPriceResponse)


@dataclass
class TradesStreamRequest:
    accounts: List[str] = message_field(1)
    ping_delay_ms: Optional[int] = message_field(15, optional=True)


@dataclass
class TradesStreamResponse:
    order_trades: Optional['OrderTrades'] = message_field(1, optional=True)
    ping: Optional['Ping'] = message_field(2, optional=True)
    subscription: Optional['SubscriptionResponse'] = message_field(3,
        optional=True)


@dataclass
class OrderTrades:
    order_id: str = message_field(1)
    created_at: datetime = message_field(2)
    direction: 'OrderDirection' = message_field(3)
    figi: str = message_field(4)
    trades: List['OrderTrade'] = message_field(5)
    account_id: str = message_field(6)
    instrument_uid: str = message_field(7)


@dataclass
class OrderTrade:
    date_time: datetime = message_field(1)
    price: 'Quotation' = message_field(2)
    quantity: int = message_field(3)
    trade_id: str = message_field(4)


@dataclass
class PostOrderRequest:
    figi: Optional[str] = message_field(1, optional=True)
    quantity: int = message_field(2)
    price: Optional['Quotation'] = message_field(3, optional=True)
    direction: 'OrderDirection' = message_field(4)
    account_id: str = message_field(5)
    order_type: 'OrderType' = message_field(6)
    order_id: str = message_field(7)
    instrument_id: str = message_field(8)
    time_in_force: 'TimeInForceType' = message_field(9)
    price_type: 'PriceType' = message_field(10)
    confirm_margin_trade: bool = message_field(11)


@dataclass
class PostOrderResponse:
    order_id: str = message_field(1)
    execution_report_status: 'OrderExecutionReportStatus' = message_field(2)
    lots_requested: int = message_field(3)
    lots_executed: int = message_field(4)
    initial_order_price: 'MoneyValue' = message_field(5)
    executed_order_price: 'MoneyValue' = message_field(6)
    total_order_amount: 'MoneyValue' = message_field(7)
    initial_commission: 'MoneyValue' = message_field(8)
    executed_commission: 'MoneyValue' = message_field(9)
    aci_value: 'MoneyValue' = message_field(10)
    figi: str = message_field(11)
    direction: 'OrderDirection' = message_field(12)
    initial_security_price: 'MoneyValue' = message_field(13)
    order_type: 'OrderType' = message_field(14)
    message: str = message_field(15)
    initial_order_price_pt: 'Quotation' = message_field(16)
    instrument_uid: str = message_field(17)
    order_request_id: str = message_field(20)
    response_metadata: 'ResponseMetadata' = message_field(254)


@dataclass
class PostOrderAsyncRequest:
    instrument_id: str = message_field(1)
    quantity: int = message_field(2)
    price: Optional['Quotation'] = message_field(3, optional=True)
    direction: 'OrderDirection' = message_field(4)
    account_id: str = message_field(5)
    order_type: 'OrderType' = message_field(6)
    order_id: str = message_field(7)
    time_in_force: Optional['TimeInForceType'] = message_field(8, optional=True
        )
    price_type: Optional['PriceType'] = message_field(9, optional=True)
    confirm_margin_trade: bool = message_field(10)


@dataclass
class PostOrderAsyncResponse:
    order_request_id: str = message_field(1)
    execution_report_status: 'OrderExecutionReportStatus' = message_field(2)
    trade_intent_id: Optional[str] = message_field(3, optional=True)


@dataclass
class CancelOrderRequest:
    account_id: str = message_field(1)
    order_id: str = message_field(2)
    order_id_type: Optional['OrderIdType'] = message_field(3, optional=True)


@dataclass
class CancelOrderResponse:
    time: datetime = message_field(1)
    response_metadata: 'ResponseMetadata' = message_field(254)


@dataclass
class GetOrderStateRequest:
    account_id: str = message_field(1)
    order_id: str = message_field(2)
    price_type: 'PriceType' = message_field(3)
    order_id_type: Optional['OrderIdType'] = message_field(4, optional=True)


@dataclass
class GetOrdersRequest:
    account_id: str = message_field(1)
    advanced_filters: Optional['GetOrdersRequestFilters'] = message_field(2,
        optional=True)


    @dataclass
    class GetOrdersRequestFilters:
        from_: Optional[datetime] = message_field(1, optional=True)
        to: Optional[datetime] = message_field(2, optional=True)
        execution_status: List['OrderExecutionReportStatus'] = message_field(3)


@dataclass
class GetOrdersResponse:
    orders: List['OrderState'] = message_field(1)


@dataclass
class OrderState:
    order_id: str = message_field(1)
    execution_report_status: 'OrderExecutionReportStatus' = message_field(2)
    lots_requested: int = message_field(3)
    lots_executed: int = message_field(4)
    initial_order_price: 'MoneyValue' = message_field(5)
    executed_order_price: 'MoneyValue' = message_field(6)
    total_order_amount: 'MoneyValue' = message_field(7)
    average_position_price: 'MoneyValue' = message_field(8)
    initial_commission: 'MoneyValue' = message_field(9)
    executed_commission: 'MoneyValue' = message_field(10)
    figi: str = message_field(11)
    direction: 'OrderDirection' = message_field(12)
    initial_security_price: 'MoneyValue' = message_field(13)
    stages: List['OrderStage'] = message_field(14)
    service_commission: 'MoneyValue' = message_field(15)
    currency: str = message_field(16)
    order_type: 'OrderType' = message_field(17)
    order_date: datetime = message_field(18)
    instrument_uid: str = message_field(19)
    order_request_id: str = message_field(20)


@dataclass
class OrderStage:
    price: 'MoneyValue' = message_field(1)
    quantity: int = message_field(2)
    trade_id: str = message_field(3)
    execution_time: datetime = message_field(5)


@dataclass
class ReplaceOrderRequest:
    account_id: str = message_field(1)
    order_id: str = message_field(6)
    idempotency_key: str = message_field(7)
    quantity: int = message_field(11)
    price: Optional['Quotation'] = message_field(12, optional=True)
    price_type: Optional['PriceType'] = message_field(13, optional=True)
    confirm_margin_trade: bool = message_field(14)


@dataclass
class GetMaxLotsRequest:
    account_id: str = message_field(1)
    instrument_id: str = message_field(2)
    price: Optional['Quotation'] = message_field(3, optional=True)


@dataclass
class GetMaxLotsResponse:
    currency: str = message_field(1)
    buy_limits: 'BuyLimitsView' = message_field(2)
    buy_margin_limits: 'BuyLimitsView' = message_field(3)
    sell_limits: 'SellLimitsView' = message_field(4)
    sell_margin_limits: 'SellLimitsView' = message_field(5)


    @dataclass
    class BuyLimitsView:
        buy_money_amount: 'Quotation' = message_field(1)
        buy_max_lots: int = message_field(2)
        buy_max_market_lots: int = message_field(3)


    @dataclass
    class SellLimitsView:
        sell_max_lots: int = message_field(1)


@dataclass
class GetOrderPriceRequest:
    account_id: str = message_field(1)
    instrument_id: str = message_field(2)
    price: 'Quotation' = message_field(3)
    direction: 'OrderDirection' = message_field(12)
    quantity: int = message_field(13)


@dataclass
class GetOrderPriceResponse:
    total_order_amount: 'MoneyValue' = message_field(1)
    initial_order_amount: 'MoneyValue' = message_field(5)
    lots_requested: int = message_field(3)
    executed_commission: 'MoneyValue' = message_field(7)
    executed_commission_rub: 'MoneyValue' = message_field(8)
    service_commission: 'MoneyValue' = message_field(9)
    deal_commission: 'MoneyValue' = message_field(10)
    extra_bond: Optional['ExtraBond'] = message_field(12, optional=True)
    extra_future: Optional['ExtraFuture'] = message_field(13, optional=True)


    @dataclass
    class ExtraBond:
        aci_value: 'MoneyValue' = message_field(2)
        nominal_conversion_rate: 'Quotation' = message_field(3)


    @dataclass
    class ExtraFuture:
        initial_margin: 'MoneyValue' = message_field(2)


@dataclass
class OrderStateStreamRequest:
    accounts: List[str] = message_field(1)
    ping_delay_millis: Optional[int] = message_field(15, optional=True)


@dataclass
class SubscriptionResponse:
    tracking_id: str = message_field(1)
    status: 'ResultSubscriptionStatus' = message_field(2)
    stream_id: str = message_field(4)
    accounts: List[str] = message_field(5)
    error: Optional['ErrorDetail'] = message_field(7, optional=True)


@dataclass
class OrderStateStreamResponse:
    order_state: Optional['OrderState'] = message_field(1, optional=True)
    ping: Optional['Ping'] = message_field(2, optional=True)
    subscription: Optional['SubscriptionResponse'] = message_field(3,
        optional=True)


    @dataclass
    class OrderState:
        order_id: str = message_field(1)
        order_request_id: Optional[str] = message_field(2, optional=True)
        client_code: str = message_field(3)
        created_at: datetime = message_field(4)
        execution_report_status: 'OrderExecutionReportStatus' = message_field(5
            )
        status_info: Optional['StatusCauseInfo'] = message_field(6,
            optional=True)
        ticker: str = message_field(7)
        class_code: str = message_field(8)
        lot_size: int = message_field(9)
        direction: 'OrderDirection' = message_field(10)
        time_in_force: 'TimeInForceType' = message_field(11)
        order_type: 'OrderType' = message_field(12)
        account_id: str = message_field(13)
        initial_order_price: 'MoneyValue' = message_field(22)
        order_price: 'MoneyValue' = message_field(23)
        amount: Optional['MoneyValue'] = message_field(24, optional=True)
        executed_order_price: 'MoneyValue' = message_field(25)
        currency: str = message_field(26)
        lots_requested: int = message_field(27)
        lots_executed: int = message_field(28)
        lots_left: int = message_field(29)
        lots_cancelled: int = message_field(30)
        marker: Optional['MarkerType'] = message_field(31, optional=True)
        trades: List['OrderTrade'] = message_field(33)
        completion_time: datetime = message_field(35)
        exchange: str = message_field(36)
        instrument_uid: str = message_field(41)


    class MarkerType(IntEnum):
        MARKER_UNKNOWN = 0
        MARKER_BROKER = 1
        MARKER_CHAT = 2
        MARKER_PAPER = 3
        MARKER_MARGIN = 4
        MARKER_TKBNM = 5
        MARKER_SHORT = 6
        MARKER_SPECMM = 7
        MARKER_PO = 8


    class StatusCauseInfo(IntEnum):
        CAUSE_UNSPECIFIED = 0
        CAUSE_CANCELLED_BY_CLIENT = 15
        CAUSE_CANCELLED_BY_EXCHANGE = 1
        CAUSE_CANCELLED_NOT_ENOUGH_POSITION = 2
        CAUSE_CANCELLED_BY_CLIENT_BLOCK = 3
        CAUSE_REJECTED_BY_BROKER = 4
        CAUSE_REJECTED_BY_EXCHANGE = 5
        CAUSE_CANCELLED_BY_BROKER = 6


class OrderDirection(IntEnum):
    ORDER_DIRECTION_UNSPECIFIED = 0
    ORDER_DIRECTION_BUY = 1
    ORDER_DIRECTION_SELL = 2


class OrderType(IntEnum):
    ORDER_TYPE_UNSPECIFIED = 0
    ORDER_TYPE_LIMIT = 1
    ORDER_TYPE_MARKET = 2
    ORDER_TYPE_BESTPRICE = 3


class OrderExecutionReportStatus(IntEnum):
    EXECUTION_REPORT_STATUS_UNSPECIFIED = 0
    EXECUTION_REPORT_STATUS_FILL = 1
    EXECUTION_REPORT_STATUS_REJECTED = 2
    EXECUTION_REPORT_STATUS_CANCELLED = 3
    EXECUTION_REPORT_STATUS_NEW = 4
    EXECUTION_REPORT_STATUS_PARTIALLYFILL = 5


class TimeInForceType(IntEnum):
    TIME_IN_FORCE_UNSPECIFIED = 0
    TIME_IN_FORCE_DAY = 1
    TIME_IN_FORCE_FILL_AND_KILL = 2
    TIME_IN_FORCE_FILL_OR_KILL = 3


class OrderIdType(IntEnum):
    ORDER_ID_TYPE_UNSPECIFIED = 0
    ORDER_ID_TYPE_EXCHANGE = 1
    ORDER_ID_TYPE_REQUEST = 2
