## 如果这个项目让你有所收获，记得 Star 关注哦，这对我是非常不错的鼓励与支持。

# Goofish API Python SDK

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Goofish API Python SDK 是一个用于闲鱼开放平台的Python客户端库，提供了完整的API封装，支持商品管理、订单处理、用户授权等功能。

## 功能特性

- 🚀 **完整的API覆盖** - 支持闲鱼开放平台的所有主要API
- 🔐 **自动签名验证** - 内置MD5签名算法，无需手动处理
- 📦 **模块化设计** - 按功能模块组织代码，易于使用和维护
- 🛡️ **类型安全** - 使用枚举类型确保参数正确性
- 📝 **详细文档** - 每个API都有详细的参数说明和示例

## 支持的API模块

- **用户模块** - 店铺授权管理
- **商品模块** - 商品CRUD操作、类目管理、属性查询
- **订单模块** - 订单查询、发货处理、卡密管理
- **其他模块** - 快递公司查询等

## 安装

### 从PyPI安装

```bash
pip install goofish-api
```

## 依赖要求

- Python 3.7+
- requests >= 2.26.0
- python-dotenv >= 0.20.0

## 快速开始
### 1. 基本使用

```python
from goofish_api import GoofishClient

APP_KEY = ''
APP_SECRET = ''
# 初始化客户端
client = GoofishClient(
    app_key=APP_KEY,
    app_secret=APP_SECRET
)


# 查询授权店铺
response = client.user.get_authorize_list()
print(response)
```

## API 使用示例

### 用户模块

#### 查询授权店铺

```python
# 获取已授权的闲鱼店铺列表
response = client.user.get_authorize_list()
print(response)
```

### 商品模块

#### 查询商品类目

```python
from goofish_api.utils.constants import ItemBizType, SpBizType

# 查询普通商品的手机类目
response = client.good.get_product_category_list(
    item_biz_type=ItemBizType.COMMON,
    sp_biz_type=SpBizType.MOBILE
)
print(response)
```

#### 查询商品属性

```python
# 查询指定类目的商品属性
response = client.good.get_product_pv_list(
    item_biz_type=ItemBizType.COMMON,
    sp_biz_type=SpBizType.MOBILE,
    channel_cat_id="4d8b31d719602249ac899d2620c5df2b"
)
print(response)
```

#### 查询商品列表

```python
from goofish_api.utils.constants import ProductStatus, SaleStatus

# 查询销售中的商品
response = client.good.get_product_list(
    product_status=ProductStatus.STATUS_21,
    sale_status=SaleStatus.ON_SALE,
    page_no=1,
    page_size=20
)
print(response)
```

#### 查询商品详情

```python
# 根据商品ID查询详情
response = client.good.get_product_detail(product_id=1234567890)
print(response)
```

#### 创建商品

```python
# 创建单个商品
product_data = {
    "item_biz_type": 2,
    "sp_biz_type": 1,
    "channel_cat_id": "e11455b218c06e7ae10cfa39bf43dc0f",
    "channel_pv": [
        {
            "property_id": "b5e5462c028aba7f1921b9e373cead75",
            "property_name": "交易形式",
            "value_id": "8a3445658e0bc44687b43d68bdc44732",
            "value_name": "代下单"
        }
    ],
    "price": 550000,  # 价格（分）
    "original_price": 700000,
    "express_fee": 10,
    "stock": 10,
    "outer_id": "2021110112345",
    "stuff_status": 100,
    "publish_shop": [
        {
            "images": ["https://example.com/image1.jpg"],
            "user_name": "闲鱼会员名",
            "province": 130000,
            "city": 130100,
            "district": 130101,
            "title": "商品标题",
            "content": "商品描述",
            "service_support": "SDR"
        }
    ]
}

response = client.good.create_product(product_data=product_data)
print(response)
```

#### 批量创建商品

```python
# 批量创建商品
product_list = [product_data1, product_data2, product_data3]
response = client.good.product_batch_create(product_data=product_list)
print(response)
```

#### 发布商品

```python
# 发布商品到闲鱼
response = client.good.product_publish(
    product_id=1234567890,
    user_name=["闲鱼会员名1", "闲鱼会员名2"]
)
print(response)
```

#### 下架商品

```python
# 下架商品
response = client.good.product_down_shelf(product_id=1234567890)
print(response)
```

#### 编辑商品

```python
# 编辑商品信息
edit_data = {
    "product_id": 1234567890,
    "title": "新的商品标题",
    "price": 600000,
    "stock": 20
}
response = client.good.product_edit(product_data=edit_data)
print(response)
```

#### 修改库存

```python
# 修改商品库存和价格
response = client.good.product_edit_stock(
    product_id=1234567890,
    price=600000,
    stock=15
)
print(response)
```

#### 删除商品

```python
# 删除商品
response = client.good.product_delete(product_id=1234567890)
print(response)
```

### 订单模块

#### 查询订单列表

```python
from goofish_api.utils.constants import OrderStatus, RefundStatus

# 查询待发货订单
response = client.order.get_order_list(
    order_status=OrderStatus.PENDING_SHIPMENT,
    page_no=1,
    page_size=20
)
print(response)
```

#### 查询订单详情

```python
# 根据订单号查询详情
response = client.order.get_order_detail(order_no="1339920336328048683")
print(response)
```

#### 查询订单卡密

```python
# 查询订单的卡密信息
response = client.order.kam_order_list(order_no="1339920336328048683")
print(response)
```

#### 订单发货

```python
# 订单物流发货
response = client.order.order_ship(
    order_no="1339920336328048683",
    ship_name="张三",
    ship_mobile="13800138000",
    ship_district_id=440305,
    ship_prov_name="广东省",
    ship_city_name="深圳市",
    ship_area_name="南山区",
    waybill_no="25051016899982",
    express_name="其他",
    express_code="qita"
)
print(response)
```

### 其他模块

#### 查询快递公司

```python
# 获取支持的快递公司列表
response = client.other.get_express_companies()
print(response)
```

## 常量枚举

SDK提供了丰富的枚举类型，确保API调用的参数正确性：

### 商品类型 (ItemBizType)

```python
from goofish_api.utils.constants import ItemBizType

ItemBizType.COMMON          # 普通商品
ItemBizType.INSPECTED       # 已验货
ItemBizType.INSPECTION_BAO  # 验货宝
ItemBizType.BRAND_AUTH      # 品牌授权
ItemBizType.XIAN_YU_SELECTED # 闲鱼严选
ItemBizType.XIAN_YU_FLASH   # 闲鱼特卖
ItemBizType.BRAND_PICK      # 品牌捡漏
```

### 行业类型 (SpBizType)

```python
from goofish_api.utils.constants import SpBizType

SpBizType.MOBILE        # 手机
SpBizType.TREND         # 潮品
SpBizType.HOME_APPLIANCE # 家电
SpBizType.DIGITAL       # 3C数码
SpBizType.LUXURY        # 奢品
SpBizType.MATERNAL      # 母婴
SpBizType.BEAUTY        # 美妆个护
# ... 更多类型
```

### 订单状态 (OrderStatus)

```python
from goofish_api.utils.constants import OrderStatus

OrderStatus.PENDING_PAYMENT    # 待付款
OrderStatus.PENDING_SHIPMENT   # 待发货
OrderStatus.SHIPPED           # 已发货
OrderStatus.TRANSACTION_SUCCESS # 交易成功
OrderStatus.REFUNDED          # 已退款
OrderStatus.TRANSACTION_CLOSED # 交易关闭
```

### 退款状态 (RefundStatus)

```python
from goofish_api.utils.constants import RefundStatus

RefundStatus.NOT_APPLIED                    # 未申请退款
RefundStatus.PENDING_SELLER_APPROVAL        # 待商家处理
RefundStatus.PENDING_BUYER_RETURN           # 待买家退货
RefundStatus.PENDING_SELLER_RECEIVE         # 待商家收货
RefundStatus.REFUND_CLOSED                  # 退款关闭
RefundStatus.REFUND_SUCCESS                 # 退款成功
RefundStatus.REFUND_REJECTED                # 已拒绝退款
RefundStatus.PENDING_RETURN_ADDRESS_CONFIRMATION # 待确认退货地址
```

## 错误处理

SDK会自动处理API响应，返回统一的响应格式：

```python
response = client.user.get_authorize_list()

if response.success:
    print("请求成功:", response.data)
else:
    print("请求失败:", response.message)
    print("错误代码:", response.code)
```

## 调试模式

启用调试模式可以查看详细的请求和响应信息：

```python
client = GoofishClient(
    app_key="your_app_key",
    app_secret="your_app_secret",
    debug=True  # 启用调试模式
)
```

## 测试示例

项目包含完整的测试示例，位于 `test/` 目录：

```bash
# 运行测试
cd test
python go.py
```

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 作者

- **XIE JUN** - [xie7654](https://github.com/xie7654)
- 邮箱: xie765462425@gmail.com，765462425@qq.com

## 相关链接

- [闲鱼开放平台文档](https://open.goofish.pro)
- [GitHub 仓库](https://github.com/xie7654/goofish_api)
- [PyPI 包](https://pypi.org/project/goofish-api/)

---

如有问题或建议，请通过GitHub Issues联系我们。或qq：765462425 wx：JUN765462425