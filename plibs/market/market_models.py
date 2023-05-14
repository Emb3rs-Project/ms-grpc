from typing import Union

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
    Gn: dict = Field(default={})
    Ln: dict = Field(default={})
    Pn: dict = Field(default={})
    QoE: dict = Field(default={})
    optimal: str = Field(default=None)
    settlement: dict = Field(default={})
    social_welfare_h: list = Field(default=[])
    SPM: dict = Field(default={})
    ADG: dict = Field(default={})
    expensive_prod: str = Field(default=None)
    shadow_price: list = Field(default=[])
    Tnm: Union[list, str] = Field(default=[])
    agent_operational_cost: dict = Field(default={})
    report: str = Field(default="")
