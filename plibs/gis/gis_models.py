from email.policy import default
from typing import Dict, Any

from pydantic import Field
from base.BaseGRPC import BaseGRPC


class CreateNetworkOutputModel(BaseGRPC):
    edges: list = Field(default=[])
    nodes: list = Field(default=[])
    demand_list: list = Field(default=[])
    supply_list: list = Field(default=[])


class OptimizeNetworkOutputModel(BaseGRPC):
    res_sources_sinks: list = Field(default=[])
    sums: Dict[str, Any] = Field(default={})
    losses_cost_kw: Dict[str, Any] = Field(default={})
    network_solution_nodes: list = Field(default=[])
    network_solution_edges: list = Field(default=[])
    potential_edges: list = Field(default=[])
    potential_nodes: list = Field(default=[])
    selected_agents: list = Field(default=[])
    report: str = Field(default="")


# string res_sources_sinks = 1;
# string sums = 2;
# string losses_cost_kw = 3;
# string network_solution_nodes = 4;
# string network_solution_edges = 5;
# string potential_edges = 6;
# string potential_nodes = 7;
# string selected_agents = 8;
# string report = 9;
