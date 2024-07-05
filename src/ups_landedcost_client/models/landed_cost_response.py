# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .brokerage_fee_items import BrokerageFeeItems
from .response_shipment_items import ResponseShipmentItems
from .errors import Errors


@JsonMap(
    {
        "abs_layer_time": "absLayerTime",
        "fulfill_time": "fulfillTime",
        "receipt_time": "receiptTime",
    }
)
class PerfStats(BaseModel):
    """See ALPerfStats

    :param abs_layer_time: Time taken through the abstraction layer in milliseconds.
    :type abs_layer_time: str
    :param fulfill_time: Time taken to complete the request.
    :type fulfill_time: str
    :param receipt_time: Time taken to receive the request.
    :type receipt_time: str
    """

    def __init__(self, abs_layer_time: str, fulfill_time: str, receipt_time: str):
        self.abs_layer_time = abs_layer_time
        self.fulfill_time = fulfill_time
        self.receipt_time = receipt_time


@JsonMap(
    {
        "currency_code": "currencyCode",
        "import_country_code": "importCountryCode",
        "id_": "id",
        "brokerage_fee_items": "brokerageFeeItems",
        "total_brokerage_fees": "totalBrokerageFees",
        "total_duties": "totalDuties",
        "total_commodity_level_taxes_and_fees": "totalCommodityLevelTaxesAndFees",
        "total_shipment_level_taxes_and_fees": "totalShipmentLevelTaxesAndFees",
        "total_vat": "totalVAT",
        "total_duty_and_tax": "totalDutyAndTax",
        "grand_total": "grandTotal",
        "shipment_items": "shipmentItems",
        "trans_id": "transID",
        "perf_stats": "perfStats",
        "al_version": "alVersion",
    }
)
class Shipment(BaseModel):
    """Every Landed Cost response must be based on a shipment.

    :param currency_code: Specifies the Currency Code set at the commodity level. This currency is applicable for all duty, tax, VAT, and fee at the shipment and commodity level.
    :type currency_code: str
    :param import_country_code: Specifies the Import/Ship-To/Destination/Final country of the shipment. Please check country list in the Appendices section.
    :type import_country_code: str
    :param id_: Specifies the Shipment ID in the Landed Cost quote.
    :type id_: str
    :param brokerage_fee_items: An array of Brokerage fees.
    :type brokerage_fee_items: List[BrokerageFeeItems]
    :param total_brokerage_fees: Grand total of all applicable Brokerage fees.
    :type total_brokerage_fees: float
    :param total_duties: Total duty amount of this shipment.
    :type total_duties: float
    :param total_commodity_level_taxes_and_fees: Total tax and other fees at commodity level.
    :type total_commodity_level_taxes_and_fees: float
    :param total_shipment_level_taxes_and_fees: Total tax and other fees at shipment level.
    :type total_shipment_level_taxes_and_fees: float
    :param total_vat: Total VAT of the shipment.
    :type total_vat: float
    :param total_duty_and_tax: Grand total of the combined duty, VAT, tax, and other fees of all commodities in this shipment including shipment level taxes and fees.
    :type total_duty_and_tax: float
    :param grand_total: Sum of totalDutyAndTax + totalBrokerageFees
    :type grand_total: float
    :param shipment_items: An array of Landed Cost for all valid commodities.
    :type shipment_items: List[ResponseShipmentItems]
    :param trans_id: An identifier unique to the request., defaults to None
    :type trans_id: str, optional
    :param perf_stats: See ALPerfStats, defaults to None
    :type perf_stats: PerfStats, optional
    :param al_version: Version number of the instance that processed this request. Default is 1., defaults to None
    :type al_version: int, optional
    :param errors: Error code and description, defaults to None
    :type errors: Errors, optional
    """

    def __init__(
        self,
        currency_code: str,
        import_country_code: str,
        id_: str,
        brokerage_fee_items: List[BrokerageFeeItems],
        total_brokerage_fees: float,
        total_duties: float,
        total_commodity_level_taxes_and_fees: float,
        total_shipment_level_taxes_and_fees: float,
        total_vat: float,
        total_duty_and_tax: float,
        grand_total: float,
        shipment_items: List[ResponseShipmentItems],
        trans_id: str = None,
        perf_stats: PerfStats = None,
        al_version: int = None,
        errors: Errors = None,
    ):
        self.currency_code = currency_code
        self.import_country_code = import_country_code
        self.id_ = id_
        self.brokerage_fee_items = self._define_list(
            brokerage_fee_items, BrokerageFeeItems
        )
        self.total_brokerage_fees = total_brokerage_fees
        self.total_duties = total_duties
        self.total_commodity_level_taxes_and_fees = total_commodity_level_taxes_and_fees
        self.total_shipment_level_taxes_and_fees = total_shipment_level_taxes_and_fees
        self.total_vat = total_vat
        self.total_duty_and_tax = total_duty_and_tax
        self.grand_total = grand_total
        self.shipment_items = self._define_list(shipment_items, ResponseShipmentItems)
        if trans_id is not None:
            self.trans_id = trans_id
        if perf_stats is not None:
            self.perf_stats = self._define_object(perf_stats, PerfStats)
        if al_version is not None:
            self.al_version = al_version
        if errors is not None:
            self.errors = self._define_object(errors, Errors)


@JsonMap({})
class LandedCostResponse(BaseModel):
    """LandedCostResponse

    :param shipment: Every Landed Cost response must be based on a shipment.
    :type shipment: Shipment
    """

    def __init__(self, shipment: Shipment):
        self.shipment = self._define_object(shipment, Shipment)
