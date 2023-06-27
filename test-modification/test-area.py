from pytest import approx, mark
from math import sqrt
from shadow.polyedr import Polyedr

tests = {
     "cube2": 0,  # центры граней попадают в единичную окружность
     "simple": 4,
     "simple_degenerate": 0,  # поворот на 90
     "simple_30": 2,  # поворот на 60
     "simple_small": 4,  # масштаб не влияет
     "tetrahedron": 4 / 3 * sqrt(3)
}


@mark.parametrize("name,answer", tests.items())
def test_(name, answer):
    assert Polyedr(f"addiotional-data/{name}.geom").area() == approx(answer)
