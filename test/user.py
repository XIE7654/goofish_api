from goofish_api import GoofishClient
from test.index import APP_KEY, APP_SECRET


def main():
    # print(APP_KEY, APP_SECRET)
    client = GoofishClient(APP_KEY, APP_SECRET)
    shop = client.user.get_authorize_list()
    print(shop)

if __name__ == "__main__":
    main()
