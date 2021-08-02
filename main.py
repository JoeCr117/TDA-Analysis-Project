# %% Imports
import Utils
from TDA_API_CLIENT import get_client

# %% Global Variables
USER_CLIENT = get_client()

# %% Functions

# %% Classes

# %% Script

# %% Tests
calls, puts = map(Utils.BeautifyChain,
                  Utils.getCurrentOptionsData(USER_CLIENT, 'FUBO'))

account_data = Utils.getAccountData(USER_CLIENT)
# %%
