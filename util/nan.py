import numpy as NP


def nan_helper(y):
    """
    Helper to handle indices and logical indices of NaNs.

    Input:
        - y, 1d numpy array with possible NaNs
    Output:
        - nans, logical indices of NaNs
        - index, a function, with signature indices= index(logical_indices),
          to convert logical indices of NaNs to 'equivalent' indices
    Example:
        >>> # linear interpolation of NaNs
        >>> nans, x= nan_helper(y)
        >>> y[nans]= NP.interp(x(nans), x(~nans), y[~nans])

    Source: http://stackoverflow.com/questions/6518811/interpolate-nan-values-in-a-numpy-array
    """
    return NP.isnan(y), lambda z: z.nonzero()[0]


def nan_interp(y):
    """
    Return a new array with nans found in *y* filled with linear
    interpolants.
    """
    nans, x = nan_helper(y)
    z = NP.array(y)
    z[nans]= NP.interp(x(nans), x(~nans), z[~nans])
    return z
