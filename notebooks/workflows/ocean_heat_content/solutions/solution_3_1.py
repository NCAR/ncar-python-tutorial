thetao_point = ds['thetao'].isel(time=0, lev = 0, lat = 30, lon=30)

orig_units = cf.Unit(thetao_point.attrs['units'])

target_units = cf.Unit('degK')
orig_units.convert(thetao_point, target_units)