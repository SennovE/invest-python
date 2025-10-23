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
from tinkoff.invest.grpc import marketdata_pb2, marketdata_pb2_grpc
from tinkoff.invest.grpc.common import (
    InstrumentStatus,
    Ping,
    PingDelaySettings,
    PingRequest,
    Quotation,
    SecurityTradingStatus,
)
from tinkoff.invest.logging import (
    get_tracking_id_from_call,
    get_tracking_id_from_coro,
    log_request,
)


class MarketDataService(BaseService):
    """//Сервис для получения биржевой информации:<br/> 1. Свечи.<br/> 2. Стаканы.<br/> 3. Торговые статусы.<br/> 4. Лента сделок."""
    _protobuf = marketdata_pb2
    _protobuf_grpc = marketdata_pb2_grpc
    _protobuf_stub = _protobuf_grpc.MarketDataServiceStub

    @handle_request_error('GetCandles')
    def get_candles(self, request: 'GetCandlesRequest') ->'GetCandlesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetCandlesRequest())
        response, call = self._stub.GetCandles.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetCandles')
        return protobuf_to_dataclass(response, GetCandlesResponse)

    @handle_request_error('GetLastPrices')
    def get_last_prices(self, request: 'GetLastPricesRequest'
        ) ->'GetLastPricesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetLastPricesRequest())
        response, call = self._stub.GetLastPrices.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetLastPrices')
        return protobuf_to_dataclass(response, GetLastPricesResponse)

    @handle_request_error('GetOrderBook')
    def get_order_book(self, request: 'GetOrderBookRequest'
        ) ->'GetOrderBookResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderBookRequest())
        response, call = self._stub.GetOrderBook.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetOrderBook')
        return protobuf_to_dataclass(response, GetOrderBookResponse)

    @handle_request_error('GetTradingStatus')
    def get_trading_status(self, request: 'GetTradingStatusRequest'
        ) ->'GetTradingStatusResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetTradingStatusRequest())
        response, call = self._stub.GetTradingStatus.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetTradingStatus')
        return protobuf_to_dataclass(response, GetTradingStatusResponse)

    @handle_request_error('GetTradingStatuses')
    def get_trading_statuses(self, request: 'GetTradingStatusesRequest'
        ) ->'GetTradingStatusesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetTradingStatusesRequest())
        response, call = self._stub.GetTradingStatuses.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetTradingStatuses')
        return protobuf_to_dataclass(response, GetTradingStatusesResponse)

    @handle_request_error('GetLastTrades')
    def get_last_trades(self, request: 'GetLastTradesRequest'
        ) ->'GetLastTradesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetLastTradesRequest())
        response, call = self._stub.GetLastTrades.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetLastTrades')
        return protobuf_to_dataclass(response, GetLastTradesResponse)

    @handle_request_error('GetClosePrices')
    def get_close_prices(self, request: 'GetClosePricesRequest'
        ) ->'GetClosePricesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetClosePricesRequest())
        response, call = self._stub.GetClosePrices.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetClosePrices')
        return protobuf_to_dataclass(response, GetClosePricesResponse)

    @handle_request_error('GetTechAnalysis')
    def get_tech_analysis(self, request: 'GetTechAnalysisRequest'
        ) ->'GetTechAnalysisResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetTechAnalysisRequest())
        response, call = self._stub.GetTechAnalysis.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetTechAnalysis')
        return protobuf_to_dataclass(response, GetTechAnalysisResponse)

    @handle_request_error('GetMarketValues')
    def get_market_values(self, request: 'GetMarketValuesRequest'
        ) ->'GetMarketValuesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMarketValuesRequest())
        response, call = self._stub.GetMarketValues.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetMarketValues')
        return protobuf_to_dataclass(response, GetMarketValuesResponse)


class AsyncMarketDataService(BaseService):
    """//GetCandles — исторические свечи по инструменту"""
    _protobuf = marketdata_pb2
    _protobuf_grpc = marketdata_pb2_grpc
    _protobuf_stub = _protobuf_grpc.MarketDataServiceStub

    @handle_aio_request_error('GetCandles')
    async def get_candles(self, request: 'GetCandlesRequest'
        ) ->'GetCandlesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetCandlesRequest())
        response_coro = self._stub.GetCandles(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetCandles')
        return protobuf_to_dataclass(response, GetCandlesResponse)

    @handle_aio_request_error('GetLastPrices')
    async def get_last_prices(self, request: 'GetLastPricesRequest'
        ) ->'GetLastPricesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetLastPricesRequest())
        response_coro = self._stub.GetLastPrices(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetLastPrices')
        return protobuf_to_dataclass(response, GetLastPricesResponse)

    @handle_aio_request_error('GetOrderBook')
    async def get_order_book(self, request: 'GetOrderBookRequest'
        ) ->'GetOrderBookResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderBookRequest())
        response_coro = self._stub.GetOrderBook(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetOrderBook')
        return protobuf_to_dataclass(response, GetOrderBookResponse)

    @handle_aio_request_error('GetTradingStatus')
    async def get_trading_status(self, request: 'GetTradingStatusRequest'
        ) ->'GetTradingStatusResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetTradingStatusRequest())
        response_coro = self._stub.GetTradingStatus(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetTradingStatus')
        return protobuf_to_dataclass(response, GetTradingStatusResponse)

    @handle_aio_request_error('GetTradingStatuses')
    async def get_trading_statuses(self, request: 'GetTradingStatusesRequest'
        ) ->'GetTradingStatusesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetTradingStatusesRequest())
        response_coro = self._stub.GetTradingStatuses(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetTradingStatuses')
        return protobuf_to_dataclass(response, GetTradingStatusesResponse)

    @handle_aio_request_error('GetLastTrades')
    async def get_last_trades(self, request: 'GetLastTradesRequest'
        ) ->'GetLastTradesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetLastTradesRequest())
        response_coro = self._stub.GetLastTrades(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetLastTrades')
        return protobuf_to_dataclass(response, GetLastTradesResponse)

    @handle_aio_request_error('GetClosePrices')
    async def get_close_prices(self, request: 'GetClosePricesRequest'
        ) ->'GetClosePricesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetClosePricesRequest())
        response_coro = self._stub.GetClosePrices(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetClosePrices')
        return protobuf_to_dataclass(response, GetClosePricesResponse)

    @handle_aio_request_error('GetTechAnalysis')
    async def get_tech_analysis(self, request: 'GetTechAnalysisRequest'
        ) ->'GetTechAnalysisResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetTechAnalysisRequest())
        response_coro = self._stub.GetTechAnalysis(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetTechAnalysis')
        return protobuf_to_dataclass(response, GetTechAnalysisResponse)

    @handle_aio_request_error('GetMarketValues')
    async def get_market_values(self, request: 'GetMarketValuesRequest'
        ) ->'GetMarketValuesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMarketValuesRequest())
        response_coro = self._stub.GetMarketValues(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetMarketValues')
        return protobuf_to_dataclass(response, GetMarketValuesResponse)


class MarketDataStreamService(BaseService):
    """//MarketDataStream — bidirectional стрим предоставления биржевой информации"""
    _protobuf = marketdata_pb2
    _protobuf_grpc = marketdata_pb2_grpc
    _protobuf_stub = _protobuf_grpc.MarketDataStreamServiceStub

    @handle_request_error_gen('MarketDataStream')
    def market_data_stream(self, requests: Iterable['MarketDataRequest']
        ) ->Iterable['MarketDataResponse']:
        for response in self._stub.MarketDataStream(request_iterator=(
            dataclass_to_protobuf(request, self._protobuf.MarketDataRequest
            ()) for request in requests), metadata=self._metadata):
            yield protobuf_to_dataclass(response, MarketDataResponse)

    @handle_request_error_gen('MarketDataServerSideStream')
    def market_data_server_side_stream(self, request:
        'MarketDataServerSideStreamRequest') ->Iterable['MarketDataResponse']:
        for response in self._stub.MarketDataServerSideStream(request=
            dataclass_to_protobuf(request, self._protobuf.
            MarketDataServerSideStreamRequest()), metadata=self._metadata):
            yield protobuf_to_dataclass(response, MarketDataResponse)


class AsyncMarketDataStreamService(BaseService):
    _protobuf = marketdata_pb2
    _protobuf_grpc = marketdata_pb2_grpc
    _protobuf_stub = _protobuf_grpc.MarketDataStreamServiceStub

    @handle_aio_request_error_gen('MarketDataStream')
    async def market_data_stream(self, request_iterator: AsyncIterable[
        'MarketDataRequest']) ->AsyncIterable['MarketDataResponse']:
        protobuf_request_iterator = (dataclass_to_protobuf(request, self.
            _protobuf.MarketDataRequest()) async for request in
            request_iterator)
        async for response in self._stub.MarketDataStream(request_iterator=
            protobuf_request_iterator, metadata=self._metadata):(yield
            protobuf_to_dataclass(response, MarketDataResponse))

    @handle_aio_request_error_gen('MarketDataServerSideStream')
    async def market_data_server_side_stream(self, request:
        'MarketDataServerSideStreamRequest') ->AsyncIterable[
        'MarketDataResponse']:
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            MarketDataServerSideStreamRequest())
        async for response in self._stub.MarketDataServerSideStream(request
            =protobuf_request, metadata=self._metadata):(yield
            protobuf_to_dataclass(response, MarketDataResponse))


@dataclass
class MarketDataRequest:
    subscribe_candles_request: Optional['SubscribeCandlesRequest'
        ] = message_field(1, optional=True)
    subscribe_order_book_request: Optional['SubscribeOrderBookRequest'
        ] = message_field(2, optional=True)
    subscribe_trades_request: Optional['SubscribeTradesRequest'
        ] = message_field(3, optional=True)
    subscribe_info_request: Optional['SubscribeInfoRequest'] = message_field(
        4, optional=True)
    subscribe_last_price_request: Optional['SubscribeLastPriceRequest'
        ] = message_field(5, optional=True)
    get_my_subscriptions: Optional['GetMySubscriptions'] = message_field(6,
        optional=True)
    ping: Optional['PingRequest'] = message_field(7, optional=True)
    ping_settings: Optional['PingDelaySettings'] = message_field(15,
        optional=True)


@dataclass
class MarketDataServerSideStreamRequest:
    subscribe_candles_request: 'SubscribeCandlesRequest' = message_field(1)
    subscribe_order_book_request: 'SubscribeOrderBookRequest' = message_field(2
        )
    subscribe_trades_request: 'SubscribeTradesRequest' = message_field(3)
    subscribe_info_request: 'SubscribeInfoRequest' = message_field(4)
    subscribe_last_price_request: 'SubscribeLastPriceRequest' = message_field(5
        )
    ping_settings: 'PingDelaySettings' = message_field(15)


@dataclass
class MarketDataResponse:
    subscribe_candles_response: Optional['SubscribeCandlesResponse'
        ] = message_field(1, optional=True)
    subscribe_order_book_response: Optional['SubscribeOrderBookResponse'
        ] = message_field(2, optional=True)
    subscribe_trades_response: Optional['SubscribeTradesResponse'
        ] = message_field(3, optional=True)
    subscribe_info_response: Optional['SubscribeInfoResponse'] = message_field(
        4, optional=True)
    candle: Optional['Candle'] = message_field(5, optional=True)
    trade: Optional['Trade'] = message_field(6, optional=True)
    orderbook: Optional['OrderBook'] = message_field(7, optional=True)
    trading_status: Optional['TradingStatus'] = message_field(8, optional=True)
    ping: Optional['Ping'] = message_field(9, optional=True)
    subscribe_last_price_response: Optional['SubscribeLastPriceResponse'
        ] = message_field(10, optional=True)
    last_price: Optional['LastPrice'] = message_field(11, optional=True)
    open_interest: Optional['OpenInterest'] = message_field(12, optional=True)


@dataclass
class SubscribeCandlesRequest:
    subscription_action: 'SubscriptionAction' = message_field(1)
    instruments: List['CandleInstrument'] = message_field(2)
    waiting_close: bool = message_field(3)
    candle_source_type: Optional['GetCandlesRequest.CandleSource'
        ] = message_field(9, optional=True)


class SubscriptionAction(IntEnum):
    SUBSCRIPTION_ACTION_UNSPECIFIED = 0
    SUBSCRIPTION_ACTION_SUBSCRIBE = 1
    SUBSCRIPTION_ACTION_UNSUBSCRIBE = 2


class SubscriptionInterval(IntEnum):
    SUBSCRIPTION_INTERVAL_UNSPECIFIED = 0
    SUBSCRIPTION_INTERVAL_ONE_MINUTE = 1
    SUBSCRIPTION_INTERVAL_FIVE_MINUTES = 2
    SUBSCRIPTION_INTERVAL_FIFTEEN_MINUTES = 3
    SUBSCRIPTION_INTERVAL_ONE_HOUR = 4
    SUBSCRIPTION_INTERVAL_ONE_DAY = 5
    SUBSCRIPTION_INTERVAL_2_MIN = 6
    SUBSCRIPTION_INTERVAL_3_MIN = 7
    SUBSCRIPTION_INTERVAL_10_MIN = 8
    SUBSCRIPTION_INTERVAL_30_MIN = 9
    SUBSCRIPTION_INTERVAL_2_HOUR = 10
    SUBSCRIPTION_INTERVAL_4_HOUR = 11
    SUBSCRIPTION_INTERVAL_WEEK = 12
    SUBSCRIPTION_INTERVAL_MONTH = 13


@dataclass
class CandleInstrument:
    figi: str = message_field(1)
    interval: 'SubscriptionInterval' = message_field(2)
    instrument_id: str = message_field(3)


@dataclass
class SubscribeCandlesResponse:
    tracking_id: str = message_field(1)
    candles_subscriptions: List['CandleSubscription'] = message_field(2)


@dataclass
class CandleSubscription:
    figi: str = message_field(1)
    interval: 'SubscriptionInterval' = message_field(2)
    subscription_status: 'SubscriptionStatus' = message_field(3)
    instrument_uid: str = message_field(4)
    waiting_close: bool = message_field(5)
    stream_id: str = message_field(6)
    subscription_id: str = message_field(7)
    subscription_action: 'SubscriptionAction' = message_field(8)
    candle_source_type: Optional['GetCandlesRequest.CandleSource'
        ] = message_field(9, optional=True)


class SubscriptionStatus(IntEnum):
    SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    SUBSCRIPTION_STATUS_SUCCESS = 1
    SUBSCRIPTION_STATUS_INSTRUMENT_NOT_FOUND = 2
    SUBSCRIPTION_STATUS_SUBSCRIPTION_ACTION_IS_INVALID = 3
    SUBSCRIPTION_STATUS_DEPTH_IS_INVALID = 4
    SUBSCRIPTION_STATUS_INTERVAL_IS_INVALID = 5
    SUBSCRIPTION_STATUS_LIMIT_IS_EXCEEDED = 6
    SUBSCRIPTION_STATUS_INTERNAL_ERROR = 7
    SUBSCRIPTION_STATUS_TOO_MANY_REQUESTS = 8
    SUBSCRIPTION_STATUS_SUBSCRIPTION_NOT_FOUND = 9
    SUBSCRIPTION_STATUS_SOURCE_IS_INVALID = 10


@dataclass
class SubscribeOrderBookRequest:
    subscription_action: 'SubscriptionAction' = message_field(1)
    instruments: List['OrderBookInstrument'] = message_field(2)


@dataclass
class OrderBookInstrument:
    figi: str = message_field(1)
    depth: int = message_field(2)
    instrument_id: str = message_field(3)
    order_book_type: 'OrderBookType' = message_field(4)


@dataclass
class SubscribeOrderBookResponse:
    tracking_id: str = message_field(1)
    order_book_subscriptions: List['OrderBookSubscription'] = message_field(2)


@dataclass
class OrderBookSubscription:
    figi: str = message_field(1)
    depth: int = message_field(2)
    subscription_status: 'SubscriptionStatus' = message_field(3)
    instrument_uid: str = message_field(4)
    stream_id: str = message_field(5)
    subscription_id: str = message_field(6)
    order_book_type: 'OrderBookType' = message_field(7)
    subscription_action: 'SubscriptionAction' = message_field(8)


class TradeSourceType(IntEnum):
    TRADE_SOURCE_UNSPECIFIED = 0
    TRADE_SOURCE_EXCHANGE = 1
    TRADE_SOURCE_DEALER = 2
    TRADE_SOURCE_ALL = 3


@dataclass
class SubscribeTradesRequest:
    subscription_action: 'SubscriptionAction' = message_field(1)
    instruments: List['TradeInstrument'] = message_field(2)
    trade_source: 'TradeSourceType' = message_field(3)
    with_open_interest: bool = message_field(4)


@dataclass
class TradeInstrument:
    figi: str = message_field(1)
    instrument_id: str = message_field(2)


@dataclass
class SubscribeTradesResponse:
    tracking_id: str = message_field(1)
    trade_subscriptions: List['TradeSubscription'] = message_field(2)
    trade_source: 'TradeSourceType' = message_field(3)


@dataclass
class TradeSubscription:
    figi: str = message_field(1)
    subscription_status: 'SubscriptionStatus' = message_field(2)
    instrument_uid: str = message_field(3)
    stream_id: str = message_field(4)
    subscription_id: str = message_field(5)
    with_open_interest: bool = message_field(6)
    subscription_action: 'SubscriptionAction' = message_field(7)


@dataclass
class SubscribeInfoRequest:
    subscription_action: 'SubscriptionAction' = message_field(1)
    instruments: List['InfoInstrument'] = message_field(2)


@dataclass
class InfoInstrument:
    figi: str = message_field(1)
    instrument_id: str = message_field(2)


@dataclass
class SubscribeInfoResponse:
    tracking_id: str = message_field(1)
    info_subscriptions: List['InfoSubscription'] = message_field(2)


@dataclass
class InfoSubscription:
    figi: str = message_field(1)
    subscription_status: 'SubscriptionStatus' = message_field(2)
    instrument_uid: str = message_field(3)
    stream_id: str = message_field(4)
    subscription_id: str = message_field(5)
    subscription_action: 'SubscriptionAction' = message_field(6)


@dataclass
class SubscribeLastPriceRequest:
    subscription_action: 'SubscriptionAction' = message_field(1)
    instruments: List['LastPriceInstrument'] = message_field(2)


@dataclass
class LastPriceInstrument:
    figi: str = message_field(1)
    instrument_id: str = message_field(2)


@dataclass
class SubscribeLastPriceResponse:
    tracking_id: str = message_field(1)
    last_price_subscriptions: List['LastPriceSubscription'] = message_field(2)


@dataclass
class LastPriceSubscription:
    figi: str = message_field(1)
    subscription_status: 'SubscriptionStatus' = message_field(2)
    instrument_uid: str = message_field(3)
    stream_id: str = message_field(4)
    subscription_id: str = message_field(5)
    subscription_action: 'SubscriptionAction' = message_field(6)


@dataclass
class Candle:
    figi: str = message_field(1)
    interval: 'SubscriptionInterval' = message_field(2)
    open: 'Quotation' = message_field(3)
    high: 'Quotation' = message_field(4)
    low: 'Quotation' = message_field(5)
    close: 'Quotation' = message_field(6)
    volume: int = message_field(7)
    time: datetime = message_field(8)
    last_trade_ts: datetime = message_field(9)
    instrument_uid: str = message_field(10)
    candle_source_type: 'CandleSource' = message_field(19)


@dataclass
class OrderBook:
    figi: str = message_field(1)
    depth: int = message_field(2)
    is_consistent: bool = message_field(3)
    bids: List['Order'] = message_field(4)
    asks: List['Order'] = message_field(5)
    time: datetime = message_field(6)
    limit_up: 'Quotation' = message_field(7)
    limit_down: 'Quotation' = message_field(8)
    instrument_uid: str = message_field(9)
    order_book_type: 'OrderBookType' = message_field(10)


@dataclass
class Order:
    price: 'Quotation' = message_field(1)
    quantity: int = message_field(2)


@dataclass
class Trade:
    figi: str = message_field(1)
    direction: 'TradeDirection' = message_field(2)
    price: 'Quotation' = message_field(3)
    quantity: int = message_field(4)
    time: datetime = message_field(5)
    instrument_uid: str = message_field(6)
    trade_source: 'TradeSourceType' = message_field(7)


class TradeDirection(IntEnum):
    TRADE_DIRECTION_UNSPECIFIED = 0
    TRADE_DIRECTION_BUY = 1
    TRADE_DIRECTION_SELL = 2


@dataclass
class TradingStatus:
    figi: str = message_field(1)
    trading_status: 'SecurityTradingStatus' = message_field(2)
    time: datetime = message_field(3)
    limit_order_available_flag: bool = message_field(4)
    market_order_available_flag: bool = message_field(5)
    instrument_uid: str = message_field(6)


@dataclass
class GetCandlesRequest:
    figi: Optional[str] = message_field(1, optional=True)
    from_: datetime = message_field(2)
    to: datetime = message_field(3)
    interval: 'CandleInterval' = message_field(4)
    instrument_id: Optional[str] = message_field(5, optional=True)
    candle_source_type: Optional['CandleSource'] = message_field(7,
        optional=True)
    limit: Optional[int] = message_field(10, optional=True)


    class CandleSource(IntEnum):
        CANDLE_SOURCE_UNSPECIFIED = 0
        CANDLE_SOURCE_EXCHANGE = 1
        CANDLE_SOURCE_INCLUDE_WEEKEND = 3


class CandleInterval(IntEnum):
    CANDLE_INTERVAL_UNSPECIFIED = 0
    CANDLE_INTERVAL_1_MIN = 1
    CANDLE_INTERVAL_5_MIN = 2
    CANDLE_INTERVAL_15_MIN = 3
    CANDLE_INTERVAL_HOUR = 4
    CANDLE_INTERVAL_DAY = 5
    CANDLE_INTERVAL_2_MIN = 6
    CANDLE_INTERVAL_3_MIN = 7
    CANDLE_INTERVAL_10_MIN = 8
    CANDLE_INTERVAL_30_MIN = 9
    CANDLE_INTERVAL_2_HOUR = 10
    CANDLE_INTERVAL_4_HOUR = 11
    CANDLE_INTERVAL_WEEK = 12
    CANDLE_INTERVAL_MONTH = 13
    CANDLE_INTERVAL_5_SEC = 14
    CANDLE_INTERVAL_10_SEC = 15
    CANDLE_INTERVAL_30_SEC = 16


class CandleSource(IntEnum):
    CANDLE_SOURCE_UNSPECIFIED = 0
    CANDLE_SOURCE_EXCHANGE = 1
    CANDLE_SOURCE_DEALER_WEEKEND = 2


@dataclass
class GetCandlesResponse:
    candles: List['HistoricCandle'] = message_field(1)


@dataclass
class HistoricCandle:
    open: 'Quotation' = message_field(1)
    high: 'Quotation' = message_field(2)
    low: 'Quotation' = message_field(3)
    close: 'Quotation' = message_field(4)
    volume: int = message_field(5)
    time: datetime = message_field(6)
    is_complete: bool = message_field(7)
    candle_source: 'CandleSource' = message_field(9)


@dataclass
class GetLastPricesRequest:
    figi: List[str] = message_field(1)
    instrument_id: List[str] = message_field(2)
    last_price_type: 'LastPriceType' = message_field(3)
    instrument_status: Optional['InstrumentStatus'] = message_field(9,
        optional=True)


@dataclass
class GetLastPricesResponse:
    last_prices: List['LastPrice'] = message_field(1)


@dataclass
class LastPrice:
    figi: str = message_field(1)
    price: 'Quotation' = message_field(2)
    time: datetime = message_field(3)
    instrument_uid: str = message_field(11)
    last_price_type: 'LastPriceType' = message_field(12)


@dataclass
class OpenInterest:
    instrument_uid: str = message_field(1)
    time: datetime = message_field(2)
    open_interest: int = message_field(3)


@dataclass
class GetOrderBookRequest:
    figi: Optional[str] = message_field(1, optional=True)
    depth: int = message_field(2)
    instrument_id: Optional[str] = message_field(3, optional=True)


@dataclass
class GetOrderBookResponse:
    figi: str = message_field(1)
    depth: int = message_field(2)
    bids: List['Order'] = message_field(3)
    asks: List['Order'] = message_field(4)
    last_price: 'Quotation' = message_field(5)
    close_price: 'Quotation' = message_field(6)
    limit_up: 'Quotation' = message_field(7)
    limit_down: 'Quotation' = message_field(8)
    last_price_ts: datetime = message_field(21)
    close_price_ts: datetime = message_field(22)
    orderbook_ts: datetime = message_field(23)
    instrument_uid: str = message_field(9)


@dataclass
class GetTradingStatusRequest:
    figi: Optional[str] = message_field(1, optional=True)
    instrument_id: Optional[str] = message_field(2, optional=True)


@dataclass
class GetTradingStatusesRequest:
    instrument_id: List[str] = message_field(1)


@dataclass
class GetTradingStatusesResponse:
    trading_statuses: List['GetTradingStatusResponse'] = message_field(1)


@dataclass
class GetTradingStatusResponse:
    figi: str = message_field(1)
    trading_status: 'SecurityTradingStatus' = message_field(2)
    limit_order_available_flag: bool = message_field(3)
    market_order_available_flag: bool = message_field(4)
    api_trade_available_flag: bool = message_field(5)
    instrument_uid: str = message_field(6)
    bestprice_order_available_flag: bool = message_field(8)
    only_best_price: bool = message_field(9)


@dataclass
class GetLastTradesRequest:
    figi: Optional[str] = message_field(1, optional=True)
    from_: datetime = message_field(2)
    to: datetime = message_field(3)
    instrument_id: Optional[str] = message_field(4, optional=True)
    trade_source: 'TradeSourceType' = message_field(5)


@dataclass
class GetLastTradesResponse:
    trades: List['Trade'] = message_field(1)


@dataclass
class GetMySubscriptions:
    pass


@dataclass
class GetClosePricesRequest:
    instruments: List['InstrumentClosePriceRequest'] = message_field(1)
    instrument_status: Optional['InstrumentStatus'] = message_field(9,
        optional=True)


@dataclass
class InstrumentClosePriceRequest:
    instrument_id: str = message_field(1)


@dataclass
class GetClosePricesResponse:
    close_prices: List['InstrumentClosePriceResponse'] = message_field(1)


@dataclass
class InstrumentClosePriceResponse:
    figi: str = message_field(1)
    instrument_uid: str = message_field(2)
    price: 'Quotation' = message_field(11)
    evening_session_price: 'Quotation' = message_field(12)
    time: datetime = message_field(21)
    evening_session_price_time: datetime = message_field(23)


@dataclass
class GetTechAnalysisRequest:
    indicator_type: 'IndicatorType' = message_field(1)
    instrument_uid: str = message_field(2)
    from_: datetime = message_field(3)
    to: datetime = message_field(4)
    interval: 'IndicatorInterval' = message_field(5)
    type_of_price: 'TypeOfPrice' = message_field(6)
    length: int = message_field(7)
    deviation: 'Deviation' = message_field(8)
    smoothing: 'Smoothing' = message_field(9)


    @dataclass
    class Smoothing:
        fast_length: int = message_field(1)
        slow_length: int = message_field(2)
        signal_smoothing: int = message_field(3)


    @dataclass
    class Deviation:
        deviation_multiplier: 'Quotation' = message_field(1)


    class IndicatorInterval(IntEnum):
        INDICATOR_INTERVAL_UNSPECIFIED = 0
        INDICATOR_INTERVAL_ONE_MINUTE = 1
        INDICATOR_INTERVAL_FIVE_MINUTES = 2
        INDICATOR_INTERVAL_FIFTEEN_MINUTES = 3
        INDICATOR_INTERVAL_ONE_HOUR = 4
        INDICATOR_INTERVAL_ONE_DAY = 5
        INDICATOR_INTERVAL_2_MIN = 6
        INDICATOR_INTERVAL_3_MIN = 7
        INDICATOR_INTERVAL_10_MIN = 8
        INDICATOR_INTERVAL_30_MIN = 9
        INDICATOR_INTERVAL_2_HOUR = 10
        INDICATOR_INTERVAL_4_HOUR = 11
        INDICATOR_INTERVAL_WEEK = 12
        INDICATOR_INTERVAL_MONTH = 13


    class TypeOfPrice(IntEnum):
        TYPE_OF_PRICE_UNSPECIFIED = 0
        TYPE_OF_PRICE_CLOSE = 1
        TYPE_OF_PRICE_OPEN = 2
        TYPE_OF_PRICE_HIGH = 3
        TYPE_OF_PRICE_LOW = 4
        TYPE_OF_PRICE_AVG = 5


    class IndicatorType(IntEnum):
        INDICATOR_TYPE_UNSPECIFIED = 0
        INDICATOR_TYPE_BB = 1
        INDICATOR_TYPE_EMA = 2
        INDICATOR_TYPE_RSI = 3
        INDICATOR_TYPE_MACD = 4
        INDICATOR_TYPE_SMA = 5


@dataclass
class GetTechAnalysisResponse:
    technical_indicators: List['TechAnalysisItem'] = message_field(1)


    @dataclass
    class TechAnalysisItem:
        timestamp: datetime = message_field(1)
        middle_band: Optional['Quotation'] = message_field(2, optional=True)
        upper_band: Optional['Quotation'] = message_field(3, optional=True)
        lower_band: Optional['Quotation'] = message_field(4, optional=True)
        signal: Optional['Quotation'] = message_field(5, optional=True)
        macd: Optional['Quotation'] = message_field(6, optional=True)


@dataclass
class GetMarketValuesRequest:
    instrument_id: List[str] = message_field(1)
    values: List['MarketValueType'] = message_field(2)


@dataclass
class GetMarketValuesResponse:
    instruments: List['MarketValueInstrument'] = message_field(1)


@dataclass
class MarketValueInstrument:
    instrument_uid: str = message_field(1)
    values: List['MarketValue'] = message_field(2)


@dataclass
class MarketValue:
    type: Optional['MarketValueType'] = message_field(1, optional=True)
    value: Optional['Quotation'] = message_field(2, optional=True)
    time: Optional[datetime] = message_field(3, optional=True)


class MarketValueType(IntEnum):
    INSTRUMENT_VALUE_UNSPECIFIED = 0
    INSTRUMENT_VALUE_LAST_PRICE = 1
    INSTRUMENT_VALUE_LAST_PRICE_DEALER = 2
    INSTRUMENT_VALUE_CLOSE_PRICE = 3
    INSTRUMENT_VALUE_EVENING_SESSION_PRICE = 4
    INSTRUMENT_VALUE_OPEN_INTEREST = 5
    INSTRUMENT_VALUE_THEOR_PRICE = 6


class OrderBookType(IntEnum):
    ORDERBOOK_TYPE_UNSPECIFIED = 0
    ORDERBOOK_TYPE_EXCHANGE = 1
    ORDERBOOK_TYPE_DEALER = 2
    ORDERBOOK_TYPE_ALL = 3


class LastPriceType(IntEnum):
    LAST_PRICE_UNSPECIFIED = 0
    LAST_PRICE_EXCHANGE = 1
    LAST_PRICE_DEALER = 2
