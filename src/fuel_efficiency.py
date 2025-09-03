import statistics

def calculate_fuel_efficiency(distance_km: float, fuel_liters: float) -> float:
    if fuel_liters <= 0:
        return 0
    return round(distance_km / fuel_liters, 2)

def average_efficiency(trips: list[tuple[float, float]]) -> float:
    efficiencies = [calculate_fuel_efficiency(d, f) for d, f in trips if f > 0]
    return round(statistics.mean(efficiencies), 2) if efficiencies else 0

def best_trip(trips: list[tuple[float, float]]) -> tuple[float, float, float]:
    if not trips:
        return (0, 0, 0)
    effs = [(d, f, calculate_fuel_efficiency(d, f)) for d, f in trips if f > 0]
    return max(effs, key=lambda x: x[2], default=(0, 0, 0))
