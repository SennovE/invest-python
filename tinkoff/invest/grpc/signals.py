from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import List, Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest._grpc_helpers import message_field
from tinkoff.invest.grpc import signals_pb2, signals_pb2_grpc
from tinkoff.invest.grpc.common import Page, PageResponse, Quotation
from tinkoff.invest.logging import get_tracking_id_from_call, log_request


class SignalService(BaseService):
    """//Сервис для получения технических сигналов и мнений аналитиков по инструментам."""
    _protobuf = signals_pb2
    _protobuf_grpc = signals_pb2_grpc
    _protobuf_stub = _protobuf_grpc.SignalServiceStub

    def get_strategies(self, request: 'GetStrategiesRequest'
        ) ->'GetStrategiesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetStrategiesRequest())
        response, call = self._stub.GetStrategies.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetStrategies')
        return protobuf_to_dataclass(response, GetStrategiesResponse)

    def get_signals(self, request: 'GetSignalsRequest') ->'GetSignalsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetSignalsRequest())
        response, call = self._stub.GetSignals.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSignals')
        return protobuf_to_dataclass(response, GetSignalsResponse)


@dataclass
class GetStrategiesRequest:
    strategy_id: Optional[str] = message_field(1, optional=True)


@dataclass
class GetStrategiesResponse:
    strategies: List['Strategy'] = message_field(1)


@dataclass
class Strategy:
    strategy_id: str = message_field(1)
    strategy_name: str = message_field(2)
    strategy_description: Optional[str] = message_field(3, optional=True)
    strategy_url: Optional[str] = message_field(4, optional=True)
    strategy_type: 'StrategyType' = message_field(5)
    active_signals: int = message_field(6)
    total_signals: int = message_field(7)
    time_in_position: int = message_field(8)
    average_signal_yield: 'Quotation' = message_field(9)
    average_signal_yield_year: 'Quotation' = message_field(10)
    yield_: 'Quotation' = message_field(11)
    yield_year: 'Quotation' = message_field(12)


@dataclass
class GetSignalsRequest:
    signal_id: Optional[str] = message_field(1, optional=True)
    strategy_id: Optional[str] = message_field(2, optional=True)
    strategy_type: Optional['StrategyType'] = message_field(3, optional=True)
    instrument_uid: Optional[str] = message_field(4, optional=True)
    from_: Optional[datetime] = message_field(5, optional=True)
    to: Optional[datetime] = message_field(6, optional=True)
    direction: Optional['SignalDirection'] = message_field(7, optional=True)
    active: Optional['SignalState'] = message_field(8, optional=True)
    paging: Optional['Page'] = message_field(9, optional=True)


@dataclass
class GetSignalsResponse:
    signals: List['Signal'] = message_field(1)
    paging: 'PageResponse' = message_field(2)


@dataclass
class Signal:
    signal_id: str = message_field(1)
    strategy_id: str = message_field(2)
    strategy_name: str = message_field(3)
    instrument_uid: str = message_field(4)
    create_dt: datetime = message_field(5)
    direction: 'SignalDirection' = message_field(6)
    initial_price: 'Quotation' = message_field(7)
    info: Optional[str] = message_field(8, optional=True)
    name: str = message_field(9)
    target_price: 'Quotation' = message_field(10)
    end_dt: datetime = message_field(11)
    probability: Optional[int] = message_field(12, optional=True)
    stoploss: Optional['Quotation'] = message_field(13, optional=True)
    close_price: Optional['Quotation'] = message_field(14, optional=True)
    close_dt: Optional[datetime] = message_field(15, optional=True)


class StrategyType(IntEnum):
    STRATEGY_TYPE_UNSPECIFIED = 0
    STRATEGY_TYPE_TECHNICAL = 1
    STRATEGY_TYPE_FUNDAMENTAL = 2


class SignalDirection(IntEnum):
    SIGNAL_DIRECTION_UNSPECIFIED = 0
    SIGNAL_DIRECTION_BUY = 1
    SIGNAL_DIRECTION_SELL = 2


class SignalState(IntEnum):
    SIGNAL_STATE_UNSPECIFIED = 0
    SIGNAL_STATE_ACTIVE = 1
    SIGNAL_STATE_CLOSED = 2
    SIGNAL_STATE_ALL = 3
