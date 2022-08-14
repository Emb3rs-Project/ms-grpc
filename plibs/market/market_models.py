from pydantic import Field
from base.BaseGRPC import BaseGRPC


class ShortTermOutputModel(BaseGRPC):
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


class LongTermOutputModel(BaseGRPC):
    Gn: list = Field(default=[])
    Ln: list = Field(default=[])
    Pn: list = Field(default=[])
    QoE: list = Field(default=[])
    optimal: bool = Field(default=None)
    settlement: list = Field(default=[])
    social_welfare_h: list = Field(default=[])
    SPM: list = Field(default=[])
    ADG: list = Field(default=[])
    expensive_prod: str = Field(default=None)
    shadow_price: list = Field(default=[])
    Tnm: list = Field(default=[])
    agent_operational_cost: list = Field(default=[])
