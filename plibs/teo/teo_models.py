from typing import Dict, Any
from pydantic import Field
from base.BaseGRPC import BaseGRPC

class BuildModelOutputModel(BaseGRPC):
  Cost: list = Field(default=[])
  AccumulatedNewCapacity: list = Field(default=[])
  AccumulatedNewStorageCapacity: list = Field(default=[])
  AnnualTechnologyEmission: list = Field(default=[])
  ProductionByTechnology: list = Field(default=[])
  StorageLevelTimesliceStart: list = Field(default=[])
  TotalEmissions: list = Field(default=[])
  DiscountedCapitalInvestmentByTechnology: list = Field(default=[])
  DiscountedCapitalInvestmentByStorage: list = Field(default=[])
  DiscountedSalvageValueByTechnology: list = Field(default=[])
  DiscountedSalvageValueByStorage: list = Field(default=[])
  TotalDiscountedFixedOperatingCost: list = Field(default=[])
  VariableOMCost: list = Field(default=[])
  ex_capacities: list = Field(default=[])
  report: str = Field(default="")