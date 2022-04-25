
from concurrent import futures
import grpc
import jsonpickle
from manager.manager_pb2 import StartSimulationRequest, StartSimulationResponse
from manager.manager_pb2_grpc import ManagerModuleServicer, add_ManagerModuleServicer_to_server

class ManagerModule(ManagerModuleServicer):

    def __init__(self) -> None:
        pass

    def StartSimulation(self, request : StartSimulationRequest, context) -> StartSimulationResponse:
        
        return StartSimulationResponse(
            simulation_uuid = request.simulation_uuid,
            result = jsonpickle.encode({ "id" : 1, "name" : "David", "age" : 33}, unpicklable=True)
        )




def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ManagerModuleServicer_to_server(ManagerModule(), server)

    server.add_insecure_port("[::]:50051")

    print("Listening...")

    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()