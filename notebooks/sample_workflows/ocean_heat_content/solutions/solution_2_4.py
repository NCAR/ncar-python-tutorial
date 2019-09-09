level_bounds_limited = ds['lev_bnds'].where(ds['lev_bnds'] < 100, drop = True)
level_bounds_limited.values