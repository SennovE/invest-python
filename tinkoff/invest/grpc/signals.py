from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import List, Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
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
    strategy_id: Optional[str] = None


@dataclass
class GetStrategiesResponse:
    strategies: List['Strategy']


@dataclass
class Strategy:
    strategy_id: str
    strategy_name: str
    strategy_type: 'StrategyType'
    active_signals: int
    total_signals: int
    time_in_position: int
    average_signal_yield: 'Quotation'
    average_signal_yield_year: 'Quotation'
    yield_: 'Quotation'
    yield_year: 'Quotation'
    strategy_description: Optional[str] = None
    strategy_url: Optional[str] = None


@dataclass
class GetSignalsRequest:
    signal_id: Optional[str] = None
    strategy_id: Optional[str] = None
    strategy_type: Optional['StrategyType'] = None
    instrument_uid: Optional[str] = None
    from_: Optional[datetime] = None
    to: Optional[datetime] = None
    direction: Optional['SignalDirection'] = None
    active: Optional['SignalState'] = None
    paging: Optional['Page'] = None


@dataclass
class GetSignalsResponse:
    signals: List['Signal']
    paging: 'PageResponse'


@dataclass
class Signal:
    signal_id: str
    strategy_id: str
    strategy_name: str
    instrument_uid: str
    create_dt: datetime
    direction: 'SignalDirection'
    initial_price: 'Quotation'
    name: str
    target_price: 'Quotation'
    end_dt: datetime
    info: Optional[str] = None
    probability: Optional[int] = None
    stoploss: Optional['Quotation'] = None
    close_price: Optional['Quotation'] = None
    close_dt: Optional[datetime] = None


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
