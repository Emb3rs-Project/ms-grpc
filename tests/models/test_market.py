from pathlib import Path

import jsonpickle

from market.market_models import LongTermOutputModel


def __get_result(filename: str):
    with open(f"{Path(__file__).parent.parent}/assets/{filename}") as file:
        result = jsonpickle.decode(file.read())
    return result


def test_long_term_output():
    result = __get_result("result_mm.txt")

    lt1 = LongTermOutputModel().from_grpc(result)
    lt2 = LongTermOutputModel(**lt1.dict())

    assert lt1 == lt2


def test_short_term_output():
    pass
