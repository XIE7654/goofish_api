from goofish_api.api.base import BaseAPI
from goofish_api.utils.api_response import ApiResponse
from goofish_api.utils.constants import RefundStatus, OrderStatus
from goofish_api.utils.helpers import action


class Order(BaseAPI):

    @action('/api/open/order/list')
    def get_order_list(self, order_status: OrderStatus, refund_status: RefundStatus, order_time: [], pay_time: [],
                       consign_time: [], confirm_time: [], refund_time: [], update_time: [], page_no: int,
                       page_size: int, **kwargs) -> ApiResponse:
        """ 获取订单列表
        :param order_status: 订单状态
        :param refund_status: 退款状态
        :param order_time: 订单时间范围
        :param pay_time: 支付时间范围
        :param consign_time: 发货时间范围
        :param confirm_time: 确认收货时间范围
        :param refund_time: 退款时间范围
        :param update_time: 更新时间范围
        :param page_no: 页码
        :param page_size: 每页大小
        """
        data = {
            "order_status": order_status,
            "refund_status": refund_status,
            "order_time": order_time,
            "pay_time": pay_time,
            "consign_time": consign_time,
            "confirm_time": confirm_time,
            "refund_time": refund_time,
            "update_time": update_time,
            "page_no": page_no,
            "page_size": page_size
        }
        return self._request(data={**kwargs, **data})

    @action('/api/open/order/detail')
    def get_order_detail(self, order_no: str, **kwargs) -> ApiResponse:
        """ 获取订单详情
        :param order_no: 订单号
        """
        data = {
            "order_no": order_no
        }
        return self._request(data={**kwargs, **data})

    @action('/api/open/order/kam/list')
    def kam_order_list(self, order_no: str, **kwargs) -> ApiResponse:
        """ 订单卡密列表
        :param order_no: 闲鱼订单号
        """
        data = {
            "order_no": order_no,
        }
        return self._request(data={**kwargs, **data})

    @action('/api/open/order/ship')
    def order_ship(self, order_no: str, ship_name, ship_mobile, ship_district_id, ship_prov_name,
                   ship_city_name, ship_area_name, waybill_no, express_name, express_code, **kwargs) -> ApiResponse:
        """ 订单物流发货
        :param order_no: 订单号
        :param ship_name: 收货人姓名
        :param ship_mobile: 收货人手机号
        :param ship_district_id: 收货人所在地区ID
        :param ship_prov_name: 收货人所在省份名称
        :param ship_city_name: 收货人所在城市名称
        :param ship_area_name: 收货人所在区县名称
        :param waybill_no: 运单号
        :param express_name: 快递公司名称
        :param express_code: 快递公司编码
        示例：
        {
            "order_no": "1339920336328048683",
            "ship_name": "张三",
            "ship_mobile": "13800138000",
            "ship_district_id": 440305,
            "ship_prov_name": "广东省",
            "ship_city_name": "深圳市",
            "ship_area_name": "南山区",
            "ship_address": "侨香路西丽街道丰泽园仓储中心",
            "waybill_no": "25051016899982",
            "express_name": "其他",
            "express_code": "qita"
        }
        """
        data = {
            "order_no": order_no,
            "ship_name": ship_name,
            "ship_mobile": ship_mobile,
            "ship_district_id": ship_district_id,
            "ship_prov_name": ship_prov_name,
            "ship_city_name": ship_city_name,
            "ship_area_name": ship_area_name,
            "waybill_no": waybill_no,
            "express_name": express_name,
            "express_code": express_code
        }
        return self._request(data={**kwargs, **data})