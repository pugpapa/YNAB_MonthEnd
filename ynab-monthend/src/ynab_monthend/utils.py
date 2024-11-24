from ynab_api import ApiClient

key_path =

def get_key(filepath: str) -> str:
    "Read the path and get the key"
    return open(filepath).read()

def ynab_connect():
    ApiClient()
    get_key(key_path)