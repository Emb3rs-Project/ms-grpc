from typing import Dict, Any
from pydantic import Field
from base.BaseGRPC import BaseGRPC


class StartSimulationRequestModel(BaseGRPC):
    simulation_uuid: str = Field(default=None)
    simulation_metadata: Dict[str, Any] = Field(default={})
    initial_data: Dict[str, Any] = Field(default={})


class StartSimulationResponseModel(BaseGRPC):
    simulation_uuid: str = Field(default=None)
    result: Dict[str, Any] = Field(default={})
