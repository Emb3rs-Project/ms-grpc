from typing import Any, Dict

from pydantic import Field
from base.BaseGRPC import BaseGRPC


class ConvertSinkOutputModel(BaseGRPC):
    all_sinks_info: Dict[str, Any] = Field(default={})
    n_grid_specific: list = Field(default=[])
    n_demand_list: list = Field(default=[])
    n_thermal_storage: list = Field(default=[])
    teo_demand_factor_group: list = Field(default=[])


class ConvertSourceOutputModel(BaseGRPC):
    all_sources_info: list = Field(default=[])
    ex_grid: list = Field(default=[])
    teo_string: str = Field(default=None)
    input_fuel: str = Field(default=None)
    output_fuel: str = Field(default=None)
    output: int = Field(default=None)
    input: int = Field(default=None)
    n_supply_list: list = Field(default=[])
    teo_capacity_factor_group: list = Field(default=[])
    teo_dhn: Dict[str, Any] = Field(default={})


class ConvertPinchOutputModel(BaseGRPC):
    best_options: Dict[str, Any] = Field(default={})
    report: str = Field(default="")


class ConvertOrcOutputModel(BaseGRPC):
    best_options: list = Field(default=[])
    report: str = Field(default="")


class CharacterizationSourceOutputModel(BaseGRPC):
    streams: list = Field(default=[])


class CharacterizationSinkOutputModel(BaseGRPC):
    streams: list = Field(default=[])


class CharacterizationOutput(BaseGRPC):
    stream: Dict[str, Any] = Field(default={})
