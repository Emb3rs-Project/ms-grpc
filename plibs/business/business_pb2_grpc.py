# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from business import business_pb2 as business_dot_business__pb2


class BusinessModuleStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.bm = channel.unary_unary(
                '/business.BusinessModule/bm',
                request_serializer=business_dot_business__pb2.BMInput.SerializeToString,
                response_deserializer=business_dot_business__pb2.BMOutput.FromString,
                )
        self.internal_heat_recobery = channel.unary_unary(
                '/business.BusinessModule/internal_heat_recobery',
                request_serializer=business_dot_business__pb2.InternalHeatRecoveryInput.SerializeToString,
                response_deserializer=business_dot_business__pb2.InternalHeatRecoveryOutput.FromString,
                )


class BusinessModuleServicer(object):
    """Missing associated documentation comment in .proto file."""

    def bm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def internal_heat_recobery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BusinessModuleServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'bm': grpc.unary_unary_rpc_method_handler(
                    servicer.bm,
                    request_deserializer=business_dot_business__pb2.BMInput.FromString,
                    response_serializer=business_dot_business__pb2.BMOutput.SerializeToString,
            ),
            'internal_heat_recobery': grpc.unary_unary_rpc_method_handler(
                    servicer.internal_heat_recobery,
                    request_deserializer=business_dot_business__pb2.InternalHeatRecoveryInput.FromString,
                    response_serializer=business_dot_business__pb2.InternalHeatRecoveryOutput.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'business.BusinessModule', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BusinessModule(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def bm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/business.BusinessModule/bm',
            business_dot_business__pb2.BMInput.SerializeToString,
            business_dot_business__pb2.BMOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def internal_heat_recobery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/business.BusinessModule/internal_heat_recobery',
            business_dot_business__pb2.InternalHeatRecoveryInput.SerializeToString,
            business_dot_business__pb2.InternalHeatRecoveryOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
