import jsonpickle
from pydantic import BaseModel


class BaseGRPC(BaseModel):

    def from_grpc(self, grpc_message):
        for attribute in self.__dict__.keys():
            if attribute[:2] != '__':
                self._set_variable(attribute, grpc_message)
        return self

    def _set_variable(self, attribute, grpc_message):
        attr_type = type(getattr(self, attribute)).__name__
        if attribute in grpc_message.DESCRIPTOR.fields_by_name.keys():
            grpc_value = getattr(grpc_message, attribute)
            if attr_type == 'dict' and not not grpc_value:
                parsed = jsonpickle.decode(grpc_value)
                setattr(self, attribute, parsed)
            else:
                setattr(self, attribute, grpc_value)
