
from dataclasses import dataclass
from typing import Any, Dict

import jsonpickle


@dataclass
class StartSimulationRequestModel(object):
    simulation_uuid: str
    simulation_metadata: str 
    initial_data: str


@dataclass
class StartSimulationResponseModel(object):
    simulation_uuid: str
    result: Dict[str, Any]

    def __init__(self, message) -> None:
        self.simulation_uuid = message.simulation_uuid
        self.result = jsonpickle.decode(message.result)
        pass