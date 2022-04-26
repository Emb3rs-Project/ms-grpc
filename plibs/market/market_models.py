from typing import Dict, Any
from pydantic import Field
from base.BaseGRPC import BaseGRPC

class MarketOutputModel(BaseGRPC):
    Gn: list = Field(default=[])
    Ln: list = Field(default=[])
    Pn: list = Field(default=[])
    QoE: list = Field(default=[])
    optimal: bool = Field(default=None)
    plot_market_clearing: str = Field(default="")
    settlement: list = Field(default=[])
    social_welfare_h: list = Field(default=[])
    shadow_price: list = Field(default=[])
    Tnm: list = Field(default=[])
    agent_operational_cost: list = Field(default=[])
