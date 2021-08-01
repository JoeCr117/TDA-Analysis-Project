# %%
# Imports
from tda import auth
from json import load
from os.path import dirname

# %%
# Functions


def get_client():
    with open(f'{dirname(__file__)}\\credentials.json') as credentials:
        creds = load(credentials)
        api_key = creds['api_key']
        redirect_uri = creds['redirect_uri']

    try:
        c = auth.client_from_token_file(
            f'{dirname(__file__)}\\authToken.pickle', api_key)
    except FileNotFoundError:
        from selenium import webdriver
        with webdriver.Firefox() as driver:
            c = auth.client_from_login_flow(
                driver, api_key, redirect_uri, f'{dirname(__file__)}\\authToken.pickle')
    return c
