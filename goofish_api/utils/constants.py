from enum import Enum


class RequestMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"

class ItemBizType(Enum):
    COMMON = 2             # 普通商品
    INSPECTED = 0          # 已验货
    INSPECTION_BAO = 10    # 验货宝
    BRAND_AUTH = 16        # 品牌授权
    XIAN_YU_SELECTED = 19  # 闲鱼严选
    XIAN_YU_FLASH = 24     # 闲鱼特卖
    BRAND_PICK = 26        # 品牌捡漏

class SpBizType(Enum):
    MOBILE = 1             # 手机
    TREND = 2              # 潮品
    HOME_APPLIANCE = 3     # 家电
    INSTRUMENT = 8         # 乐器
    DIGITAL = 9            # 3C数码
    LUXURY = 16            # 奢品
    MATERNAL = 17          # 母婴
    BEAUTY = 18            # 美妆个护
    JEWELRY = 19           # 文玩/珠宝
    GAMING = 20            # 游戏电玩
    HOME = 21              # 家居
    VIRTUAL_GAME = 22      # 虚拟游戏
    ACCOUNT_RENTAL = 23    # 租号
    BOOK = 24              # 图书
    VOUCHER = 25           # 卡券
    FOOD = 27              # 食品
    TRENDY_TOY = 28        # 潮玩
    SECOND_HAND_CAR = 29   # 二手车
    PET_PLANT = 30         # 宠植
    GIFT = 31              # 工艺礼品
    CAR_SERVICE = 33       # 汽车服务
    OTHER = 99             # 其他

class FlashSaleType(Enum):
    LI_QI = 1         # 临期
    GU_PIN = 2        # 孤品
    DUAN_MA = 3       # 断码
    WEI_XIA = 4       # 微瑕
    WEI_HUO = 5       # 尾货
    GUAN_FAN = 6      # 官翻
    QUAN_XIN = 7      # 全新
    FU_DAI = 8        # 福袋
    OTHER = 99        # 其他
    BRAND_WEI_XIA = 2601  # 微瑕
    BRAND_LI_QI = 2602  # 临期
    BRAND_QING_CANG = 2603  # 清仓
    BRAND_GUAN_FAN = 2604  # 官翻

class ProductStatus(Enum):
    """管家商品状态枚举"""
    UNKNOWN = 0  # 默认值
    STATUS_21 = 21  # 状态21
    STATUS_22 = 22  # 状态22
    STATUS_23 = 23  # 状态23
    STATUS_31 = 31  # 状态31
    STATUS_33 = 33  # 状态33
    STATUS_36 = 36  # 状态36
    STATUS_NEGATIVE_1 = -1  # 状态-1

class SaleStatus(Enum):
    """销售状态枚举"""
    UNKNOWN = 0  # 默认值
    PENDING_PUBLICATION = 1  # 待发布
    ON_SALE = 2  # 销售中
    OFF_SALE = 3  # 已下架


class OrderStatus(Enum):
    """订单状态枚举"""
    PENDING_PAYMENT = 11  # 待付款
    PENDING_SHIPMENT = 12  # 待发货
    SHIPPED = 21  # 已发货
    TRANSACTION_SUCCESS = 22  # 交易成功
    REFUNDED = 23  # 已退款
    TRANSACTION_CLOSED = 24  # 交易关闭

class RefundStatus(Enum):
    """退款状态枚举"""
    NOT_APPLIED = 0  # 未申请退款
    PENDING_SELLER_APPROVAL = 1  # 待商家处理
    PENDING_BUYER_RETURN = 2  # 待买家退货
    PENDING_SELLER_RECEIVE = 3  # 待商家收货
    REFUND_CLOSED = 4  # 退款关闭
    REFUND_SUCCESS = 5  # 退款成功
    REFUND_REJECTED = 6  # 已拒绝退款
    PENDING_RETURN_ADDRESS_CONFIRMATION = 8  # 待确认退货地址
