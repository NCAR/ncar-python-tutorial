temperature_limited = ds["thetao"].where(delta_level != 0, drop=True)
temperature_limited
