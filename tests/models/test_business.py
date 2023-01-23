from pathlib import Path

import jsonpickle

from business.business_models import BMOutputModel


def test_bm_output():
    with open(f"{Path(__file__).parent.parent}/assets/result_bm.txt") as file:
        result = jsonpickle.decode(file.read())

    f1 = BMOutputModel().from_grpc(result)
    f2 = BMOutputModel(**f1.dict())

    assert f1 == f2
