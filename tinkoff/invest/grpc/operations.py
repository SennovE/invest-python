from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import Iterable, List, Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest._grpc_helpers import message_field
from tinkoff.invest.grpc import operations_pb2, operations_pb2_grpc
from tinkoff.invest.grpc.common import (
    InstrumentType,
    MoneyValue,
    Ping,
    PingDelaySettings,
    Quotation,
)
from tinkoff.invest.logging import get_tracking_id_from_call, log_request


class OperationsService(BaseService):
    """/*С помощью методов сервиса можно получить:<br/><br/> **1**. Список операций по счету.<br/> **2**.
                              Портфель по счету.<br/> **3**. Позиции ценных бумаг на счете.<br/> **4**.
                              Доступный остаток для вывода средств.<br/> **5**. Различные отчеты.*/"""
    _protobuf = operations_pb2
    _protobuf_grpc = operations_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OperationsServiceStub

    def get_operations(self, request: 'OperationsRequest'
        ) ->'OperationsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            OperationsRequest())
        response, call = self._stub.GetOperations.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetOperations')
        return protobuf_to_dataclass(response, OperationsResponse)

    def get_portfolio(self, request: 'PortfolioRequest') ->'PortfolioResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PortfolioRequest())
        response, call = self._stub.GetPortfolio.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetPortfolio')
        return protobuf_to_dataclass(response, PortfolioResponse)

    def get_positions(self, request: 'PositionsRequest') ->'PositionsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PositionsRequest())
        response, call = self._stub.GetPositions.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetPositions')
        return protobuf_to_dataclass(response, PositionsResponse)

    def get_withdraw_limits(self, request: 'WithdrawLimitsRequest'
        ) ->'WithdrawLimitsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            WithdrawLimitsRequest())
        response, call = self._stub.GetWithdrawLimits.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetWithdrawLimits')
        return protobuf_to_dataclass(response, WithdrawLimitsResponse)

    def get_broker_report(self, request: 'BrokerReportRequest'
        ) ->'BrokerReportResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            BrokerReportRequest())
        response, call = self._stub.GetBrokerReport.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetBrokerReport')
        return protobuf_to_dataclass(response, BrokerReportResponse)

    def get_dividends_foreign_issuer(self, request:
        'GetDividendsForeignIssuerRequest'
        ) ->'GetDividendsForeignIssuerResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetDividendsForeignIssuerRequest())
        response, call = self._stub.GetDividendsForeignIssuer.with_call(request
            =protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call),
            'GetDividendsForeignIssuer')
        return protobuf_to_dataclass(response,
            GetDividendsForeignIssuerResponse)

    def get_operations_by_cursor(self, request: 'GetOperationsByCursorRequest'
        ) ->'GetOperationsByCursorResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOperationsByCursorRequest())
        response, call = self._stub.GetOperationsByCursor.with_call(request
            =protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetOperationsByCursor')
        return protobuf_to_dataclass(response, GetOperationsByCursorResponse)


class OperationsStreamService(BaseService):
    """//PortfolioStream — стрим обновлений портфеля"""
    _protobuf = operations_pb2
    _protobuf_grpc = operations_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OperationsStreamServiceStub

    def portfolio_stream(self, request: 'PortfolioStreamRequest') ->Iterable[
        'PortfolioStreamResponse']:
        for response in self._stub.PortfolioStream(request=
            dataclass_to_protobuf(request, self._protobuf.
            PortfolioStreamRequest()), metadata=self._metadata):
            yield protobuf_to_dataclass(response, PortfolioStreamResponse)

    def positions_stream(self, request: 'PositionsStreamRequest') ->Iterable[
        'PositionsStreamResponse']:
        for response in self._stub.PositionsStream(request=
            dataclass_to_protobuf(request, self._protobuf.
            PositionsStreamRequest()), metadata=self._metadata):
            yield protobuf_to_dataclass(response, PositionsStreamResponse)


@dataclass
class OperationsRequest:
    account_id: str = message_field(1)
    from_: Optional[datetime] = message_field(2, optional=True)
    to: Optional[datetime] = message_field(3, optional=True)
    state: Optional['OperationState'] = message_field(4, optional=True)
    figi: Optional[str] = message_field(5, optional=True)


@dataclass
class OperationsResponse:
    operations: List['Operation'] = message_field(1)


@dataclass
class Operation:
    id: str = message_field(1)
    parent_operation_id: str = message_field(2)
    currency: str = message_field(3)
    payment: 'MoneyValue' = message_field(4)
    price: 'MoneyValue' = message_field(5)
    state: 'OperationState' = message_field(6)
    quantity: int = message_field(7)
    quantity_rest: int = message_field(8)
    figi: str = message_field(9)
    instrument_type: str = message_field(10)
    date: datetime = message_field(11)
    type: str = message_field(12)
    operation_type: 'OperationType' = message_field(13)
    trades: List['OperationTrade'] = message_field(14)
    asset_uid: str = message_field(16)
    position_uid: str = message_field(17)
    instrument_uid: str = message_field(18)
    child_operations: List['ChildOperationItem'] = message_field(19)


@dataclass
class OperationTrade:
    trade_id: str = message_field(1)
    date_time: datetime = message_field(2)
    quantity: int = message_field(3)
    price: 'MoneyValue' = message_field(4)


@dataclass
class PortfolioRequest:
    account_id: str = message_field(1)
    currency: Optional['CurrencyRequest'] = message_field(2, optional=True)


    class CurrencyRequest(IntEnum):
        RUB = 0
        USD = 1
        EUR = 2


@dataclass
class PortfolioResponse:
    total_amount_shares: 'MoneyValue' = message_field(1)
    total_amount_bonds: 'MoneyValue' = message_field(2)
    total_amount_etf: 'MoneyValue' = message_field(3)
    total_amount_currencies: 'MoneyValue' = message_field(4)
    total_amount_futures: 'MoneyValue' = message_field(5)
    expected_yield: 'Quotation' = message_field(6)
    positions: List['PortfolioPosition'] = message_field(7)
    account_id: str = message_field(8)
    total_amount_options: 'MoneyValue' = message_field(9)
    total_amount_sp: 'MoneyValue' = message_field(10)
    total_amount_portfolio: 'MoneyValue' = message_field(11)
    virtual_positions: List['VirtualPortfolioPosition'] = message_field(12)
    daily_yield: 'MoneyValue' = message_field(15)
    daily_yield_relative: 'Quotation' = message_field(16)


@dataclass
class PositionsRequest:
    account_id: str = message_field(1)


@dataclass
class PositionsResponse:
    money: List['MoneyValue'] = message_field(1)
    blocked: List['MoneyValue'] = message_field(2)
    securities: List['PositionsSecurities'] = message_field(3)
    limits_loading_in_progress: bool = message_field(4)
    futures: List['PositionsFutures'] = message_field(5)
    options: List['PositionsOptions'] = message_field(6)
    account_id: str = message_field(15)


@dataclass
class WithdrawLimitsRequest:
    account_id: str = message_field(1)


@dataclass
class WithdrawLimitsResponse:
    money: List['MoneyValue'] = message_field(1)
    blocked: List['MoneyValue'] = message_field(2)
    blocked_guarantee: List['MoneyValue'] = message_field(3)


@dataclass
class PortfolioPosition:
    figi: str = message_field(1)
    instrument_type: str = message_field(2)
    quantity: 'Quotation' = message_field(3)
    average_position_price: 'MoneyValue' = message_field(4)
    expected_yield: 'Quotation' = message_field(5)
    current_nkd: 'MoneyValue' = message_field(6)
    average_position_price_pt: 'Quotation' = message_field(7)
    current_price: 'MoneyValue' = message_field(8)
    average_position_price_fifo: 'MoneyValue' = message_field(9)
    quantity_lots: 'Quotation' = message_field(10)
    blocked: bool = message_field(21)
    blocked_lots: 'Quotation' = message_field(22)
    position_uid: str = message_field(24)
    instrument_uid: str = message_field(25)
    var_margin: 'MoneyValue' = message_field(26)
    expected_yield_fifo: 'Quotation' = message_field(27)
    daily_yield: 'MoneyValue' = message_field(31)
    ticker: str = message_field(32)


@dataclass
class VirtualPortfolioPosition:
    position_uid: str = message_field(1)
    instrument_uid: str = message_field(2)
    figi: str = message_field(3)
    instrument_type: str = message_field(4)
    quantity: 'Quotation' = message_field(5)
    average_position_price: 'MoneyValue' = message_field(6)
    expected_yield: 'Quotation' = message_field(7)
    expected_yield_fifo: 'Quotation' = message_field(8)
    expire_date: datetime = message_field(9)
    current_price: 'MoneyValue' = message_field(10)
    average_position_price_fifo: 'MoneyValue' = message_field(11)
    daily_yield: 'MoneyValue' = message_field(31)
    ticker: str = message_field(32)


@dataclass
class PositionsSecurities:
    figi: str = message_field(1)
    blocked: int = message_field(2)
    balance: int = message_field(3)
    position_uid: str = message_field(4)
    instrument_uid: str = message_field(5)
    ticker: str = message_field(6)
    exchange_blocked: bool = message_field(11)
    instrument_type: str = message_field(16)


@dataclass
class PositionsFutures:
    figi: str = message_field(1)
    blocked: int = message_field(2)
    balance: int = message_field(3)
    position_uid: str = message_field(4)
    instrument_uid: str = message_field(5)
    ticker: str = message_field(6)


@dataclass
class PositionsOptions:
    position_uid: str = message_field(1)
    instrument_uid: str = message_field(2)
    ticker: str = message_field(3)
    blocked: int = message_field(11)
    balance: int = message_field(21)


@dataclass
class BrokerReportRequest:
    generate_broker_report_request: Optional['GenerateBrokerReportRequest'
        ] = message_field(1, optional=True)
    get_broker_report_request: Optional['GetBrokerReportRequest'
        ] = message_field(2, optional=True)


@dataclass
class BrokerReportResponse:
    generate_broker_report_response: Optional['GenerateBrokerReportResponse'
        ] = message_field(1, optional=True)
    get_broker_report_response: Optional['GetBrokerReportResponse'
        ] = message_field(2, optional=True)


@dataclass
class GenerateBrokerReportRequest:
    account_id: str = message_field(1)
    from_: datetime = message_field(2)
    to: datetime = message_field(3)


@dataclass
class GenerateBrokerReportResponse:
    task_id: str = message_field(1)


@dataclass
class GetBrokerReportRequest:
    task_id: str = message_field(1)
    page: Optional[int] = message_field(2, optional=True)


@dataclass
class GetBrokerReportResponse:
    broker_report: List['BrokerReport'] = message_field(1)
    itemsCount: int = message_field(2)
    pagesCount: int = message_field(3)
    page: int = message_field(4)


@dataclass
class BrokerReport:
    trade_id: str = message_field(1)
    order_id: str = message_field(2)
    figi: str = message_field(3)
    execute_sign: str = message_field(4)
    trade_datetime: datetime = message_field(5)
    exchange: str = message_field(6)
    class_code: str = message_field(7)
    direction: str = message_field(8)
    name: str = message_field(9)
    ticker: str = message_field(10)
    price: 'MoneyValue' = message_field(11)
    quantity: int = message_field(12)
    order_amount: 'MoneyValue' = message_field(13)
    aci_value: 'Quotation' = message_field(14)
    total_order_amount: 'MoneyValue' = message_field(15)
    broker_commission: 'MoneyValue' = message_field(16)
    exchange_commission: 'MoneyValue' = message_field(17)
    exchange_clearing_commission: 'MoneyValue' = message_field(18)
    repo_rate: 'Quotation' = message_field(19)
    party: str = message_field(20)
    clear_value_date: datetime = message_field(21)
    sec_value_date: datetime = message_field(22)
    broker_status: str = message_field(23)
    separate_agreement_type: str = message_field(24)
    separate_agreement_number: str = message_field(25)
    separate_agreement_date: str = message_field(26)
    delivery_type: str = message_field(27)


class OperationState(IntEnum):
    OPERATION_STATE_UNSPECIFIED = 0
    OPERATION_STATE_EXECUTED = 1
    OPERATION_STATE_CANCELED = 2
    OPERATION_STATE_PROGRESS = 3


class OperationType(IntEnum):
    OPERATION_TYPE_UNSPECIFIED = 0
    OPERATION_TYPE_INPUT = 1
    OPERATION_TYPE_BOND_TAX = 2
    OPERATION_TYPE_OUTPUT_SECURITIES = 3
    OPERATION_TYPE_OVERNIGHT = 4
    OPERATION_TYPE_TAX = 5
    OPERATION_TYPE_BOND_REPAYMENT_FULL = 6
    OPERATION_TYPE_SELL_CARD = 7
    OPERATION_TYPE_DIVIDEND_TAX = 8
    OPERATION_TYPE_OUTPUT = 9
    OPERATION_TYPE_BOND_REPAYMENT = 10
    OPERATION_TYPE_TAX_CORRECTION = 11
    OPERATION_TYPE_SERVICE_FEE = 12
    OPERATION_TYPE_BENEFIT_TAX = 13
    OPERATION_TYPE_MARGIN_FEE = 14
    OPERATION_TYPE_BUY = 15
    OPERATION_TYPE_BUY_CARD = 16
    OPERATION_TYPE_INPUT_SECURITIES = 17
    OPERATION_TYPE_SELL_MARGIN = 18
    OPERATION_TYPE_BROKER_FEE = 19
    OPERATION_TYPE_BUY_MARGIN = 20
    OPERATION_TYPE_DIVIDEND = 21
    OPERATION_TYPE_SELL = 22
    OPERATION_TYPE_COUPON = 23
    OPERATION_TYPE_SUCCESS_FEE = 24
    OPERATION_TYPE_DIVIDEND_TRANSFER = 25
    OPERATION_TYPE_ACCRUING_VARMARGIN = 26
    OPERATION_TYPE_WRITING_OFF_VARMARGIN = 27
    OPERATION_TYPE_DELIVERY_BUY = 28
    OPERATION_TYPE_DELIVERY_SELL = 29
    OPERATION_TYPE_TRACK_MFEE = 30
    OPERATION_TYPE_TRACK_PFEE = 31
    OPERATION_TYPE_TAX_PROGRESSIVE = 32
    OPERATION_TYPE_BOND_TAX_PROGRESSIVE = 33
    OPERATION_TYPE_DIVIDEND_TAX_PROGRESSIVE = 34
    OPERATION_TYPE_BENEFIT_TAX_PROGRESSIVE = 35
    OPERATION_TYPE_TAX_CORRECTION_PROGRESSIVE = 36
    OPERATION_TYPE_TAX_REPO_PROGRESSIVE = 37
    OPERATION_TYPE_TAX_REPO = 38
    OPERATION_TYPE_TAX_REPO_HOLD = 39
    OPERATION_TYPE_TAX_REPO_REFUND = 40
    OPERATION_TYPE_TAX_REPO_HOLD_PROGRESSIVE = 41
    OPERATION_TYPE_TAX_REPO_REFUND_PROGRESSIVE = 42
    OPERATION_TYPE_DIV_EXT = 43
    OPERATION_TYPE_TAX_CORRECTION_COUPON = 44
    OPERATION_TYPE_CASH_FEE = 45
    OPERATION_TYPE_OUT_FEE = 46
    OPERATION_TYPE_OUT_STAMP_DUTY = 47
    OPERATION_TYPE_OUTPUT_SWIFT = 50
    OPERATION_TYPE_INPUT_SWIFT = 51
    OPERATION_TYPE_OUTPUT_ACQUIRING = 53
    OPERATION_TYPE_INPUT_ACQUIRING = 54
    OPERATION_TYPE_OUTPUT_PENALTY = 55
    OPERATION_TYPE_ADVICE_FEE = 56
    OPERATION_TYPE_TRANS_IIS_BS = 57
    OPERATION_TYPE_TRANS_BS_BS = 58
    OPERATION_TYPE_OUT_MULTI = 59
    OPERATION_TYPE_INP_MULTI = 60
    OPERATION_TYPE_OVER_PLACEMENT = 61
    OPERATION_TYPE_OVER_COM = 62
    OPERATION_TYPE_OVER_INCOME = 63
    OPERATION_TYPE_OPTION_EXPIRATION = 64
    OPERATION_TYPE_FUTURE_EXPIRATION = 65


@dataclass
class GetDividendsForeignIssuerRequest:
    generate_div_foreign_issuer_report: Optional[
        'GenerateDividendsForeignIssuerReportRequest'] = message_field(1,
        optional=True)
    get_div_foreign_issuer_report: Optional[
        'GetDividendsForeignIssuerReportRequest'] = message_field(2,
        optional=True)


@dataclass
class GetDividendsForeignIssuerResponse:
    generate_div_foreign_issuer_report_response: Optional[
        'GenerateDividendsForeignIssuerReportResponse'] = message_field(1,
        optional=True)
    div_foreign_issuer_report: Optional[
        'GetDividendsForeignIssuerReportResponse'] = message_field(2,
        optional=True)


@dataclass
class GenerateDividendsForeignIssuerReportRequest:
    account_id: str = message_field(1)
    from_: datetime = message_field(2)
    to: datetime = message_field(3)


@dataclass
class GetDividendsForeignIssuerReportRequest:
    task_id: str = message_field(1)
    page: Optional[int] = message_field(2, optional=True)


@dataclass
class GenerateDividendsForeignIssuerReportResponse:
    task_id: str = message_field(1)


@dataclass
class GetDividendsForeignIssuerReportResponse:
    dividends_foreign_issuer_report: List['DividendsForeignIssuerReport'
        ] = message_field(1)
    itemsCount: int = message_field(2)
    pagesCount: int = message_field(3)
    page: int = message_field(4)


@dataclass
class DividendsForeignIssuerReport:
    record_date: datetime = message_field(1)
    payment_date: datetime = message_field(2)
    security_name: str = message_field(3)
    isin: str = message_field(4)
    issuer_country: str = message_field(5)
    quantity: int = message_field(6)
    dividend: 'Quotation' = message_field(7)
    external_commission: 'Quotation' = message_field(8)
    dividend_gross: 'Quotation' = message_field(9)
    tax: 'Quotation' = message_field(10)
    dividend_amount: 'Quotation' = message_field(11)
    currency: str = message_field(12)


@dataclass
class PortfolioStreamRequest:
    accounts: List[str] = message_field(1)
    ping_settings: 'PingDelaySettings' = message_field(15)


@dataclass
class PortfolioStreamResponse:
    subscriptions: Optional['PortfolioSubscriptionResult'] = message_field(
        1, optional=True)
    portfolio: Optional['PortfolioResponse'] = message_field(2, optional=True)
    ping: Optional['Ping'] = message_field(3, optional=True)


@dataclass
class PortfolioSubscriptionResult:
    accounts: List['AccountSubscriptionStatus'] = message_field(1)
    tracking_id: str = message_field(7)
    stream_id: str = message_field(8)


@dataclass
class AccountSubscriptionStatus:
    account_id: str = message_field(1)
    subscription_status: 'PortfolioSubscriptionStatus' = message_field(6)


class PortfolioSubscriptionStatus(IntEnum):
    PORTFOLIO_SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    PORTFOLIO_SUBSCRIPTION_STATUS_SUCCESS = 1
    PORTFOLIO_SUBSCRIPTION_STATUS_ACCOUNT_NOT_FOUND = 2
    PORTFOLIO_SUBSCRIPTION_STATUS_INTERNAL_ERROR = 3


@dataclass
class GetOperationsByCursorRequest:
    account_id: str = message_field(1)
    instrument_id: Optional[str] = message_field(2, optional=True)
    from_: Optional[datetime] = message_field(6, optional=True)
    to: Optional[datetime] = message_field(7, optional=True)
    cursor: Optional[str] = message_field(11, optional=True)
    limit: Optional[int] = message_field(12, optional=True)
    operation_types: List['OperationType'] = message_field(13)
    state: Optional['OperationState'] = message_field(14, optional=True)
    without_commissions: Optional[bool] = message_field(15, optional=True)
    without_trades: Optional[bool] = message_field(16, optional=True)
    without_overnights: Optional[bool] = message_field(17, optional=True)


@dataclass
class GetOperationsByCursorResponse:
    has_next: bool = message_field(1)
    next_cursor: str = message_field(2)
    items: List['OperationItem'] = message_field(6)


@dataclass
class OperationItem:
    cursor: str = message_field(1)
    broker_account_id: str = message_field(6)
    id: str = message_field(16)
    parent_operation_id: str = message_field(17)
    name: str = message_field(18)
    date: datetime = message_field(21)
    type: 'OperationType' = message_field(22)
    description: str = message_field(23)
    state: 'OperationState' = message_field(24)
    instrument_uid: str = message_field(31)
    figi: str = message_field(32)
    instrument_type: str = message_field(33)
    instrument_kind: 'InstrumentType' = message_field(34)
    position_uid: str = message_field(35)
    payment: 'MoneyValue' = message_field(41)
    price: 'MoneyValue' = message_field(42)
    commission: 'MoneyValue' = message_field(43)
    yield_: 'MoneyValue' = message_field(44)
    yield_relative: 'Quotation' = message_field(45)
    accrued_int: 'MoneyValue' = message_field(46)
    quantity: int = message_field(51)
    quantity_rest: int = message_field(52)
    quantity_done: int = message_field(53)
    cancel_date_time: datetime = message_field(56)
    cancel_reason: str = message_field(57)
    trades_info: 'OperationItemTrades' = message_field(61)
    asset_uid: str = message_field(64)
    child_operations: List['ChildOperationItem'] = message_field(65)


@dataclass
class OperationItemTrades:
    trades: List['OperationItemTrade'] = message_field(6)


@dataclass
class OperationItemTrade:
    num: str = message_field(1)
    date: datetime = message_field(6)
    quantity: int = message_field(11)
    price: 'MoneyValue' = message_field(16)
    yield_: 'MoneyValue' = message_field(21)
    yield_relative: 'Quotation' = message_field(22)


@dataclass
class PositionsStreamRequest:
    accounts: List[str] = message_field(1)
    with_initial_positions: bool = message_field(3)
    ping_settings: 'PingDelaySettings' = message_field(15)


@dataclass
class PositionsStreamResponse:
    subscriptions: Optional['PositionsSubscriptionResult'] = message_field(
        1, optional=True)
    position: Optional['PositionData'] = message_field(2, optional=True)
    ping: Optional['Ping'] = message_field(3, optional=True)
    initial_positions: Optional['PositionsResponse'] = message_field(5,
        optional=True)


@dataclass
class PositionsSubscriptionResult:
    accounts: List['PositionsSubscriptionStatus'] = message_field(1)
    tracking_id: str = message_field(7)
    stream_id: str = message_field(8)


@dataclass
class PositionsSubscriptionStatus:
    account_id: str = message_field(1)
    subscription_status: 'PositionsAccountSubscriptionStatus' = message_field(6
        )


class PositionsAccountSubscriptionStatus(IntEnum):
    POSITIONS_SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    POSITIONS_SUBSCRIPTION_STATUS_SUCCESS = 1
    POSITIONS_SUBSCRIPTION_STATUS_ACCOUNT_NOT_FOUND = 2
    POSITIONS_SUBSCRIPTION_STATUS_INTERNAL_ERROR = 3


@dataclass
class PositionData:
    account_id: str = message_field(1)
    money: List['PositionsMoney'] = message_field(2)
    securities: List['PositionsSecurities'] = message_field(3)
    futures: List['PositionsFutures'] = message_field(4)
    options: List['PositionsOptions'] = message_field(5)
    date: datetime = message_field(6)


@dataclass
class PositionsMoney:
    available_value: 'MoneyValue' = message_field(1)
    blocked_value: 'MoneyValue' = message_field(2)


@dataclass
class ChildOperationItem:
    instrument_uid: str = message_field(1)
    payment: 'MoneyValue' = message_field(2)
