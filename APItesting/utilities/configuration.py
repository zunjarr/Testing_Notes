import configparser


def getConfig():
    # Read properties.ini file
    config = configparser.ConfigParser()
    path = f'C:/Users/dorugzu/PycharmProjects/pythonProject/APItesting/utilities/properties.ini'
    config.read(f"{path}")

    for api_name in config.sections():
        # print('section name is ', api_name)
        for endpoint in config.options(api_name):
            # print('endpoint value is ', endpoint)
            endpoint_val_from_ini = config.get(api_name, endpoint)
            # print('section_val_from_ini is ', endpoint_val_from_ini)
            return endpoint_val_from_ini


def getAuthUrl():
    config = configparser.ConfigParser()
    path = f'C:/Users/dorugzu/PycharmProjects/pythonProject/APItesting/utilities/properties.ini'
    config.read(f"{path}")

    for AUTH in config.sections():
        # print('section name is ', AUTH)
        for auth_url in config.options(AUTH):
            # print('endpoint value is ', auth_url)
            auth_url_from_ini = config.get(AUTH, auth_url)
            # print('section_val_from_ini is ', section_val_from_ini)
            return auth_url_from_ini


def getToken():
    config = configparser.ConfigParser()
    path = f'C:/Users/dorugzu/PycharmProjects/pythonProject/APItesting/utilities/properties.ini'
    config.read(f"{path}")

    # for TOKEN in config.sections():
        # print('section name is ', TOKEN)
        # if TOKEN=='TOKEN':
    for api_token in config.options("TOKEN"):
        # print('endpoint value is ', api_token)
        api_token_from_ini = config.get("TOKEN", api_token)
        print('section_val_from_ini is ', api_token_from_ini)
        return api_token_from_ini
# getToken()
