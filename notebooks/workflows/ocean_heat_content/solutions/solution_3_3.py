level_bounds_in_m = change_units(ds, "lev", "lev_bnds", "m")
temperature_in_K = change_units(ds, "thetao", "thetao", "degK")
print(level_bounds_in_m, temperature_in_K)
