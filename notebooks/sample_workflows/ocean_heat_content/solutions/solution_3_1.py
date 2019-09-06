theatao_point = ds['thetao'][0]

orig_units = cf.Unit(thetao_point.attrs['units'])

target_units = cf.Unit('degK)
orig_units.convert(thetao_point, target_units)