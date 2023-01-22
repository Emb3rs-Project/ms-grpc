# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from manager import manager_pb2 as manager_dot_manager__pb2


class ManagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartSimulation = channel.unary_unary(
                '/manager.Manager/StartSimulation',
                request_serializer=manager_dot_manager__pb2.StartSimulationRequest.SerializeToString,
                response_deserializer=manager_dot_manager__pb2.StartSimulationResponse.FromString,
                )
        self.StartCharacterization = channel.unary_unary(
                '/manager.Manager/StartCharacterization',
                request_serializer=manager_dot_manager__pb2.StartCharacterizationRequest.SerializeToString,
                response_deserializer=manager_dot_manager__pb2.StartCharacterizationResponse.FromString,
                )
        self.UpdateSimulation = channel.unary_unary(
                '/manager.Manager/UpdateSimulation',
                request_serializer=manager_dot_manager__pb2.UpdateSimulationRequest.SerializeToString,
                response_deserializer=manager_dot_manager__pb2.UpdateSimulationResponse.FromString,
                )


class ManagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartSimulation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartCharacterization(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSimulation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartSimulation': grpc.unary_unary_rpc_method_handler(
                    servicer.StartSimulation,
                    request_deserializer=manager_dot_manager__pb2.StartSimulationRequest.FromString,
                    response_serializer=manager_dot_manager__pb2.StartSimulationResponse.SerializeToString,
            ),
            'StartCharacterization': grpc.unary_unary_rpc_method_handler(
                    servicer.StartCharacterization,
                    request_deserializer=manager_dot_manager__pb2.StartCharacterizationRequest.FromString,
                    response_serializer=manager_dot_manager__pb2.StartCharacterizationResponse.SerializeToString,
            ),
            'UpdateSimulation': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSimulation,
                    request_deserializer=manager_dot_manager__pb2.UpdateSimulationRequest.FromString,
                    response_serializer=manager_dot_manager__pb2.UpdateSimulationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'manager.Manager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Manager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartSimulation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/manager.Manager/StartSimulation',
            manager_dot_manager__pb2.StartSimulationRequest.SerializeToString,
            manager_dot_manager__pb2.StartSimulationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartCharacterization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/manager.Manager/StartCharacterization',
            manager_dot_manager__pb2.StartCharacterizationRequest.SerializeToString,
            manager_dot_manager__pb2.StartCharacterizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateSimulation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/manager.Manager/UpdateSimulation',
            manager_dot_manager__pb2.UpdateSimulationRequest.SerializeToString,
            manager_dot_manager__pb2.UpdateSimulationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
