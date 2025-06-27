from goofish_api.api.base import BaseAPI
from goofish_api.utils.api_response import ApiResponse
from goofish_api.utils.constants import ItemBizType, SpBizType, FlashSaleType, ProductStatus, SaleStatus
from goofish_api.utils.helpers import action


class Good(BaseAPI):

    @action("/api/open/product/category/list")
    def get_product_category_list(self, item_biz_type: ItemBizType, sp_biz_type: SpBizType = None,
                             flash_sale_type: FlashSaleType = None, **kwargs) -> ApiResponse:
        """ 查询商品类目
        :param item_biz_type: 商品类型（必需）
        :param sp_biz_type: 行业类型 (可选)
        :param flash_sale_type: 闲鱼特卖类型 (可选)
        示例：
        {
            "item_biz_type": 2,
            "sp_biz_type": 2
        }
        """
        data = {
            "item_biz_type": item_biz_type,
            "sp_biz_type": sp_biz_type,
            "flash_sale_type": flash_sale_type
        }
        return self._request(data={**kwargs, **data})

    @action('/api/open/product/pv/list')
    def get_product_pv_list(self, item_biz_type: ItemBizType, sp_biz_type: SpBizType,
                            channel_cat_id: int, sub_property_id: int = '', **kwargs) -> ApiResponse:
        """ 查询商品属性
        :param item_biz_type: 商品类型（必需）
        :param sp_biz_type: 行业类型（必需）
        :param channel_cat_id: 渠道类目ID（必需）
        :param sub_property_id: 属性值ID (可选)
        示例：
        {
            "channel_cat_id":"4d8b31d719602249ac899d2620c5df2b",
            "sub_property_id": "",
            "item_biz_type":2,
            "sp_biz_type":1
        }
        """
        data = {
            "item_biz_type": item_biz_type,
            "sp_biz_type": sp_biz_type,
            "channel_cat_id": channel_cat_id,
            "sub_property_id": sub_property_id,
        }
        return self._request(data={**kwargs, **data})

    @action('/api/open/product/list')
    def get_product_list(self, online_time: [], offline_time: [], sold_time: [], update_time: [], create_time: [],
                         product_status: ProductStatus, sale_status: SaleStatus, page_no: int = 1,
                         page_size: int = 50, **kwargs):
        """ 查询商品列表
        :param online_time: 商品上架时间 第一个元素值为开始时间戳,第二个元素值为结束时间戳
        :param offline_time: 商品下架时间
        :param sold_time: 商品售罄时间
        :param update_time: 商品更新时间
        :param create_time: 商品创建时间
        :param product_status: 商品状态
        :param sale_status: 商品销售状态
        :param page_no: 页码 >= 1 <= 100
        :param page_size: 每页数量 >= 1 <= 100
        示例：
        {
            "online_time": [
                1690300800,
                1690366883
            ],
            "offline_time": [
                1690300800,
                1690366883
            ],
            "sold_time": [
                1690300800,
                1690366883
            ],
            "update_time": [
                1690300800,
                1690366883
            ],
            "create_time": [
                1690300800,
                1690366883
            ],
            "product_status": 21,
            "page_no": 1,
            "page_size": 50
        }
        """
        data = {
            'online_time': online_time,
            'offline_time': offline_time,
            'sold_time': sold_time,
            'update_time': update_time,
            'create_time': create_time,
            'product_status': product_status,
            'sale_status': sale_status,
            'page_no': page_no,
            'page_size': page_size
        }
        return self._request(data={**kwargs, **data})

    @action('/api/open/product/detail')
    def get_product_detail(self, product_id: int, **kwargs) -> ApiResponse:
        """ 查询商品详情
        :param product_id: 管家商品ID
        示例：
        {
            "product_id": 1234567890
        }
        """
        data = {
            'product_id': product_id
        }
        return self._request(data={**kwargs, **data})

    @action('/api/open/product/sku/list')
    def get_product_sku_list(self, product_id: [],  **kwargs) -> ApiResponse:
        """ 查询商品规格
        :param product_id: 管家商品ID 最多支持100个
        示例：
        {
            "product_id": [1234567890, 1234567891]
        }
        """
        data = {
            'product_id': product_id
        }
        return self._request(data={**kwargs, **data})

    @action('/api/open/product/create')
    def create_product(self, product_data: dict, **kwargs) -> ApiResponse:
        """ 创建商品（单个）
        :param product_data: 商品数据
        示例：
        {
            "item_biz_type": 2,
            "sp_biz_type": 1,
            "channel_cat_id": "e11455b218c06e7ae10cfa39bf43dc0f",
            "channel_pv": [
                {
                    "property_id": "b5e5462c028aba7f1921b9e373cead75",
                    "property_name": "交易形式",
                    "value_id": "8a3445658e0bc44687b43d68bdc44732",
                    "value_name": "代下单"
                },
                {
                    "property_id": "96ad8793a2fdb81bb108d382c4e6ea42",
                    "property_name": "面值",
                    "value_id": "38ed5f6522cd7ab6",
                    "value_name": "100元"
                }
            ],
            "price": 550000,
            "original_price": 700000,
            "express_fee": 10,
            "stock": 10,
            "outer_id": "2021110112345",
            "stuff_status": 100,
            "publish_shop": [
                {
                    "images": [
                        "https://xxx.com/xxx1.jpg",
                        "https://xxx.com/xxx2.jpg"
                    ],
                    "user_name": "闲鱼会员名",
                    "province": 130000,
                    "city": 130100,
                    "district": 130101,
                    "title": "商品标题",
                    "content": "商品描述。",
                    "service_support": "SDR"
                }
            ],
            "sku_items": [
                {
                    "price": 500000,
                    "stock": 10,
                    "outer_id": "",
                    "sku_text": "颜色:白色;容量:128G"
                },
                {
                    "price": 600000,
                    "stock": 10,
                    "outer_id": "",
                    "sku_text": "颜色:白色;容量:256G"
                },
                {
                    "price": 500000,
                    "stock": 10,
                    "outer_id": "",
                    "sku_text": "颜色:黑色;容量:128G"
                },
                {
                    "price": 600000,
                    "stock": 10,
                    "outer_id": "",
                    "sku_text": "颜色:黑色;容量:256G"
                }
            ],
            "book_data": {
                "title": "北京法源寺",
                "author": "李敖",
                "publisher": "中国友谊出版公司",
                "isbn": "9787505720176"
            },
            "food_data": {
                "pack": "罐装",
                "spec": "150",
                "brand": "伏特加伏特加",
                "expire": {
                    "num": 360,
                    "unit": "天"
                },
                "production": {
                    "date": "2021-11-29",
                    "address": {
                        "detail": "北京市东城区x街道",
                        "province": 130000,
                        "city": 130100,
                        "district": 130101
                    }
                }
            },
            "report_data": {
                "used_car": {
                    "report_url": "https://xxxxxx.com"
                },
                "beauty_makeup": {
                    "org_id": 181,
                    "brand": "欧莱雅",
                    "spec": "小瓶装",
                    "level": "全新",
                    "org_name": "哈哈哈",
                    "images": [
                        "https://xxx.com/xxx1.jpg",
                        "https://xxx.com/xxx2.jpg"
                    ]
                },
                "game": {
                    "qc_no": "123123",
                    "qc_desc": "符合",
                    "title": "测试游戏",
                    "platform": "小霸王",
                    "images": [
                        "https://xxx.com/xxx1.jpg",
                        "https://xxx.com/xxx2.jpg"
                    ]
                },
                "curio": {
                    "org_id": 191,
                    "org_name": "NGC评级",
                    "size": "12mmx14mm",
                    "material": "陶瓷",
                    "qc_no": "3131319",
                    "images": [
                        "https://xxx.com/xxx1.jpg",
                        "https://xxx.com/xxx2.jpg"
                    ]
                },
                "jewelry": {
                    "org_name": "某某平台",
                    "shape": "圆形",
                    "color": "白色",
                    "weight": "125g",
                    "qc_no": "3131319",
                    "qc_desc": "无瑕疵",
                    "images": [
                        "https://xxx.com/xxx1.jpg",
                        "https://xxx.com/xxx2.jpg"
                    ]
                },
                "valuable": {
                    "org_id": 162,
                    "org_name": "国检",
                    "qc_no": "454545",
                    "qc_desc": "经检测符合制造商公示的制作工艺",
                    "images": [
                        "https://xxx.com/xxx1.jpg",
                        "https://xxx.com/xxx2.jpg"
                    ]
                },
                "yx_3c": {
                    "class_id": 10,
                    "subclass_id": 1001,
                    "brand_id": 10000,
                    "brand_name": "苹果",
                    "model_id": 10011,
                    "model_name": "iPhone 14 Pro",
                    "model_sn": "IMEI/序列号",
                    "report_user": "张胜男",
                    "report_time": "2024-03-15 18:04:44",
                    "report_items": [
                        {
                            "answer_id": 11103,
                            "answer_name": "不开机",
                            "answer_type": 2,
                            "category_name": "拆修侵液",
                            "group_name": "系统情况",
                            "question_name": "系统情况"
                        }
                    ],
                    "answer_ids": [
                        11103,
                        11106
                    ]
                }
            }
        }
        """
        data = product_data
        return self._request(data={**kwargs, **data})

    @action('/api/open/product/batchCreate')
    def product_batch_create(self, product_data: [], **kwargs):
        """ 批量创建商品
        1：字段参数要求与单个创建商品一致
        2：每批次最多创建50个商品
        3：同批次时item_key字段值要唯一
        :param product_data: 商品数据列表
        """
        data = product_data
        return self._request(data={**kwargs, **data})

    @action('/api/open/product/publish')
    def product_publish(self, product_id: int, user_name: [], specify_publish_time: str, notify_url: str, **kwargs):
        """ 上架商品 特别提醒：本接口会采用异步的方式更新商品信息到闲鱼App上，因此更新结果采用回调的方式进行通知。
        :param product_id: 商品数据列表
        :param user_name: 闲鱼会员名列表，
        :param specify_publish_time: 指定上架时间，格式为yyyy-MM-dd HH:mm:ss，如果不传则默认立即上架
        :param notify_url: 商品上架结果回调地址
        示例：
        {
            "product_id": 220656347074629,
            "user_name": [
                "tb924343042"
            ]
        }
        """
        data = {
            'product_id': product_id,
            'user_name': user_name,
            'specify_publish_time': specify_publish_time,
            'notify_url': notify_url
        }
        return self._request(data={**kwargs, **data})

    @action('/api/open/product/downShelf')
    def product_down_shelf(self, product_id: int, **kwargs):
        """ 下架商品
        :param product_id: 商品数据列表
        示例：
        {
            "product_id": 220656347074629,
        }
        """
        data = {
            'product_id': product_id,
        }
        return self._request(data={**kwargs, **data})

    @action('/api/open/product/edit')
    def product_edit(self, product_data: dict, **kwargs) -> ApiResponse:
        """ 编辑商品
        :param product_data: 商品数据
        示例：
       {
            "product_id": 443299347640581,
            "item_biz_type": 2,
            "sp_biz_type": 1,
            "category_id": 50025386,
            "channel_cat_id": "e11455b218c06e7ae10cfa39bf43dc0f",
            "channel_pv": [
                {
                    "property_id": "b5e5462c028aba7f1921b9e373cead75",
                    "property_name": "交易形式",
                    "value_id": "8a3445658e0bc44687b43d68bdc44732",
                    "value_name": "代下单"
                },
                {
                    "property_id": "96ad8793a2fdb81bb108d382c4e6ea42",
                    "property_name": "面值",
                    "value_id": "38ed5f6522cd7ab6",
                    "value_name": "100元"
                }
            ],
            "title": "iPhone 12 128G 黑色",
            "price": 550000,
            "original_price": 700000,
            "express_fee": 10,
            "stock": 10,
            "outer_id": "2021110112345",
            "stuff_status": 100,
            "publish_shop": [
                {
                    "images": [
                        "https://xxx.com/xxx1.jpg",
                        "https://xxx.com/xxx2.jpg"
                    ],
                    "user_name": "闲鱼会员名",
                    "province": 130000,
                    "city": 130100,
                    "district": 130101,
                    "title": "商品标题",
                    "content": "商品描述。",
                    "white_images": "https://xxx.com/xxx1.jpg",
                    "service_support": "SDR"
                }
            ],
            "sku_items": [
                {
                    "price": 500000,
                    "stock": 10,
                    "outer_id": "",
                    "sku_text": "颜色:白色;容量:128G"
                },
                {
                    "price": 600000,
                    "stock": 10,
                    "outer_id": "",
                    "sku_text": "颜色:白色;容量:256G"
                },
                {
                    "price": 500000,
                    "stock": 10,
                    "outer_id": "",
                    "sku_text": "颜色:黑色;容量:128G"
                },
                {
                    "price": 600000,
                    "stock": 10,
                    "outer_id": "",
                    "sku_text": "颜色:黑色;容量:256G"
                }
            ],
            "book_data": {
                "title": "北京法源寺",
                "author": "李敖",
                "publisher": "中国友谊出版公司",
                "isbn": "9787505720176"
            },
            "food_data": {
                "pack": "罐装",
                "spec": "150",
                "brand": "伏特加伏特加",
                "expire": {
                    "num": 360,
                    "unit": "天"
                },
                "production": {
                    "date": "2021-11-29",
                    "address": {
                        "detail": "北京市东城区x街道",
                        "province": 130000,
                        "city": 130100,
                        "district": 130101
                    }
                }
            },
            "report_data": {
                "used_car": {
                    "report_url": "https://xxxxxx.com"
                },
                "beauty_makeup": {
                    "org_id": 181,
                    "brand": "欧莱雅",
                    "spec": "小瓶装",
                    "level": "全新",
                    "org_name": "哈哈哈",
                    "qc_result": "通过",
                    "images": [
                        "https://xxx.com/xxx1.jpg",
                        "https://xxx.com/xxx2.jpg"
                    ]
                },
                "game": {
                    "qc_no": "123123",
                    "qc_result": "符合",
                    "title": "测试游戏",
                    "platform": "小霸王",
                    "images": [
                        "https://xxx.com/xxx1.jpg",
                        "https://xxx.com/xxx2.jpg"
                    ]
                },
                "curio": {
                    "org_id": 191,
                    "org_name": "NGC评级",
                    "size": "12mmx14mm",
                    "material": "陶瓷",
                    "qc_no": "3131319",
                    "qc_result": "真品",
                    "images": [
                        "https://xxx.com/xxx1.jpg",
                        "https://xxx.com/xxx2.jpg"
                    ]
                },
                "jewelry": {
                    "org_name": "某某平台",
                    "shape": "圆形",
                    "color": "白色",
                    "weight": "125g",
                    "qc_no": "3131319",
                    "qc_desc": "无瑕疵",
                    "images": [
                        "https://xxx.com/xxx1.jpg",
                        "https://xxx.com/xxx2.jpg"
                    ]
                },
                "valuable": {
                    "org_id": 162,
                    "org_name": "国检",
                    "qc_no": "454545",
                    "qc_result": "符合",
                    "images": [
                        "https://xxx.com/xxx1.jpg",
                        "https://xxx.com/xxx2.jpg"
                    ]
                },
                "yx_3c": {
                    "class_id": 10,
                    "subclass_id": 1001,
                    "brand_id": 10000,
                    "brand_name": "苹果",
                    "model_id": 10011,
                    "model_name": "iPhone 14 Pro",
                    "model_sn": "IMEI/序列号",
                    "report_user": "张胜男",
                    "report_time": "2024-03-15 18:04:44",
                    "report_items": [
                        {
                            "answer_id": 11103,
                            "answer_name": "不开机",
                            "answer_type": 2,
                            "category_name": "拆修侵液",
                            "group_name": "系统情况",
                            "question_name": "系统情况"
                        }
                    ],
                    "answer_ids": [
                        11103,
                        11106
                    ]
                }
            }
        }
        """
        data = {
            **product_data
        }
        return self._request(data={**kwargs, **data})

    @action('/api/open/product/edit/stock')
    def product_edit_stock(self, product_id: int, price: int, original_price: int,
                           stock: int, sku_items: [], **kwargs) -> ApiResponse:
        """ 编辑商品库存
        :param product_id: 商品ID
        :param price: 商品价格（分）
        :param original_price: 商品原价（分）
        :param stock: 单规格库存
        :param sku_items: 多规格库存
        示例：
        {
            "product_id": 219530767978565,
            "stock": 99999,
            "sku_items": [
                {
                    "stock": 6699,
                    "price":99999,
                    "sku_id": 219530767978561
                },
                {
                    "stock": 3982,
                    "price":99999,
                    "sku_id": 219530767978562
                }
            ]
        }
        """
        data = {
            'product_id': product_id,
            'sku_items': sku_items,
            'price': price,
            'original_price': original_price,
            'stock': stock
        }
        return self._request(data={**kwargs, **data})

    @action('/api/open/product/delete')
    def product_delete(self, product_id: int, **kwargs) -> ApiResponse:
        """ 删除商品
        :param product_id: 商品ID
        示例：
        {
            "product_id": 219530767978565
        }
        """
        data = {
            'product_id': product_id
        }
        return self._request(data={**kwargs, **data})