""" Module for climatology functions """


def compute_seasonal_climatology(dset):
    """Function to compute seasonal climatologies
    Parameters
    ----------
    dset : xr.Dataset, xr.DataArray
         xarray dataset, or xarray dataarray

    Returns
    -------
    Computed seasonal climatology
    """

    clim = dset.groupby("time.season").mean(dim="time")
    return clim
