import sys
from concurrent import futures
import grpc
import jsonpickle

from plibs.manager.manager_pb2 import StartSimulationRequest, StartSimulationResponse
from plibs.manager.manager_pb2_grpc import ManagerServicer, add_ManagerServicer_to_server


class ManagerModule(ManagerServicer):

    def __init__(self) -> None:
        pass

    def StartSimulation(self, request: StartSimulationRequest, context) -> StartSimulationResponse:
        return StartSimulationResponse(
            simulation_uuid=request.simulation_uuid,
            result=jsonpickle.encode(
                {"id": 1, "name": "David", "age": 33}, unpicklable=False)
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ManagerServicer_to_server(ManagerModule(), server)

    server.add_insecure_port("[::]:50051")

    print("Listening...")

    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
