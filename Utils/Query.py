# %%
# Imports
from TDA_API_CLIENT import get_client
from tda import client

# %%
# Global Variables

# %%
# Functions


def getCurrentOptionsData(symbol: 'str') -> 'tuple[dict, dict]':
    # Get Client
    user_client = get_client()
    # Query for Option Chain
    response = user_client.get_option_chain(
        symbol=symbol, include_quotes=True, contract_type=client.Client.Options.ContractType.ALL)
    # Check for good response
    assert response.status_code == 200, response.raise_for_status()
    # Return Data
    return response.json()['callExpDateMap'], response.json()['putExpDateMap']

# %%
# Classes

# %%
# Script
