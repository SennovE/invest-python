from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import List, Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest._grpc_helpers import message_field
from tinkoff.invest.grpc import instruments_pb2, instruments_pb2_grpc
from tinkoff.invest.grpc.common import (
    BrandData,
    InstrumentStatus,
    InstrumentType,
    MoneyValue,
    Page,
    PageResponse,
    Quotation,
    RealExchange,
    SecurityTradingStatus,
)
from tinkoff.invest.logging import get_tracking_id_from_call, log_request


class InstrumentsService(BaseService):
    """/*Методы сервиса предназначены для получения:<br/>1. Информации об инструментах.<br/>2.
                            Расписания торговых сессий.<br/>3. Календаря выплат купонов по облигациям.<br/>4.
                            Размера гарантийного обеспечения по фьючерсам.<br/>5. Дивидендов по ценной бумаге.*/"""
    _protobuf = instruments_pb2
    _protobuf_grpc = instruments_pb2_grpc
    _protobuf_stub = _protobuf_grpc.InstrumentsServiceStub

    def trading_schedules(self, request: 'TradingSchedulesRequest'
        ) ->'TradingSchedulesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            TradingSchedulesRequest())
        response, call = self._stub.TradingSchedules.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'TradingSchedules')
        return protobuf_to_dataclass(response, TradingSchedulesResponse)

    def bond_by(self, request: 'InstrumentRequest') ->'BondResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.BondBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'BondBy')
        return protobuf_to_dataclass(response, BondResponse)

    def bonds(self, request: 'InstrumentsRequest') ->'BondsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Bonds.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'Bonds')
        return protobuf_to_dataclass(response, BondsResponse)

    def get_bond_coupons(self, request: 'GetBondCouponsRequest'
        ) ->'GetBondCouponsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetBondCouponsRequest())
        response, call = self._stub.GetBondCoupons.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetBondCoupons')
        return protobuf_to_dataclass(response, GetBondCouponsResponse)

    def get_bond_events(self, request: 'GetBondEventsRequest'
        ) ->'GetBondEventsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetBondEventsRequest())
        response, call = self._stub.GetBondEvents.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetBondEvents')
        return protobuf_to_dataclass(response, GetBondEventsResponse)

    def currency_by(self, request: 'InstrumentRequest') ->'CurrencyResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.CurrencyBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'CurrencyBy')
        return protobuf_to_dataclass(response, CurrencyResponse)

    def currencies(self, request: 'InstrumentsRequest') ->'CurrenciesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Currencies.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'Currencies')
        return protobuf_to_dataclass(response, CurrenciesResponse)

    def etf_by(self, request: 'InstrumentRequest') ->'EtfResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.EtfBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'EtfBy')
        return protobuf_to_dataclass(response, EtfResponse)

    def etfs(self, request: 'InstrumentsRequest') ->'EtfsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Etfs.with_call(request=protobuf_request,
            metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'Etfs')
        return protobuf_to_dataclass(response, EtfsResponse)

    def future_by(self, request: 'InstrumentRequest') ->'FutureResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.FutureBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'FutureBy')
        return protobuf_to_dataclass(response, FutureResponse)

    def futures(self, request: 'InstrumentsRequest') ->'FuturesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Futures.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'Futures')
        return protobuf_to_dataclass(response, FuturesResponse)

    def option_by(self, request: 'InstrumentRequest') ->'OptionResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.OptionBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'OptionBy')
        return protobuf_to_dataclass(response, OptionResponse)

    def options(self, request: 'InstrumentsRequest') ->'OptionsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Options.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'Options')
        return protobuf_to_dataclass(response, OptionsResponse)

    def options_by(self, request: 'FilterOptionsRequest') ->'OptionsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            FilterOptionsRequest())
        response, call = self._stub.OptionsBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'OptionsBy')
        return protobuf_to_dataclass(response, OptionsResponse)

    def share_by(self, request: 'InstrumentRequest') ->'ShareResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.ShareBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'ShareBy')
        return protobuf_to_dataclass(response, ShareResponse)

    def shares(self, request: 'InstrumentsRequest') ->'SharesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Shares.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'Shares')
        return protobuf_to_dataclass(response, SharesResponse)

    def indicatives(self, request: 'IndicativesRequest'
        ) ->'IndicativesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            IndicativesRequest())
        response, call = self._stub.Indicatives.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'Indicatives')
        return protobuf_to_dataclass(response, IndicativesResponse)

    def get_accrued_interests(self, request: 'GetAccruedInterestsRequest'
        ) ->'GetAccruedInterestsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccruedInterestsRequest())
        response, call = self._stub.GetAccruedInterests.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetAccruedInterests')
        return protobuf_to_dataclass(response, GetAccruedInterestsResponse)

    def get_futures_margin(self, request: 'GetFuturesMarginRequest'
        ) ->'GetFuturesMarginResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetFuturesMarginRequest())
        response, call = self._stub.GetFuturesMargin.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetFuturesMargin')
        return protobuf_to_dataclass(response, GetFuturesMarginResponse)

    def get_instrument_by(self, request: 'InstrumentRequest'
        ) ->'InstrumentResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.GetInstrumentBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetInstrumentBy')
        return protobuf_to_dataclass(response, InstrumentResponse)

    def get_dividends(self, request: 'GetDividendsRequest'
        ) ->'GetDividendsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetDividendsRequest())
        response, call = self._stub.GetDividends.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetDividends')
        return protobuf_to_dataclass(response, GetDividendsResponse)

    def get_asset_by(self, request: 'AssetRequest') ->'AssetResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            AssetRequest())
        response, call = self._stub.GetAssetBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetAssetBy')
        return protobuf_to_dataclass(response, AssetResponse)

    def get_assets(self, request: 'AssetsRequest') ->'AssetsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            AssetsRequest())
        response, call = self._stub.GetAssets.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetAssets')
        return protobuf_to_dataclass(response, AssetsResponse)

    def get_favorites(self, request: 'GetFavoritesRequest'
        ) ->'GetFavoritesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetFavoritesRequest())
        response, call = self._stub.GetFavorites.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetFavorites')
        return protobuf_to_dataclass(response, GetFavoritesResponse)

    def edit_favorites(self, request: 'EditFavoritesRequest'
        ) ->'EditFavoritesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            EditFavoritesRequest())
        response, call = self._stub.EditFavorites.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'EditFavorites')
        return protobuf_to_dataclass(response, EditFavoritesResponse)

    def create_favorite_group(self, request: 'CreateFavoriteGroupRequest'
        ) ->'CreateFavoriteGroupResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CreateFavoriteGroupRequest())
        response, call = self._stub.CreateFavoriteGroup.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'CreateFavoriteGroup')
        return protobuf_to_dataclass(response, CreateFavoriteGroupResponse)

    def delete_favorite_group(self, request: 'DeleteFavoriteGroupRequest'
        ) ->'DeleteFavoriteGroupResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            DeleteFavoriteGroupRequest())
        response, call = self._stub.DeleteFavoriteGroup.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'DeleteFavoriteGroup')
        return protobuf_to_dataclass(response, DeleteFavoriteGroupResponse)

    def get_favorite_groups(self, request: 'GetFavoriteGroupsRequest'
        ) ->'GetFavoriteGroupsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetFavoriteGroupsRequest())
        response, call = self._stub.GetFavoriteGroups.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetFavoriteGroups')
        return protobuf_to_dataclass(response, GetFavoriteGroupsResponse)

    def get_countries(self, request: 'GetCountriesRequest'
        ) ->'GetCountriesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetCountriesRequest())
        response, call = self._stub.GetCountries.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetCountries')
        return protobuf_to_dataclass(response, GetCountriesResponse)

    def find_instrument(self, request: 'FindInstrumentRequest'
        ) ->'FindInstrumentResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            FindInstrumentRequest())
        response, call = self._stub.FindInstrument.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'FindInstrument')
        return protobuf_to_dataclass(response, FindInstrumentResponse)

    def get_brands(self, request: 'GetBrandsRequest') ->'GetBrandsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetBrandsRequest())
        response, call = self._stub.GetBrands.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetBrands')
        return protobuf_to_dataclass(response, GetBrandsResponse)

    def get_brand_by(self, request: 'GetBrandRequest') ->'Brand':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetBrandRequest())
        response, call = self._stub.GetBrandBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetBrandBy')
        return protobuf_to_dataclass(response, Brand)

    def get_asset_fundamentals(self, request: 'GetAssetFundamentalsRequest'
        ) ->'GetAssetFundamentalsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAssetFundamentalsRequest())
        response, call = self._stub.GetAssetFundamentals.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetAssetFundamentals')
        return protobuf_to_dataclass(response, GetAssetFundamentalsResponse)

    def get_asset_reports(self, request: 'GetAssetReportsRequest'
        ) ->'GetAssetReportsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAssetReportsRequest())
        response, call = self._stub.GetAssetReports.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetAssetReports')
        return protobuf_to_dataclass(response, GetAssetReportsResponse)

    def get_consensus_forecasts(self, request: 'GetConsensusForecastsRequest'
        ) ->'GetConsensusForecastsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetConsensusForecastsRequest())
        response, call = self._stub.GetConsensusForecasts.with_call(request
            =protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetConsensusForecasts')
        return protobuf_to_dataclass(response, GetConsensusForecastsResponse)

    def get_forecast_by(self, request: 'GetForecastRequest'
        ) ->'GetForecastResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetForecastRequest())
        response, call = self._stub.GetForecastBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetForecastBy')
        return protobuf_to_dataclass(response, GetForecastResponse)

    def get_risk_rates(self, request: 'RiskRatesRequest'
        ) ->'RiskRatesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            RiskRatesRequest())
        response, call = self._stub.GetRiskRates.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetRiskRates')
        return protobuf_to_dataclass(response, RiskRatesResponse)

    def get_insider_deals(self, request: 'GetInsiderDealsRequest'
        ) ->'GetInsiderDealsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetInsiderDealsRequest())
        response, call = self._stub.GetInsiderDeals.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetInsiderDeals')
        return protobuf_to_dataclass(response, GetInsiderDealsResponse)


@dataclass
class TradingSchedulesRequest:
    exchange: Optional[str] = message_field(1, optional=True)
    from_: Optional[datetime] = message_field(2, optional=True)
    to: Optional[datetime] = message_field(3, optional=True)


@dataclass
class TradingSchedulesResponse:
    exchanges: List['TradingSchedule'] = message_field(1)


@dataclass
class TradingSchedule:
    exchange: str = message_field(1)
    days: List['TradingDay'] = message_field(2)


@dataclass
class TradingDay:
    date: datetime = message_field(1)
    is_trading_day: bool = message_field(2)
    start_time: datetime = message_field(3)
    end_time: datetime = message_field(4)
    opening_auction_start_time: datetime = message_field(7)
    closing_auction_end_time: datetime = message_field(8)
    evening_opening_auction_start_time: datetime = message_field(9)
    evening_start_time: datetime = message_field(10)
    evening_end_time: datetime = message_field(11)
    clearing_start_time: datetime = message_field(12)
    clearing_end_time: datetime = message_field(13)
    premarket_start_time: datetime = message_field(14)
    premarket_end_time: datetime = message_field(15)
    closing_auction_start_time: datetime = message_field(16)
    opening_auction_end_time: datetime = message_field(17)
    intervals: List['TradingInterval'] = message_field(18)


@dataclass
class InstrumentRequest:
    id_type: 'InstrumentIdType' = message_field(1)
    class_code: Optional[str] = message_field(2, optional=True)
    id: str = message_field(3)


@dataclass
class InstrumentsRequest:
    instrument_status: Optional['InstrumentStatus'] = message_field(1,
        optional=True)
    instrument_exchange: Optional['InstrumentExchangeType'] = message_field(
        2, optional=True)


@dataclass
class FilterOptionsRequest:
    basic_asset_uid: Optional[str] = message_field(1, optional=True)
    basic_asset_position_uid: Optional[str] = message_field(2, optional=True)


@dataclass
class BondResponse:
    instrument: 'Bond' = message_field(1)


@dataclass
class BondsResponse:
    instruments: List['Bond'] = message_field(1)


@dataclass
class GetBondCouponsRequest:
    figi: str = message_field(1)
    from_: Optional[datetime] = message_field(2, optional=True)
    to: Optional[datetime] = message_field(3, optional=True)
    instrument_id: str = message_field(4)


@dataclass
class GetBondCouponsResponse:
    events: List['Coupon'] = message_field(1)


@dataclass
class GetBondEventsRequest:
    from_: Optional[datetime] = message_field(2, optional=True)
    to: Optional[datetime] = message_field(3, optional=True)
    instrument_id: str = message_field(4)
    type: 'EventType' = message_field(5)


    class EventType(IntEnum):
        EVENT_TYPE_UNSPECIFIED = 0
        EVENT_TYPE_CPN = 1
        EVENT_TYPE_CALL = 2
        EVENT_TYPE_MTY = 3
        EVENT_TYPE_CONV = 4


@dataclass
class GetBondEventsResponse:
    events: List['BondEvent'] = message_field(1)


    @dataclass
    class BondEvent:
        instrument_id: str = message_field(2)
        event_number: int = message_field(3)
        event_date: datetime = message_field(4)
        event_type: 'GetBondEventsRequest.EventType' = message_field(5)
        event_total_vol: 'Quotation' = message_field(6)
        fix_date: datetime = message_field(7)
        rate_date: datetime = message_field(8)
        default_date: datetime = message_field(9)
        real_pay_date: datetime = message_field(10)
        pay_date: datetime = message_field(11)
        pay_one_bond: 'MoneyValue' = message_field(12)
        money_flow_val: 'MoneyValue' = message_field(13)
        execution: str = message_field(14)
        operation_type: str = message_field(15)
        value: 'Quotation' = message_field(16)
        note: str = message_field(17)
        convert_to_fin_tool_id: str = message_field(18)
        coupon_start_date: datetime = message_field(19)
        coupon_end_date: datetime = message_field(20)
        coupon_period: int = message_field(21)
        coupon_interest_rate: 'Quotation' = message_field(22)


@dataclass
class Coupon:
    figi: str = message_field(1)
    coupon_date: datetime = message_field(2)
    coupon_number: int = message_field(3)
    fix_date: datetime = message_field(4)
    pay_one_bond: 'MoneyValue' = message_field(5)
    coupon_type: 'CouponType' = message_field(6)
    coupon_start_date: datetime = message_field(7)
    coupon_end_date: datetime = message_field(8)
    coupon_period: int = message_field(9)


class CouponType(IntEnum):
    COUPON_TYPE_UNSPECIFIED = 0
    COUPON_TYPE_CONSTANT = 1
    COUPON_TYPE_FLOATING = 2
    COUPON_TYPE_DISCOUNT = 3
    COUPON_TYPE_MORTGAGE = 4
    COUPON_TYPE_FIX = 5
    COUPON_TYPE_VARIABLE = 6
    COUPON_TYPE_OTHER = 7


@dataclass
class CurrencyResponse:
    instrument: 'Currency' = message_field(1)


@dataclass
class CurrenciesResponse:
    instruments: List['Currency'] = message_field(1)


@dataclass
class EtfResponse:
    instrument: 'Etf' = message_field(1)


@dataclass
class EtfsResponse:
    instruments: List['Etf'] = message_field(1)


@dataclass
class FutureResponse:
    instrument: 'Future' = message_field(1)


@dataclass
class FuturesResponse:
    instruments: List['Future'] = message_field(1)


@dataclass
class OptionResponse:
    instrument: 'Option' = message_field(1)


@dataclass
class OptionsResponse:
    instruments: List['Option'] = message_field(1)


@dataclass
class Option:
    uid: str = message_field(1)
    position_uid: str = message_field(2)
    ticker: str = message_field(3)
    class_code: str = message_field(4)
    basic_asset_position_uid: str = message_field(5)
    trading_status: 'SecurityTradingStatus' = message_field(21)
    real_exchange: 'RealExchange' = message_field(31)
    direction: 'OptionDirection' = message_field(41)
    payment_type: 'OptionPaymentType' = message_field(42)
    style: 'OptionStyle' = message_field(43)
    settlement_type: 'OptionSettlementType' = message_field(44)
    name: str = message_field(101)
    currency: str = message_field(111)
    settlement_currency: str = message_field(112)
    asset_type: str = message_field(131)
    basic_asset: str = message_field(132)
    exchange: str = message_field(141)
    country_of_risk: str = message_field(151)
    country_of_risk_name: str = message_field(152)
    sector: str = message_field(161)
    brand: 'BrandData' = message_field(162)
    lot: int = message_field(201)
    basic_asset_size: 'Quotation' = message_field(211)
    klong: 'Quotation' = message_field(221)
    kshort: 'Quotation' = message_field(222)
    dlong: 'Quotation' = message_field(223)
    dshort: 'Quotation' = message_field(224)
    dlong_min: 'Quotation' = message_field(225)
    dshort_min: 'Quotation' = message_field(226)
    min_price_increment: 'Quotation' = message_field(231)
    strike_price: 'MoneyValue' = message_field(241)
    dlong_client: 'Quotation' = message_field(290)
    dshort_client: 'Quotation' = message_field(291)
    expiration_date: datetime = message_field(301)
    first_trade_date: datetime = message_field(311)
    last_trade_date: datetime = message_field(312)
    first_1min_candle_date: datetime = message_field(321)
    first_1day_candle_date: datetime = message_field(322)
    short_enabled_flag: bool = message_field(401)
    for_iis_flag: bool = message_field(402)
    otc_flag: bool = message_field(403)
    buy_available_flag: bool = message_field(404)
    sell_available_flag: bool = message_field(405)
    for_qual_investor_flag: bool = message_field(406)
    weekend_flag: bool = message_field(407)
    blocked_tca_flag: bool = message_field(408)
    api_trade_available_flag: bool = message_field(409)
    required_tests: List[str] = message_field(410)


class OptionDirection(IntEnum):
    OPTION_DIRECTION_UNSPECIFIED = 0
    OPTION_DIRECTION_PUT = 1
    OPTION_DIRECTION_CALL = 2


class OptionPaymentType(IntEnum):
    OPTION_PAYMENT_TYPE_UNSPECIFIED = 0
    OPTION_PAYMENT_TYPE_PREMIUM = 1
    OPTION_PAYMENT_TYPE_MARGINAL = 2


class OptionStyle(IntEnum):
    OPTION_STYLE_UNSPECIFIED = 0
    OPTION_STYLE_AMERICAN = 1
    OPTION_STYLE_EUROPEAN = 2


class OptionSettlementType(IntEnum):
    OPTION_EXECUTION_TYPE_UNSPECIFIED = 0
    OPTION_EXECUTION_TYPE_PHYSICAL_DELIVERY = 1
    OPTION_EXECUTION_TYPE_CASH_SETTLEMENT = 2


@dataclass
class ShareResponse:
    instrument: 'Share' = message_field(1)


@dataclass
class SharesResponse:
    instruments: List['Share'] = message_field(1)


@dataclass
class Bond:
    figi: str = message_field(1)
    ticker: str = message_field(2)
    class_code: str = message_field(3)
    isin: str = message_field(4)
    lot: int = message_field(5)
    currency: str = message_field(6)
    klong: 'Quotation' = message_field(7)
    kshort: 'Quotation' = message_field(8)
    dlong: 'Quotation' = message_field(9)
    dshort: 'Quotation' = message_field(10)
    dlong_min: 'Quotation' = message_field(11)
    dshort_min: 'Quotation' = message_field(12)
    short_enabled_flag: bool = message_field(13)
    name: str = message_field(15)
    exchange: str = message_field(16)
    coupon_quantity_per_year: int = message_field(17)
    maturity_date: datetime = message_field(18)
    nominal: 'MoneyValue' = message_field(19)
    initial_nominal: 'MoneyValue' = message_field(20)
    state_reg_date: datetime = message_field(21)
    placement_date: datetime = message_field(22)
    placement_price: 'MoneyValue' = message_field(23)
    aci_value: 'MoneyValue' = message_field(24)
    country_of_risk: str = message_field(25)
    country_of_risk_name: str = message_field(26)
    sector: str = message_field(27)
    issue_kind: str = message_field(28)
    issue_size: int = message_field(29)
    issue_size_plan: int = message_field(30)
    trading_status: 'SecurityTradingStatus' = message_field(31)
    otc_flag: bool = message_field(32)
    buy_available_flag: bool = message_field(33)
    sell_available_flag: bool = message_field(34)
    floating_coupon_flag: bool = message_field(35)
    perpetual_flag: bool = message_field(36)
    amortization_flag: bool = message_field(37)
    min_price_increment: 'Quotation' = message_field(38)
    api_trade_available_flag: bool = message_field(39)
    uid: str = message_field(40)
    real_exchange: 'RealExchange' = message_field(41)
    position_uid: str = message_field(42)
    asset_uid: str = message_field(43)
    required_tests: List[str] = message_field(44)
    for_iis_flag: bool = message_field(51)
    for_qual_investor_flag: bool = message_field(52)
    weekend_flag: bool = message_field(53)
    blocked_tca_flag: bool = message_field(54)
    subordinated_flag: bool = message_field(55)
    liquidity_flag: bool = message_field(56)
    first_1min_candle_date: datetime = message_field(61)
    first_1day_candle_date: datetime = message_field(62)
    risk_level: 'RiskLevel' = message_field(63)
    brand: 'BrandData' = message_field(64)
    bond_type: 'BondType' = message_field(65)
    call_date: datetime = message_field(69)
    dlong_client: 'Quotation' = message_field(90)
    dshort_client: 'Quotation' = message_field(91)


@dataclass
class Currency:
    figi: str = message_field(1)
    ticker: str = message_field(2)
    class_code: str = message_field(3)
    isin: str = message_field(4)
    lot: int = message_field(5)
    currency: str = message_field(6)
    klong: 'Quotation' = message_field(7)
    kshort: 'Quotation' = message_field(8)
    dlong: 'Quotation' = message_field(9)
    dshort: 'Quotation' = message_field(10)
    dlong_min: 'Quotation' = message_field(11)
    dshort_min: 'Quotation' = message_field(12)
    short_enabled_flag: bool = message_field(13)
    name: str = message_field(15)
    exchange: str = message_field(16)
    nominal: 'MoneyValue' = message_field(17)
    country_of_risk: str = message_field(18)
    country_of_risk_name: str = message_field(19)
    trading_status: 'SecurityTradingStatus' = message_field(20)
    otc_flag: bool = message_field(21)
    buy_available_flag: bool = message_field(22)
    sell_available_flag: bool = message_field(23)
    iso_currency_name: str = message_field(24)
    min_price_increment: 'Quotation' = message_field(25)
    api_trade_available_flag: bool = message_field(26)
    uid: str = message_field(27)
    real_exchange: 'RealExchange' = message_field(28)
    position_uid: str = message_field(29)
    required_tests: List[str] = message_field(30)
    for_iis_flag: bool = message_field(41)
    for_qual_investor_flag: bool = message_field(52)
    weekend_flag: bool = message_field(53)
    blocked_tca_flag: bool = message_field(54)
    first_1min_candle_date: datetime = message_field(56)
    first_1day_candle_date: datetime = message_field(57)
    brand: 'BrandData' = message_field(60)
    dlong_client: 'Quotation' = message_field(90)
    dshort_client: 'Quotation' = message_field(91)


@dataclass
class Etf:
    figi: str = message_field(1)
    ticker: str = message_field(2)
    class_code: str = message_field(3)
    isin: str = message_field(4)
    lot: int = message_field(5)
    currency: str = message_field(6)
    klong: 'Quotation' = message_field(7)
    kshort: 'Quotation' = message_field(8)
    dlong: 'Quotation' = message_field(9)
    dshort: 'Quotation' = message_field(10)
    dlong_min: 'Quotation' = message_field(11)
    dshort_min: 'Quotation' = message_field(12)
    short_enabled_flag: bool = message_field(13)
    name: str = message_field(15)
    exchange: str = message_field(16)
    fixed_commission: 'Quotation' = message_field(17)
    focus_type: str = message_field(18)
    released_date: datetime = message_field(19)
    num_shares: 'Quotation' = message_field(20)
    country_of_risk: str = message_field(21)
    country_of_risk_name: str = message_field(22)
    sector: str = message_field(23)
    rebalancing_freq: str = message_field(24)
    trading_status: 'SecurityTradingStatus' = message_field(25)
    otc_flag: bool = message_field(26)
    buy_available_flag: bool = message_field(27)
    sell_available_flag: bool = message_field(28)
    min_price_increment: 'Quotation' = message_field(29)
    api_trade_available_flag: bool = message_field(30)
    uid: str = message_field(31)
    real_exchange: 'RealExchange' = message_field(32)
    position_uid: str = message_field(33)
    asset_uid: str = message_field(34)
    instrument_exchange: 'InstrumentExchangeType' = message_field(35)
    required_tests: List[str] = message_field(36)
    for_iis_flag: bool = message_field(41)
    for_qual_investor_flag: bool = message_field(42)
    weekend_flag: bool = message_field(43)
    blocked_tca_flag: bool = message_field(44)
    liquidity_flag: bool = message_field(45)
    first_1min_candle_date: datetime = message_field(56)
    first_1day_candle_date: datetime = message_field(57)
    brand: 'BrandData' = message_field(60)
    dlong_client: 'Quotation' = message_field(90)
    dshort_client: 'Quotation' = message_field(91)


@dataclass
class Future:
    figi: str = message_field(1)
    ticker: str = message_field(2)
    class_code: str = message_field(3)
    lot: int = message_field(4)
    currency: str = message_field(5)
    klong: 'Quotation' = message_field(6)
    kshort: 'Quotation' = message_field(7)
    dlong: 'Quotation' = message_field(8)
    dshort: 'Quotation' = message_field(9)
    dlong_min: 'Quotation' = message_field(10)
    dshort_min: 'Quotation' = message_field(11)
    short_enabled_flag: bool = message_field(12)
    name: str = message_field(13)
    exchange: str = message_field(14)
    first_trade_date: datetime = message_field(15)
    last_trade_date: datetime = message_field(16)
    futures_type: str = message_field(17)
    asset_type: str = message_field(18)
    basic_asset: str = message_field(19)
    basic_asset_size: 'Quotation' = message_field(20)
    country_of_risk: str = message_field(21)
    country_of_risk_name: str = message_field(22)
    sector: str = message_field(23)
    expiration_date: datetime = message_field(24)
    trading_status: 'SecurityTradingStatus' = message_field(25)
    otc_flag: bool = message_field(26)
    buy_available_flag: bool = message_field(27)
    sell_available_flag: bool = message_field(28)
    min_price_increment: 'Quotation' = message_field(29)
    api_trade_available_flag: bool = message_field(30)
    uid: str = message_field(31)
    real_exchange: 'RealExchange' = message_field(32)
    position_uid: str = message_field(33)
    basic_asset_position_uid: str = message_field(34)
    required_tests: List[str] = message_field(35)
    for_iis_flag: bool = message_field(41)
    for_qual_investor_flag: bool = message_field(42)
    weekend_flag: bool = message_field(43)
    blocked_tca_flag: bool = message_field(44)
    first_1min_candle_date: datetime = message_field(56)
    first_1day_candle_date: datetime = message_field(57)
    initial_margin_on_buy: 'MoneyValue' = message_field(61)
    initial_margin_on_sell: 'MoneyValue' = message_field(62)
    min_price_increment_amount: 'Quotation' = message_field(63)
    brand: 'BrandData' = message_field(64)
    dlong_client: 'Quotation' = message_field(90)
    dshort_client: 'Quotation' = message_field(91)


@dataclass
class Share:
    figi: str = message_field(1)
    ticker: str = message_field(2)
    class_code: str = message_field(3)
    isin: str = message_field(4)
    lot: int = message_field(5)
    currency: str = message_field(6)
    klong: 'Quotation' = message_field(7)
    kshort: 'Quotation' = message_field(8)
    dlong: 'Quotation' = message_field(9)
    dshort: 'Quotation' = message_field(10)
    dlong_min: 'Quotation' = message_field(11)
    dshort_min: 'Quotation' = message_field(12)
    short_enabled_flag: bool = message_field(13)
    name: str = message_field(15)
    exchange: str = message_field(16)
    ipo_date: datetime = message_field(17)
    issue_size: int = message_field(18)
    country_of_risk: str = message_field(19)
    country_of_risk_name: str = message_field(20)
    sector: str = message_field(21)
    issue_size_plan: int = message_field(22)
    nominal: 'MoneyValue' = message_field(23)
    trading_status: 'SecurityTradingStatus' = message_field(25)
    otc_flag: bool = message_field(26)
    buy_available_flag: bool = message_field(27)
    sell_available_flag: bool = message_field(28)
    div_yield_flag: bool = message_field(29)
    share_type: 'ShareType' = message_field(30)
    min_price_increment: 'Quotation' = message_field(31)
    api_trade_available_flag: bool = message_field(32)
    uid: str = message_field(33)
    real_exchange: 'RealExchange' = message_field(34)
    position_uid: str = message_field(35)
    asset_uid: str = message_field(36)
    instrument_exchange: 'InstrumentExchangeType' = message_field(37)
    required_tests: List[str] = message_field(38)
    for_iis_flag: bool = message_field(46)
    for_qual_investor_flag: bool = message_field(47)
    weekend_flag: bool = message_field(48)
    blocked_tca_flag: bool = message_field(49)
    liquidity_flag: bool = message_field(50)
    first_1min_candle_date: datetime = message_field(56)
    first_1day_candle_date: datetime = message_field(57)
    brand: 'BrandData' = message_field(60)
    dlong_client: 'Quotation' = message_field(90)
    dshort_client: 'Quotation' = message_field(91)


@dataclass
class GetAccruedInterestsRequest:
    figi: str = message_field(1)
    from_: datetime = message_field(2)
    to: datetime = message_field(3)
    instrument_id: str = message_field(4)


@dataclass
class GetAccruedInterestsResponse:
    accrued_interests: List['AccruedInterest'] = message_field(1)


@dataclass
class AccruedInterest:
    date: datetime = message_field(1)
    value: 'Quotation' = message_field(2)
    value_percent: 'Quotation' = message_field(3)
    nominal: 'Quotation' = message_field(4)


@dataclass
class GetFuturesMarginRequest:
    figi: str = message_field(1)
    instrument_id: str = message_field(4)


@dataclass
class GetFuturesMarginResponse:
    initial_margin_on_buy: 'MoneyValue' = message_field(1)
    initial_margin_on_sell: 'MoneyValue' = message_field(2)
    min_price_increment: 'Quotation' = message_field(3)
    min_price_increment_amount: 'Quotation' = message_field(4)


class InstrumentIdType(IntEnum):
    INSTRUMENT_ID_UNSPECIFIED = 0
    INSTRUMENT_ID_TYPE_FIGI = 1
    INSTRUMENT_ID_TYPE_TICKER = 2
    INSTRUMENT_ID_TYPE_UID = 3
    INSTRUMENT_ID_TYPE_POSITION_UID = 4


@dataclass
class InstrumentResponse:
    instrument: 'Instrument' = message_field(1)


@dataclass
class Instrument:
    figi: str = message_field(1)
    ticker: str = message_field(2)
    class_code: str = message_field(3)
    isin: str = message_field(4)
    lot: int = message_field(5)
    currency: str = message_field(6)
    klong: 'Quotation' = message_field(7)
    kshort: 'Quotation' = message_field(8)
    dlong: 'Quotation' = message_field(9)
    dshort: 'Quotation' = message_field(10)
    dlong_min: 'Quotation' = message_field(11)
    dshort_min: 'Quotation' = message_field(12)
    short_enabled_flag: bool = message_field(13)
    name: str = message_field(14)
    exchange: str = message_field(15)
    country_of_risk: str = message_field(16)
    country_of_risk_name: str = message_field(17)
    instrument_type: str = message_field(18)
    trading_status: 'SecurityTradingStatus' = message_field(19)
    otc_flag: bool = message_field(20)
    buy_available_flag: bool = message_field(21)
    sell_available_flag: bool = message_field(22)
    min_price_increment: 'Quotation' = message_field(23)
    api_trade_available_flag: bool = message_field(24)
    uid: str = message_field(25)
    real_exchange: 'RealExchange' = message_field(26)
    position_uid: str = message_field(27)
    asset_uid: str = message_field(28)
    required_tests: List[str] = message_field(29)
    for_iis_flag: bool = message_field(36)
    for_qual_investor_flag: bool = message_field(37)
    weekend_flag: bool = message_field(38)
    blocked_tca_flag: bool = message_field(39)
    instrument_kind: 'InstrumentType' = message_field(40)
    first_1min_candle_date: datetime = message_field(56)
    first_1day_candle_date: datetime = message_field(57)
    brand: 'BrandData' = message_field(60)
    dlong_client: 'Quotation' = message_field(490)
    dshort_client: 'Quotation' = message_field(491)


@dataclass
class GetDividendsRequest:
    figi: str = message_field(1)
    from_: Optional[datetime] = message_field(2, optional=True)
    to: Optional[datetime] = message_field(3, optional=True)
    instrument_id: str = message_field(4)


@dataclass
class GetDividendsResponse:
    dividends: List['Dividend'] = message_field(1)


@dataclass
class Dividend:
    dividend_net: 'MoneyValue' = message_field(1)
    payment_date: datetime = message_field(2)
    declared_date: datetime = message_field(3)
    last_buy_date: datetime = message_field(4)
    dividend_type: str = message_field(5)
    record_date: datetime = message_field(6)
    regularity: str = message_field(7)
    close_price: 'MoneyValue' = message_field(8)
    yield_value: 'Quotation' = message_field(9)
    created_at: datetime = message_field(10)


class ShareType(IntEnum):
    SHARE_TYPE_UNSPECIFIED = 0
    SHARE_TYPE_COMMON = 1
    SHARE_TYPE_PREFERRED = 2
    SHARE_TYPE_ADR = 3
    SHARE_TYPE_GDR = 4
    SHARE_TYPE_MLP = 5
    SHARE_TYPE_NY_REG_SHRS = 6
    SHARE_TYPE_CLOSED_END_FUND = 7
    SHARE_TYPE_REIT = 8


@dataclass
class AssetRequest:
    id: str = message_field(1)


@dataclass
class AssetResponse:
    asset: 'AssetFull' = message_field(1)


@dataclass
class AssetsRequest:
    instrument_type: Optional['InstrumentType'] = message_field(1, optional
        =True)
    instrument_status: Optional['InstrumentStatus'] = message_field(2,
        optional=True)


@dataclass
class AssetsResponse:
    assets: List['Asset'] = message_field(1)


@dataclass
class AssetFull:
    uid: str = message_field(1)
    type: 'AssetType' = message_field(2)
    name: str = message_field(3)
    name_brief: str = message_field(4)
    description: str = message_field(5)
    deleted_at: datetime = message_field(6)
    required_tests: List[str] = message_field(7)
    currency: Optional['AssetCurrency'] = message_field(8, optional=True)
    security: Optional['AssetSecurity'] = message_field(9, optional=True)
    gos_reg_code: str = message_field(10)
    cfi: str = message_field(11)
    code_nsd: str = message_field(12)
    status: str = message_field(13)
    brand: 'Brand' = message_field(14)
    updated_at: datetime = message_field(15)
    br_code: str = message_field(16)
    br_code_name: str = message_field(17)
    instruments: List['AssetInstrument'] = message_field(18)


@dataclass
class Asset:
    uid: str = message_field(1)
    type: 'AssetType' = message_field(2)
    name: str = message_field(3)
    instruments: List['AssetInstrument'] = message_field(4)


class AssetType(IntEnum):
    ASSET_TYPE_UNSPECIFIED = 0
    ASSET_TYPE_CURRENCY = 1
    ASSET_TYPE_COMMODITY = 2
    ASSET_TYPE_INDEX = 3
    ASSET_TYPE_SECURITY = 4


@dataclass
class AssetCurrency:
    base_currency: str = message_field(1)


@dataclass
class AssetSecurity:
    isin: str = message_field(1)
    type: str = message_field(2)
    instrument_kind: 'InstrumentType' = message_field(10)
    share: Optional['AssetShare'] = message_field(3, optional=True)
    bond: Optional['AssetBond'] = message_field(4, optional=True)
    sp: Optional['AssetStructuredProduct'] = message_field(5, optional=True)
    etf: Optional['AssetEtf'] = message_field(6, optional=True)
    clearing_certificate: Optional['AssetClearingCertificate'] = message_field(
        7, optional=True)


@dataclass
class AssetShare:
    type: 'ShareType' = message_field(1)
    issue_size: 'Quotation' = message_field(2)
    nominal: 'Quotation' = message_field(3)
    nominal_currency: str = message_field(4)
    primary_index: str = message_field(5)
    dividend_rate: 'Quotation' = message_field(6)
    preferred_share_type: str = message_field(7)
    ipo_date: datetime = message_field(8)
    registry_date: datetime = message_field(9)
    div_yield_flag: bool = message_field(10)
    issue_kind: str = message_field(11)
    placement_date: datetime = message_field(12)
    repres_isin: str = message_field(13)
    issue_size_plan: 'Quotation' = message_field(14)
    total_float: 'Quotation' = message_field(15)


@dataclass
class AssetBond:
    current_nominal: 'Quotation' = message_field(1)
    borrow_name: str = message_field(2)
    issue_size: 'Quotation' = message_field(3)
    nominal: 'Quotation' = message_field(4)
    nominal_currency: str = message_field(5)
    issue_kind: str = message_field(6)
    interest_kind: str = message_field(7)
    coupon_quantity_per_year: int = message_field(8)
    indexed_nominal_flag: bool = message_field(9)
    subordinated_flag: bool = message_field(10)
    collateral_flag: bool = message_field(11)
    tax_free_flag: bool = message_field(12)
    amortization_flag: bool = message_field(13)
    floating_coupon_flag: bool = message_field(14)
    perpetual_flag: bool = message_field(15)
    maturity_date: datetime = message_field(16)
    return_condition: str = message_field(17)
    state_reg_date: datetime = message_field(18)
    placement_date: datetime = message_field(19)
    placement_price: 'Quotation' = message_field(20)
    issue_size_plan: 'Quotation' = message_field(21)


@dataclass
class AssetStructuredProduct:
    borrow_name: str = message_field(1)
    nominal: 'Quotation' = message_field(2)
    nominal_currency: str = message_field(3)
    type: 'StructuredProductType' = message_field(4)
    logic_portfolio: str = message_field(5)
    asset_type: 'AssetType' = message_field(6)
    basic_asset: str = message_field(7)
    safety_barrier: 'Quotation' = message_field(8)
    maturity_date: datetime = message_field(9)
    issue_size_plan: 'Quotation' = message_field(10)
    issue_size: 'Quotation' = message_field(11)
    placement_date: datetime = message_field(12)
    issue_kind: str = message_field(13)


class StructuredProductType(IntEnum):
    SP_TYPE_UNSPECIFIED = 0
    SP_TYPE_DELIVERABLE = 1
    SP_TYPE_NON_DELIVERABLE = 2


@dataclass
class AssetEtf:
    total_expense: 'Quotation' = message_field(1)
    hurdle_rate: 'Quotation' = message_field(2)
    performance_fee: 'Quotation' = message_field(3)
    fixed_commission: 'Quotation' = message_field(4)
    payment_type: str = message_field(5)
    watermark_flag: bool = message_field(6)
    buy_premium: 'Quotation' = message_field(7)
    sell_discount: 'Quotation' = message_field(8)
    rebalancing_flag: bool = message_field(9)
    rebalancing_freq: str = message_field(10)
    management_type: str = message_field(11)
    primary_index: str = message_field(12)
    focus_type: str = message_field(13)
    leveraged_flag: bool = message_field(14)
    num_share: 'Quotation' = message_field(15)
    ucits_flag: bool = message_field(16)
    released_date: datetime = message_field(17)
    description: str = message_field(18)
    primary_index_description: str = message_field(19)
    primary_index_company: str = message_field(20)
    index_recovery_period: 'Quotation' = message_field(21)
    inav_code: str = message_field(22)
    div_yield_flag: bool = message_field(23)
    expense_commission: 'Quotation' = message_field(24)
    primary_index_tracking_error: 'Quotation' = message_field(25)
    rebalancing_plan: str = message_field(26)
    tax_rate: str = message_field(27)
    rebalancing_dates: List[datetime] = message_field(28)
    issue_kind: str = message_field(29)
    nominal: 'Quotation' = message_field(30)
    nominal_currency: str = message_field(31)


@dataclass
class AssetClearingCertificate:
    nominal: 'Quotation' = message_field(1)
    nominal_currency: str = message_field(2)


@dataclass
class Brand:
    uid: str = message_field(1)
    name: str = message_field(2)
    description: str = message_field(3)
    info: str = message_field(4)
    company: str = message_field(5)
    sector: str = message_field(6)
    country_of_risk: str = message_field(7)
    country_of_risk_name: str = message_field(8)


@dataclass
class AssetInstrument:
    uid: str = message_field(1)
    figi: str = message_field(2)
    instrument_type: str = message_field(3)
    ticker: str = message_field(4)
    class_code: str = message_field(5)
    links: List['InstrumentLink'] = message_field(6)
    instrument_kind: 'InstrumentType' = message_field(10)
    position_uid: str = message_field(11)


@dataclass
class InstrumentLink:
    type: str = message_field(1)
    instrument_uid: str = message_field(2)


@dataclass
class GetFavoritesRequest:
    group_id: Optional[str] = message_field(1, optional=True)


@dataclass
class GetFavoritesResponse:
    favorite_instruments: List['FavoriteInstrument'] = message_field(1)
    group_id: Optional[str] = message_field(2, optional=True)


@dataclass
class FavoriteInstrument:
    figi: str = message_field(1)
    ticker: str = message_field(2)
    class_code: str = message_field(3)
    isin: str = message_field(4)
    instrument_type: str = message_field(11)
    name: str = message_field(12)
    uid: str = message_field(13)
    otc_flag: bool = message_field(16)
    api_trade_available_flag: bool = message_field(17)
    instrument_kind: 'InstrumentType' = message_field(18)


@dataclass
class EditFavoritesRequest:
    instruments: List['EditFavoritesRequestInstrument'] = message_field(1)
    action_type: 'EditFavoritesActionType' = message_field(6)
    group_id: Optional[str] = message_field(7, optional=True)


@dataclass
class EditFavoritesRequestInstrument:
    figi: Optional[str] = message_field(1, optional=True)
    instrument_id: str = message_field(2)


class EditFavoritesActionType(IntEnum):
    EDIT_FAVORITES_ACTION_TYPE_UNSPECIFIED = 0
    EDIT_FAVORITES_ACTION_TYPE_ADD = 1
    EDIT_FAVORITES_ACTION_TYPE_DEL = 2


@dataclass
class EditFavoritesResponse:
    favorite_instruments: List['FavoriteInstrument'] = message_field(1)
    group_id: Optional[str] = message_field(2, optional=True)


@dataclass
class CreateFavoriteGroupRequest:
    group_name: str = message_field(1)
    group_color: str = message_field(2)
    note: Optional[str] = message_field(3, optional=True)


@dataclass
class CreateFavoriteGroupResponse:
    group_id: str = message_field(1)
    group_name: str = message_field(2)


@dataclass
class DeleteFavoriteGroupRequest:
    group_id: str = message_field(1)


@dataclass
class DeleteFavoriteGroupResponse:
    pass


@dataclass
class GetFavoriteGroupsRequest:
    instrument_id: List[str] = message_field(1)
    excluded_group_id: List[str] = message_field(2)


@dataclass
class GetFavoriteGroupsResponse:
    groups: List['FavoriteGroup'] = message_field(1)


    @dataclass
    class FavoriteGroup:
        group_id: str = message_field(1)
        group_name: str = message_field(2)
        color: str = message_field(3)
        size: int = message_field(4)
        contains_instrument: Optional[bool] = message_field(5, optional=True)


@dataclass
class GetCountriesRequest:
    pass


@dataclass
class GetCountriesResponse:
    countries: List['CountryResponse'] = message_field(1)


@dataclass
class IndicativesRequest:
    pass


@dataclass
class IndicativesResponse:
    instruments: List['IndicativeResponse'] = message_field(1)


@dataclass
class IndicativeResponse:
    figi: str = message_field(1)
    ticker: str = message_field(2)
    class_code: str = message_field(3)
    currency: str = message_field(4)
    instrument_kind: 'InstrumentType' = message_field(10)
    name: str = message_field(12)
    exchange: str = message_field(13)
    uid: str = message_field(14)
    buy_available_flag: bool = message_field(404)
    sell_available_flag: bool = message_field(405)


@dataclass
class CountryResponse:
    alfa_two: str = message_field(1)
    alfa_three: str = message_field(2)
    name: str = message_field(3)
    name_brief: str = message_field(4)


@dataclass
class FindInstrumentRequest:
    query: str = message_field(1)
    instrument_kind: Optional['InstrumentType'] = message_field(2, optional
        =True)
    api_trade_available_flag: Optional[bool] = message_field(3, optional=True)


@dataclass
class FindInstrumentResponse:
    instruments: List['InstrumentShort'] = message_field(1)


@dataclass
class InstrumentShort:
    isin: str = message_field(1)
    figi: str = message_field(2)
    ticker: str = message_field(3)
    class_code: str = message_field(4)
    instrument_type: str = message_field(5)
    name: str = message_field(6)
    uid: str = message_field(7)
    position_uid: str = message_field(8)
    instrument_kind: 'InstrumentType' = message_field(10)
    api_trade_available_flag: bool = message_field(11)
    for_iis_flag: bool = message_field(12)
    first_1min_candle_date: datetime = message_field(26)
    first_1day_candle_date: datetime = message_field(27)
    for_qual_investor_flag: bool = message_field(28)
    weekend_flag: bool = message_field(29)
    blocked_tca_flag: bool = message_field(30)
    lot: int = message_field(31)


@dataclass
class GetBrandsRequest:
    paging: 'Page' = message_field(1)


@dataclass
class GetBrandRequest:
    id: str = message_field(1)


@dataclass
class GetBrandsResponse:
    brands: List['Brand'] = message_field(1)
    paging: 'PageResponse' = message_field(2)


@dataclass
class GetAssetFundamentalsRequest:
    assets: List[str] = message_field(1)


@dataclass
class GetAssetFundamentalsResponse:
    fundamentals: List['StatisticResponse'] = message_field(1)


    @dataclass
    class StatisticResponse:
        asset_uid: str = message_field(1)
        currency: str = message_field(2)
        market_capitalization: float = message_field(3)
        high_price_last_52_weeks: float = message_field(4)
        low_price_last_52_weeks: float = message_field(5)
        average_daily_volume_last_10_days: float = message_field(6)
        average_daily_volume_last_4_weeks: float = message_field(7)
        beta: float = message_field(8)
        free_float: float = message_field(9)
        forward_annual_dividend_yield: float = message_field(10)
        shares_outstanding: float = message_field(11)
        revenue_ttm: float = message_field(12)
        ebitda_ttm: float = message_field(13)
        net_income_ttm: float = message_field(14)
        eps_ttm: float = message_field(15)
        diluted_eps_ttm: float = message_field(16)
        free_cash_flow_ttm: float = message_field(17)
        five_year_annual_revenue_growth_rate: float = message_field(18)
        three_year_annual_revenue_growth_rate: float = message_field(19)
        pe_ratio_ttm: float = message_field(20)
        price_to_sales_ttm: float = message_field(21)
        price_to_book_ttm: float = message_field(22)
        price_to_free_cash_flow_ttm: float = message_field(23)
        total_enterprise_value_mrq: float = message_field(24)
        ev_to_ebitda_mrq: float = message_field(25)
        net_margin_mrq: float = message_field(26)
        net_interest_margin_mrq: float = message_field(27)
        roe: float = message_field(28)
        roa: float = message_field(29)
        roic: float = message_field(30)
        total_debt_mrq: float = message_field(31)
        total_debt_to_equity_mrq: float = message_field(32)
        total_debt_to_ebitda_mrq: float = message_field(33)
        free_cash_flow_to_price: float = message_field(34)
        net_debt_to_ebitda: float = message_field(35)
        current_ratio_mrq: float = message_field(36)
        fixed_charge_coverage_ratio_fy: float = message_field(37)
        dividend_yield_daily_ttm: float = message_field(38)
        dividend_rate_ttm: float = message_field(39)
        dividends_per_share: float = message_field(40)
        five_years_average_dividend_yield: float = message_field(41)
        five_year_annual_dividend_growth_rate: float = message_field(42)
        dividend_payout_ratio_fy: float = message_field(43)
        buy_back_ttm: float = message_field(44)
        one_year_annual_revenue_growth_rate: float = message_field(45)
        domicile_indicator_code: str = message_field(46)
        adr_to_common_share_ratio: float = message_field(47)
        number_of_employees: float = message_field(48)
        ex_dividend_date: datetime = message_field(49)
        fiscal_period_start_date: datetime = message_field(50)
        fiscal_period_end_date: datetime = message_field(51)
        revenue_change_five_years: float = message_field(53)
        eps_change_five_years: float = message_field(54)
        ebitda_change_five_years: float = message_field(55)
        total_debt_change_five_years: float = message_field(56)
        ev_to_sales: float = message_field(57)


@dataclass
class GetAssetReportsRequest:
    instrument_id: str = message_field(1)
    from_: Optional[datetime] = message_field(2, optional=True)
    to: Optional[datetime] = message_field(3, optional=True)


@dataclass
class GetAssetReportsResponse:
    events: List['GetAssetReportsEvent'] = message_field(1)


    @dataclass
    class GetAssetReportsEvent:
        instrument_id: str = message_field(1)
        report_date: datetime = message_field(2)
        period_year: int = message_field(3)
        period_num: int = message_field(4)
        period_type: 'AssetReportPeriodType' = message_field(5)
        created_at: datetime = message_field(6)


    class AssetReportPeriodType(IntEnum):
        PERIOD_TYPE_UNSPECIFIED = 0
        PERIOD_TYPE_QUARTER = 1
        PERIOD_TYPE_SEMIANNUAL = 2
        PERIOD_TYPE_ANNUAL = 3


@dataclass
class GetConsensusForecastsRequest:
    paging: Optional['Page'] = message_field(1, optional=True)


@dataclass
class GetConsensusForecastsResponse:
    items: List['ConsensusForecastsItem'] = message_field(1)
    page: 'PageResponse' = message_field(2)


    @dataclass
    class ConsensusForecastsItem:
        uid: str = message_field(1)
        asset_uid: str = message_field(2)
        created_at: datetime = message_field(3)
        best_target_price: 'Quotation' = message_field(4)
        best_target_low: 'Quotation' = message_field(5)
        best_target_high: 'Quotation' = message_field(6)
        total_buy_recommend: int = message_field(7)
        total_hold_recommend: int = message_field(8)
        total_sell_recommend: int = message_field(9)
        currency: str = message_field(10)
        consensus: 'Recommendation' = message_field(11)
        prognosis_date: datetime = message_field(12)


class Recommendation(IntEnum):
    RECOMMENDATION_UNSPECIFIED = 0
    RECOMMENDATION_BUY = 1
    RECOMMENDATION_HOLD = 2
    RECOMMENDATION_SELL = 3


@dataclass
class GetForecastRequest:
    instrument_id: str = message_field(1)


@dataclass
class GetForecastResponse:
    targets: List['TargetItem'] = message_field(1)
    consensus: 'ConsensusItem' = message_field(2)


    @dataclass
    class TargetItem:
        uid: str = message_field(1)
        ticker: str = message_field(2)
        company: str = message_field(3)
        recommendation: 'Recommendation' = message_field(4)
        recommendation_date: datetime = message_field(5)
        currency: str = message_field(6)
        current_price: 'Quotation' = message_field(7)
        target_price: 'Quotation' = message_field(8)
        price_change: 'Quotation' = message_field(9)
        price_change_rel: 'Quotation' = message_field(10)
        show_name: str = message_field(11)


    @dataclass
    class ConsensusItem:
        uid: str = message_field(1)
        ticker: str = message_field(2)
        recommendation: 'Recommendation' = message_field(3)
        currency: str = message_field(4)
        current_price: 'Quotation' = message_field(5)
        consensus: 'Quotation' = message_field(6)
        min_target: 'Quotation' = message_field(7)
        max_target: 'Quotation' = message_field(8)
        price_change: 'Quotation' = message_field(9)
        price_change_rel: 'Quotation' = message_field(10)


@dataclass
class RiskRatesRequest:
    instrument_id: List[str] = message_field(1)


@dataclass
class RiskRatesResponse:
    instrument_risk_rates: List['RiskRateResult'] = message_field(1)


    @dataclass
    class RiskRateResult:
        instrument_uid: str = message_field(1)
        short_risk_rate: Optional['RiskRate'] = message_field(2, optional=True)
        long_risk_rate: Optional['RiskRate'] = message_field(3, optional=True)
        short_risk_rates: List['RiskRate'] = message_field(5)
        long_risk_rates: List['RiskRate'] = message_field(6)
        error: Optional[str] = message_field(9, optional=True)


    @dataclass
    class RiskRate:
        risk_level_code: str = message_field(2)
        value: 'Quotation' = message_field(5)


@dataclass
class TradingInterval:
    type: str = message_field(1)
    interval: 'TimeInterval' = message_field(2)


    @dataclass
    class TimeInterval:
        start_ts: datetime = message_field(1)
        end_ts: datetime = message_field(2)


@dataclass
class GetInsiderDealsRequest:
    instrument_id: str = message_field(1)
    limit: int = message_field(2)
    next_cursor: Optional[str] = message_field(3, optional=True)


@dataclass
class GetInsiderDealsResponse:
    insider_deals: List['InsiderDeal'] = message_field(1)
    next_cursor: Optional[str] = message_field(2, optional=True)


    @dataclass
    class InsiderDeal:
        trade_id: int = message_field(1)
        direction: 'TradeDirection' = message_field(2)
        currency: str = message_field(3)
        date: datetime = message_field(4)
        quantity: int = message_field(5)
        price: 'Quotation' = message_field(6)
        instrument_uid: str = message_field(7)
        ticker: str = message_field(8)
        investor_name: str = message_field(9)
        investor_position: str = message_field(10)
        percentage: float = message_field(11)
        is_option_execution: bool = message_field(12)
        disclosure_date: datetime = message_field(13)


    class TradeDirection(IntEnum):
        TRADE_DIRECTION_UNSPECIFIED = 0
        TRADE_DIRECTION_BUY = 1
        TRADE_DIRECTION_SELL = 2


class RiskLevel(IntEnum):
    RISK_LEVEL_UNSPECIFIED = 0
    RISK_LEVEL_LOW = 1
    RISK_LEVEL_MODERATE = 2
    RISK_LEVEL_HIGH = 3


class BondType(IntEnum):
    BOND_TYPE_UNSPECIFIED = 0
    BOND_TYPE_REPLACED = 1


class InstrumentExchangeType(IntEnum):
    INSTRUMENT_EXCHANGE_UNSPECIFIED = 0
    INSTRUMENT_EXCHANGE_DEALER = 1
