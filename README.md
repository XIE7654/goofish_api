# Goofish API

Python SDK for interacting with the Goofish API.

```shell
# 安装
pip install goofish_api
```

```python
# 使用
from goofish_api import GoofishClient
APP_KEY = ''
APP_SECRET = ''
client = GoofishClient(APP_KEY, APP_SECRET)
data = client.user.get_authorize_list()
print(data)
data = client.good.get_product_pv_list(2, 1, '4d8b31d719602249ac899d2620c5df2b')
print(data)
```