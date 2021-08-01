# %% Imports
from functools import wraps
import time

# %% Global Variables

# %% Functions


def _time(Original_Function):

    @wraps(Original_Function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = Original_Function(*args, **kwargs)
        print(f'{Original_Function.__name__} ran in {time.time() - t1}')
        return result

    return wrapper


# %% Classes

# %% Script


# %% Tests

# %%
