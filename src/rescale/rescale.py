import numpy as np


def rescale(input_array: np.ndarray) -> np.ndarray:
    """Linearly rescale an array to the range [0, 1].

    Maps the minimum value of the input to 0 and the maximum to 1,
    scaling all other values proportionally in between.

    Parameters
    ----------
    input_array : numpy.ndarray
        The array of values to rescale.

    Returns
    -------
    numpy.ndarray
        An array the same shape as ``input_array``, with values
        linearly mapped onto the interval [0, 1].

    Examples
    --------
    >>> import numpy as np
    >>> rescale(np.array([1, 2, 3, 4, 5]))
    array([0.  , 0.25, 0.5 , 0.75, 1.  ])
    """
    L = np.min(input_array)
    H = np.max(input_array)
    output_array = (input_array - L) / (H - L)
    return output_array
