from typing import Dict, Any

from pydantic import Field
from base.BaseGRPC import BaseGRPC


class ConvertSinkOutputModel(BaseGRPC):
    all_sinks_info: Dict[str, Any] = Field(default={})
    n_demand_list: list = Field(default=[])
    teo_demand_factor_group: list = Field(default=[])


class ConvertSourceOutputModel(BaseGRPC):
    all_sources_info: list = Field(default=[])
    teo_string: str = Field(default=None)
    input_fuel: str = Field(default=None)
    output_fuel: str = Field(default=None)
    output: int = Field(default=None)
    input: int = Field(default=None)
    n_supply_list: list = Field(default=[])
    teo_capacity_factor_group: list = Field(default=[])
    teo_dhn: Dict[str, Any] = Field(default={})


class ConvertPinchOutputModel(BaseGRPC):
    co2_optimization: list = Field(default=[])
    energy_recovered_optimization: list = Field(default=[])
    energy_investment_optimization: list = Field(default=[])


class ConvertOrcOutputModel(BaseGRPC):
    best_options: list = Field(default=[])


class CharacterizationSourceOutputModel(BaseGRPC):
    streams: list = Field(default=[])


class CharacterizationSinkOutputModel(BaseGRPC):
    hot_stream: Dict[str, Any] = Field(default={})
    cold_stream: Dict[str, Any] = Field(default={})
