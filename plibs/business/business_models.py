

import pydantic


class BMOutputModel(pydantic.BaseModel):
    NPV_socio_economic: str = pydantic.Field(default=None)
    IRR_socio_economic: str = pydantic.Field(default=None)
    Sensitivity_NPV_socio_economic: str = pydantic.Field(default=None)
    NPV_comm_actor: str = pydantic.Field(default=None)
    IRR_comm_actor: str = pydantic.Field(default=None)
    Sensitivity_NPV_comm_actor: str = pydantic.Field(default=None)
    Discountrate_socio: str = pydantic.Field(default=None)
    Discountrate_business: str = pydantic.Field(default=None)
    LCOH_s: str = pydantic.Field(default=None)


class InternalHeatRecoveryOutputModel(pydantic.BaseModel):
    LCOH_sen: str = pydantic.Field(default=None)
    NPV_sen: str = pydantic.Field(default=None)
