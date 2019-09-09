def limit_depth_of_variables(level_bounds, temperature, depth_limit):
    level_bounds_limited = level_bounds.where(level_bounds < depth_limit, depth_limit)
    delta_level = abs(level_bounds_limited[:, 1] - level_bounds_limited[:, 0])

    delta_level_limited = delta_level.where(delta_level != 0, drop=True)
    temperature_limited = temperature.where(delta_level != 0, drop=True)

    return delta_level_limited, temperature_limited


delta_level_limited, temperature_limited = limit_depth_of_variables(
    ds["lev_bnds"], ds["thetao"], 50
)
delta_level_limited, temperature_limited
