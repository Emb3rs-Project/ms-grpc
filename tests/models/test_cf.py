from pathlib import Path

import jsonpickle

from cf.cf_models import ConvertSinkOutputModel, ConvertSourceOutputModel


def __get_result(filename: str):
    with open(f"{Path(__file__).parent.parent}/assets/{filename}") as file:
        result = jsonpickle.decode(file.read())
    return result


def test_convert_sink_output():
    result = __get_result("result_cf_sink.txt")

    cf1 = ConvertSinkOutputModel().from_grpc(result)
    cf2 = ConvertSinkOutputModel(**cf1.dict())

    assert cf1 == cf2


def test_convert_source_output():
    result = __get_result("result_cf_source.txt")

    cf3 = ConvertSourceOutputModel().from_grpc(result)
    cf4 = ConvertSourceOutputModel(**cf3.dict())

    assert cf3.all_sources_info == cf4.all_sources_info
    assert cf3.ex_grid == cf4.ex_grid
    assert cf3.teo_string == cf4.teo_string
    assert cf3.input_fuel == cf4.input_fuel
    assert cf3.output_fuel == cf4.output_fuel
    assert cf3.output == cf4.output
    assert cf3.input == cf4.input
    assert cf3.n_supply_list == cf4.n_supply_list
    assert len(cf3.teo_capacity_factor_group) == len(cf4.teo_capacity_factor_group)
    assert cf3.teo_dhn == cf4.teo_dhn
