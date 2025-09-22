import pytest
from src.calculator import fun1, fun2, fun3, fun4, safe_divide, power

@pytest.mark.parametrize("x,y,expected", [(2,3,5), (-1,1,0), (2.5,0.5,3.0)])
def test_fun1(x, y, expected):
    assert fun1(x, y) == expected

@pytest.mark.parametrize("x,y,expected", [(5,3,2), (-1,-1,0), (2.5,0.5,2.0)])
def test_fun2(x, y, expected):
    assert fun2(x, y) == expected

@pytest.mark.parametrize("x,y,expected", [(2,3,6), (-2,3,-6), (2.5,2,5.0)])
def test_fun3(x, y, expected):
    assert fun3(x, y) == expected

def test_fun4_metrics_dict():
    out = fun4(1, 2, 3)
    assert isinstance(out, dict)
    assert out["sum"] == 6
    assert out["mean"] == 2
    assert out["min"] == 1
    assert out["max"] == 3
    assert out["range"] == 2

@pytest.mark.parametrize("badx,bady", [("2",3), (2,"3"), (None,1), (True,2), (2,False)])
def test_fun1_type_errors(badx, bady):
    with pytest.raises(ValueError):
        fun1(badx, bady)

@pytest.mark.parametrize("badx,bady", [("2",3), (2,"3"), (None,1), (True,2), (2,False)])
def test_fun2_type_errors(badx, bady):
    with pytest.raises(ValueError):
        fun2(badx, bady)

@pytest.mark.parametrize("badx,bady", [("2",3), (2,"3"), (None,1), (True,2), (2,False)])
def test_fun3_type_errors(badx, bady):
    with pytest.raises(ValueError):
        fun3(badx, bady)

def test_safe_divide_ok():
    assert safe_divide(9, 3) == 3

def test_safe_divide_zero():
    with pytest.raises(ZeroDivisionError):
        safe_divide(1, 0)

def test_power():
    assert power(2, 4) == 16
    assert power(3, 2) == 9
