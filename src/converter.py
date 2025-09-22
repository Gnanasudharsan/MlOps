"""
Unit conversion utilities.

Usage:
    convert(60, "mph", "kph") -> 96.56064
    convert(1, "gal", "L")    -> 3.785411784
    convert(0, "C", "F")      -> 32
"""

from typing import Callable, Dict, Tuple

# ---- Aliases (case-insensitive) -> canonical unit codes ----
ALIASES = {
    # length
    "m": "m", "meter": "m", "meters": "m", "metre": "m", "metres": "m",
    "km": "km", "kilometer": "km", "kilometers": "km", "kilometre": "km", "kilometres": "km",
    "mi": "mi", "mile": "mi", "miles": "mi",
    "ft": "ft", "foot": "ft", "feet": "ft",

    # mass
    "kg": "kg", "kilogram": "kg", "kilograms": "kg",
    "g": "g", "gram": "g", "grams": "g",
    "lb": "lb", "lbs": "lb", "pound": "lb", "pounds": "lb",

    # temperature
    "c": "C", "°c": "C", "celsius": "C",
    "f": "F", "°f": "F", "fahrenheit": "F",
    "k": "K", "kelvin": "K",

    # time
    "s": "s", "sec": "s", "secs": "s", "second": "s", "seconds": "s",
    "min": "min", "minute": "min", "minutes": "min",
    "h": "h", "hr": "h", "hour": "h", "hours": "h",

    # speed
    "mps": "mps", "m/s": "mps",
    "kph": "kph", "km/h": "kph", "kmh": "kph",
    "mph": "mph",

    # volume (US gallon)
    "l": "L", "liter": "L", "liters": "L", "litre": "L", "litres": "L",
    "ml": "mL", "milliliter": "mL", "milliliters": "mL", "millilitre": "mL", "millilitres": "mL",
    "gal": "gal", "gallon": "gal", "gallons": "gal",

    # area
    "sqm": "sqm", "m^2": "sqm", "square_meter": "sqm", "square_meters": "sqm",
    "sqft": "sqft", "ft^2": "sqft", "square_foot": "sqft", "square_feet": "sqft",
    "acre": "acre", "acres": "acre",
}

def _canon(unit: str) -> str:
    if not isinstance(unit, str):
        raise ValueError("Unit must be a string.")
    key = unit.strip().lower()
    if key not in ALIASES:
        raise ValueError(f"Unknown unit: {unit}")
    return ALIASES[key]

def _is_number(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)

# Base units:
#   length: meter (m)
#   mass: kilogram (kg)
#   temperature: Kelvin (K)
#   time: second (s)
#   speed: meter/second (mps)
#   volume: liter (L)
#   area: square meter (sqm)
UNITS: Dict[str, Tuple[str, Callable[[float], float], Callable[[float], float]]] = {
    # length
    "m":   ("length", lambda v: v,                lambda v: v),
    "km":  ("length", lambda v: v * 1000.0,       lambda v: v / 1000.0),
    "mi":  ("length", lambda v: v * 1609.344,     lambda v: v / 1609.344),
    "ft":  ("length", lambda v: v * 0.3048,       lambda v: v / 0.3048),

    # mass
    "kg":  ("mass",   lambda v: v,                lambda v: v),
    "g":   ("mass",   lambda v: v * 0.001,        lambda v: v / 0.001),
    "lb":  ("mass",   lambda v: v * 0.45359237,   lambda v: v / 0.45359237),

    # temperature (base = K)
    "K":   ("temperature", lambda v: v,                           lambda v: v),
    "C":   ("temperature", lambda v: v + 273.15,                  lambda v: v - 273.15),
    "F":   ("temperature", lambda v: (v - 32.0) * 5.0/9.0 + 273.15,
                                 lambda v: (v - 273.15) * 9.0/5.0 + 32.0),

    # time
    "s":   ("time",   lambda v: v,                lambda v: v),
    "min": ("time",   lambda v: v * 60.0,         lambda v: v / 60.0),
    "h":   ("time",   lambda v: v * 3600.0,       lambda v: v / 3600.0),

    # speed (base = mps)
    "mps": ("speed",  lambda v: v,                lambda v: v),
    "kph": ("speed",  lambda v: v * (1000.0/3600.0), lambda v: v / (1000.0/3600.0)),
    "mph": ("speed",  lambda v: v * 0.44704,      lambda v: v / 0.44704),

    # volume (US gallon)
    "L":   ("volume", lambda v: v,                lambda v: v),
    "mL":  ("volume", lambda v: v * 0.001,        lambda v: v / 0.001),
    "gal": ("volume", lambda v: v * 3.785411784,  lambda v: v / 3.785411784),

    # area
    "sqm": ("area",   lambda v: v,                lambda v: v),
    "sqft":("area",   lambda v: v * 0.09290304,   lambda v: v / 0.09290304),
    "acre":("area",   lambda v: v * 4046.8564224, lambda v: v / 4046.8564224),
}

def _category(unit: str) -> str:
    return UNITS[unit][0]

def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert 'value' from 'from_unit' to 'to_unit'.

    Raises:
        ValueError: if value is not numeric, units are unknown, or categories differ.
    """
    if not _is_number(value):
        raise ValueError("Value must be a number (int or float).")
    f = _canon(from_unit)
    t = _canon(to_unit)
    if f not in UNITS or t not in UNITS:
        raise ValueError("Unsupported unit.")
    if _category(f) != _category(t):
        raise ValueError(f"Incompatible categories: {from_unit} -> {to_unit}")
    to_base = UNITS[f][1]
    from_base = UNITS[t][2]
    base_val = to_base(float(value))
    return from_base(base_val)
