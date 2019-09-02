"""Module for statistic functions"""


def compute_mean(dset, dims=None):
    """Compute Mean along specified dim
    Parameters
    ----------
    dset : xr.Dataset, xr.DataArray
          xarray dataset or xarray dataarray

    dims : list, default (None)

        list of dimensions to apply mean along

    Returns
    -------
    Dataset/DataArray with mean applied to specified dimensions
    """

    return dset.mean(dim=dims)
