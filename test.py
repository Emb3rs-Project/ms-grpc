import jsonpickle

from manager.manager_pb2 import StartSimulationRequest
from plibs.manager.manager_models import StartSimulationRequestModel

a = StartSimulationRequestModel()

_dict = {
    "xpto": 1,
    "data": "x",
    "array": [1, ",", 3]
}

inputs = {
    "simulation_uuid": 'xpto',
    "simulation_metadata": jsonpickle.encode(_dict, unpicklable=True)
}

grpc_request = StartSimulationRequest(
    **inputs
)

a.from_grpc(grpc_request)

print(a)
