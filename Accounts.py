import requests


def getAllAccounts():
    account_list = requests.get('').json()

    return account_list


def getUSERS():
    account_list = getAllAccounts()

    USERS = {}

    for account in account_list:
        if account['enable']:
            USERS[account['secret'][2:34]] = account['secret'][2:34]

    return USERS


def get_USER_MAX_TCP_CONNS():
    account_list = getAllAccounts()

    USERS = {}

    for account in account_list:
        if account['enable']:
            USERS[account['secret'][2:34]] = account['connection']

    return USERS


if __name__ == '__main__':
    print(get_USER_MAX_TCP_CONNS())
