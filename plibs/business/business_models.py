from pydantic import Field
from base.BaseGRPC import BaseGRPC


class BMOutputModel(BaseGRPC):
    NPV_socio_economic: str = Field(default=None)
    IRR_socio_economic: str = Field(default=None)
    Sensitivity_NPV_socio_economic: str = Field(default=None)
    NPV_comm_actor: str = Field(default=None)
    IRR_comm_actor: str = Field(default=None)
    Sensitivity_NPV_comm_actor: str = Field(default=None)
    Discountrate_socio: str = Field(default=None)
    Discountrate_business: str = Field(default=None)
    LCOH_s: str = Field(default=None)


class InternalHeatRecoveryOutputModel(BaseGRPC):
    LCOH_sen: str = Field(default=None)
    NPV_sen: str = Field(default=None)
