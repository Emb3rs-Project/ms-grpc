from pydantic import Field
from base.BaseGRPC import BaseGRPC


class BMOutputModel(BaseGRPC):
    NPV_socio_economic: str = Field(default=None)
    IRR_socio_economic: str = Field(default=None)
    Sensitivity_NPV_socio_economic: list = Field(default=None)
    NPV_comm_actor: list = Field(default=None)
    IRR_comm_actor: list = Field(default=None)
    Sensitivity_NPV_comm_actor: list = Field(default=None)
    Discountrate_socio: list = Field(default=None)
    Discountrate_business: list = Field(default=None)
    LCOH_s: list = Field(default=None)


class InternalHeatRecoveryOutputModel(BaseGRPC):
    LCOH_sen: str = Field(default=None)
    NPV_sen: str = Field(default=None)
