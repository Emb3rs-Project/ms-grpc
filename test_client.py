from uuid import uuid4
import grpc
import jsonpickle

from manager.manager_models import StartSimulationResponseModel
from manager.manager_pb2 import StartSimulationRequest
from manager.manager_pb2_grpc import ManagerStub


class ManagerClient(object):

    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

        self.channel = grpc.insecure_channel(
            f"{self.host}:{self.port}"
        )

        self.stub = ManagerStub(self.channel)

    def start_simulation(self, uuid):
        s_request = StartSimulationRequest(
            simulation_uuid=uuid,
            simulation_metadata=jsonpickle.encode({}, unpicklable=False),
            initial_data=jsonpickle.encode({}, unpicklable=False)
        )

        print(f'{s_request}')

        return self.stub.StartSimulation(s_request)


if __name__ == '__main__':
    client = ManagerClient('localhost', 50051)
    response = client.start_simulation(str(uuid4()))
    result = StartSimulationResponseModel().from_grpc(response)

    print(f'{result}')
