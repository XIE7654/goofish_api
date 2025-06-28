from goofish_api import GoofishClient
from test.index import APP_KEY, APP_SECRET


def main():
    client = GoofishClient(APP_KEY, APP_SECRET)
    shop = client.user.get_authorize_list()
    express = client.other.get_express_companies()
    orders = client.order.get_order_list()
    print(shop)
    print(express)
    print(orders)

if __name__ == "__main__":
    main()
