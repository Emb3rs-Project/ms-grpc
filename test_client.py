


from uuid import uuid4
import grpc
import jsonpickle
from manager.manager_pb2 import StartSimulationRequest, StartSimulationResponse

from manager.manager_pb2_grpc import ManagerModuleStub
from manager.models import StartSimulationRequestModel, StartSimulationResponseModel


class ManagerClient(object):


    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

        self.channel = grpc.insecure_channel(
            f"{self.host}:{self.port}"
        )

        self.stub = ManagerModuleStub(self.channel)


    def start_simulation(self, uuid):

        sRequest = StartSimulationRequest(
            simulation_uuid = uuid,
            simulation_metadata = jsonpickle.encode({}, unpicklable=True),
            initial_data = jsonpickle.encode({}, unpicklable=True)
        )

        print(f'{sRequest}')

        return self.stub.StartSimulation(sRequest)


if __name__ == '__main__':
    client = ManagerClient('localhost', 50051)
    result : StartSimulationResponseModel = StartSimulationResponseModel(client.start_simulation(str(uuid4())))

    print(f'{result}')