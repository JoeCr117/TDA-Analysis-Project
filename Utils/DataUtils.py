# %%
# Imports
import pandas as pd
import json
from pickle import load, dump

# %%
# Global Variables

# %%
# Functions


def DSave(Obj: 'object', Path: 'str', Name: 'str') -> 'None':
    with open(f'{Path}\\{Name}', 'wb') as f:
        dump(Obj, f)


def DLoad(Path: 'str', Name: 'str') -> 'object':
    with open(f'{Path}\\{Name}', 'rb') as f:
        return load(f)


def JsonToOptionChainDF(RawJson: 'json') -> 'pd.DataFrame':
    frame = pd.json_normalize(RawJson)
    return frame
# %%
# Classes


# %%
# Script
# %%
