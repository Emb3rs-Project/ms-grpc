from typing import Dict, List, Tuple, Union, get_args, get_origin

import jsonpickle
from pydantic import BaseModel

ITERABLE_TYPES = (dict, list, tuple, Dict, List, Tuple)


class BaseGRPC(BaseModel):

    def from_grpc(self, grpc_message):
        for attribute in self.__dict__.keys():
            if attribute[:2] != '__':
                self._set_variable(attribute, grpc_message)
        return self

    def _set_variable(self, attribute, grpc_message):
        attr_type = get_origin(self.__fields__[attribute].annotation) or self.__fields__[attribute].type_
        if attr_type is Union:
            attr_type_args = get_args(attr_type)
            attr_type = get_origin(attr_type_args[0] if len(attr_type_args) > 0 else attr_type_args)
        if attribute in grpc_message.DESCRIPTOR.fields_by_name.keys():
            grpc_value = getattr(grpc_message, attribute).replace("[NaN]", "[]").replace("NaN", "null")
            if (
                attr_type in ITERABLE_TYPES
                and grpc_value
                and (parsed := jsonpickle.decode(grpc_value)) not in ("None", "none")
            ):
                iterations = 0
                while not isinstance(parsed, ITERABLE_TYPES) and iterations <= 5:
                    iterations += 1
                    parsed = jsonpickle.decode(parsed)
                return setattr(self, attribute, parsed)
            if attr_type is not None:
                grpc_value = attr_type(grpc_value)
            return setattr(self, attribute, grpc_value)
