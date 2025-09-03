import pytest
from src.fuel_efficiency import calculate_fuel_efficiency, average_efficiency, best_trip

def test_calculate_normal_case():
    assert calculate_fuel_efficiency(500, 25) == 20.0

def test_calculate_zero_fuel():
    assert calculate_fuel_efficiency(100, 0) == 0

def test_calculate_rounding():
    assert calculate_fuel_efficiency(100, 3) == 33.33

def test_average_efficiency():
    trips = [(100, 5), (200, 10), (300, 20)]  # 20, 20, 15
    assert average_efficiency(trips) == 18.33

def test_average_efficiency_with_invalid_trip():
    trips = [(100, 0), (200, 10)]
    assert average_efficiency(trips) == 20.0

def test_best_trip():
    trips = [(100, 5), (300, 20), (50, 2)]
    assert best_trip(trips) == (100, 5, 20.0)

def test_best_trip_empty():
    assert best_trip([]) == (0, 0, 0)
