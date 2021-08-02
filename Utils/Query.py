# %% Imports
from tda import client

# %% Global Variables

# %% Functions


def getCurrentOptionsData(user_client: 'client.Client|client.AsyncClient', symbol: 'str') -> 'tuple[dict, dict]':
    # Query for Option Chain
    response = user_client.get_option_chain(
        symbol=symbol, include_quotes=True, contract_type=client.Client.Options.ContractType.ALL)
    # Check for good response
    assert response.status_code == 200, response.raise_for_status()
    # Return Data
    return response.json()['callExpDateMap'], response.json()['putExpDateMap']


def getAccountData(user_client: 'client.Client|client.AsyncClient') -> 'dict':
    # Query for Account Data
    response = user_client.get_account(account_id=user_client.get_user_principals().json()['accounts'][0]['accountId'],
                                       fields=client.Client.Account.Fields.POSITIONS)

    assert response.status_code == 200, response.raise_for_status()
    return response.json()

# %% Classes

# %% Script

# %% Tests
