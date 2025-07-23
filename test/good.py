import json

from goofish_api import GoofishClient
from goofish_api.utils.constants import ItemBizType, SpBizType
from test.index import APP_KEY, APP_SECRET


def main():
    # print(APP_KEY, APP_SECRET)
    client = GoofishClient(APP_KEY, APP_SECRET)
    # data = client.good.get_product_list()
    res = client.good.get_product_category_list(item_biz_type=2)
    if hasattr(res, 'to_dict'):
        data = res.to_dict()
    elif hasattr(res, '__dict__'):
        data = res.__dict__
    else:
        data = res
    with open('order_list_g.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    # data = client.good.get_product_pv_list(2, 1, '4d8b31d719602249ac899d2620c5df2b')
    print(data)

if __name__ == "__main__":
    main()
