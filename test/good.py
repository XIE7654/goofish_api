import json

from goofish_api import GoofishClient
from goofish_api.utils.constants import ItemBizType, SpBizType
from test.index import APP_KEY, APP_SECRET


def main():
    # print(APP_KEY, APP_SECRET)
    client = GoofishClient(APP_KEY, APP_SECRET)
    # data = client.good.get_product_category_list(ItemBizType.COMMON.value)
    data = client.good.get_product_pv_list(2, 1, '4d8b31d719602249ac899d2620c5df2b')
    print(data)

if __name__ == "__main__":
    main()
