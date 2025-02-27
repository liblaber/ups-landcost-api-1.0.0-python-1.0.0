# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .landed_cost_request_shipment import LandedCostRequestShipment


@JsonMap(
    {
        "currency_code": "currencyCode",
        "trans_id": "transID",
        "allow_partial_landed_cost_result": "allowPartialLandedCostResult",
    }
)
class LandedCostRequest(BaseModel):
    """The root element for the Landed Cost document.

    :param currency_code: Specifies the currency of transaction or purchase.
    :type currency_code: str
    :param trans_id: Unique transaction ID for the request.
    :type trans_id: str
    :param allow_partial_landed_cost_result: An optional flag to indicate that partial landed cost calculations are acceptable to be used by upstream systems. When set to *false*, the system will return an error when at least one commodity in the shipment is invalid (all or none), and no results  will be sent back for that request. When set to *true*, the system will return partial calculations when applicable. Valid values: true = Partial Landed Cost result will return. false = All or No result will return (default)., defaults to None
    :type allow_partial_landed_cost_result: bool, optional
    :param alversion: Version number of the instance that processed this request. This must match the major number of the corresponding ICD version.
    :type alversion: int
    :param shipment: Every Landed Cost request must be based on a shipment.
    :type shipment: LandedCostRequestShipment
    """

    def __init__(
        self,
        currency_code: str,
        trans_id: str,
        alversion: int,
        shipment: LandedCostRequestShipment,
        allow_partial_landed_cost_result: bool = None,
    ):
        self.currency_code = currency_code
        self.trans_id = trans_id
        if allow_partial_landed_cost_result is not None:
            self.allow_partial_landed_cost_result = allow_partial_landed_cost_result
        self.alversion = alversion
        self.shipment = self._define_object(shipment, LandedCostRequestShipment)
