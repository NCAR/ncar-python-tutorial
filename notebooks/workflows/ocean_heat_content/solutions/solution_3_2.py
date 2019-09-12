def change_units(ds, variable_str, variable_bounds_str, target_unit_str):
    orig_units = cf.Unit(ds[variable_str].attrs["units"])
    target_units = cf.Unit(target_unit_str)
    variable_in_new_units = xr.apply_ufunc(
        orig_units.convert,
        ds[variable_bounds_str],
        target_units,
        output_dtypes=[ds[variable_bounds_str].dtype],
    )
    return variable_in_new_units
