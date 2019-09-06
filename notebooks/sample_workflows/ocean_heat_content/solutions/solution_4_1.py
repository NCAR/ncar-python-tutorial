def calc_ocean_heat(delta_level, temperature):
    rho = 1026  # kg/m^3
    c_p = 3990  # J/(kg K)
    weighted_temperature = delta_level * temperature
    heat = weighted_temperature.sum(dim="lev") * rho * c_p
    return heat


heat = calc_ocean_heat(delta_level_limited, temperature_limited)
print(heat)
