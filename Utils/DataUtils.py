# %% Imports
from pandas import DataFrame
from pickle import load, dump

# %% Global Variables

# %% Functions


def DSave(Obj: 'object', Path: 'str', Name: 'str') -> 'None':
    with open(f'{Path}\\{Name}', 'wb') as f:
        dump(Obj, f)


def DLoad(Path: 'str', Name: 'str') -> 'object':
    with open(f'{Path}\\{Name}', 'rb') as f:
        return load(f)


def BeautifyChain(Chain: 'dict') -> 'DataFrame':
    return DataFrame.from_dict(Chain).rename(columns=lambda x: x[:10])
# %% Classes


# %% Script

# %% Tests
