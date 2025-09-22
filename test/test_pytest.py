import pytest
from math import isclose
from src.converter import convert

# --- length ---
@pytest.mark.parametrize("v,fu,tu,exp", [
    (1, "km", "m", 1000.0),
    (1, "mi", "km", 1.609344),
    (10, "ft", "m", 3.048),
])
def test_length(v, fu, tu, exp):
    assert isclose(convert(v, fu, tu), exp, rel_tol=1e-9, abs_tol=1e-12)

# --- mass ---
@pytest.mark.parametrize("v,fu,tu,exp", [
    (1, "kg", "g", 1000.0),
    (1, "lb", "kg", 0.45359237),
])
def test_mass(v, fu, tu, exp):
    assert isclose(convert(v, fu, tu), exp, rel_tol=1e-12, abs_tol=1e-12)

# --- temperature ---
@pytest.mark.parametrize("v,fu,tu,exp", [
    (0, "C", "F", 32.0),
    (212, "F", "K", 373.15),
    (273.15, "K", "C", 0.0),
])
def test_temperature(v, fu, tu, exp):
    assert isclose(convert(v, fu, tu), exp, rel_tol=1e-10, abs_tol=1e-10)

# --- time ---
@pytest.mark.parametrize("v,fu,tu,exp", [
    (2, "h", "min", 120.0),
    (90, "min", "h", 1.5),
    (30, "s", "min", 0.5),
])
def test_time(v, fu, tu, exp):
    assert isclose(convert(v, fu, tu), exp, rel_tol=1e-12, abs_tol=1e-12)

# --- speed ---
@pytest.mark.parametrize("v,fu,tu,exp", [
    (60, "mph", "kph", 96.56064),
    (100, "kph", "mps", 27.7777777778),
    (10, "mps", "mph", 22.3693629205),
])
def test_speed(v, fu, tu, exp):
    assert isclose(convert(v, fu, tu), exp, rel_tol=1e-9, abs_tol=1e-9)

# --- volume ---
@pytest.mark.parametrize("v,fu,tu,exp", [
    (1, "gal", "L", 3.785411784),
    (500, "mL", "L", 0.5),
])
def test_volume(v, fu, tu, exp):
    assert isclose(convert(v, fu, tu), exp, rel_tol=1e-12, abs_tol=1e-12)

# --- area ---
@pytest.mark.parametrize("v,fu,tu,exp", [
    (10, "sqft", "sqm", 0.9290304),
    (1, "acre", "sqm", 4046.8564224),
])
def test_area(v, fu, tu, exp):
    assert isclose(convert(v, fu, tu), exp, rel_tol=1e-12, abs_tol=1e-12)

# --- errors ---
@pytest.mark.parametrize("v,fu,tu", [
    (1, "m", "kg"),   # cross-category
    (1, "nope", "m"), # unknown unit
    ("x", "m", "km"), # non-numeric value
])
def test_errors(v, fu, tu):
    with pytest.raises(ValueError):
        convert(v, fu, tu)
