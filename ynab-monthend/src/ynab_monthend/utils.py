import os
import tomllib
from ynab_api import ApiClient
from todoist_api_python.api_async import TodoistAPIAsync
from todoist_api_python.api import TodoistAPI
from requests_oauthlib import OAuth2Session


TODOIST_CONFIG = '~/.todoist.toml'
YNAB_API_KEY = '~/.ynab.toml'

def ynab_connect():
    return ApiClient(open(os.path.expanduser('~/.ynab')).read().strip())

    
def todoist_connect():
    todoist_config = tomllib.load(open(TODOIST_CONFIG, mode='rb'))
    client_id = todoist_config['client_id']
    client_secret = todoist_config['client_secret']
    scope = 'data:read_write'
    ro.OAuth2()
    auth_url = "https://todoist.com/oauth/authorize"
    return TodoistAPI(open(os.path.expanduser('~/.todoist')).read().strip())