import hashlib
import http.client
import json
import time

import logging
import requests
from requests import request

from goofish_api.utils.api_response import ApiResponse

log = logging.getLogger(__name__)


# 应用配置示例，请替换应用配置


class BaseClient(object):
    method = 'GET'
    domain = "https://open.goofish.pro"  # 正式环境域名

    def __init__(self, app_key, app_secret, seller_id = None, debug = False):
        self.app_key = app_key
        self.app_secret = app_secret
        self.seller_id = seller_id
        print(app_key, app_secret)
        self.debug = debug
        self.headers = {
            "content-type": "application/json;charset=UTF-8",
        }

    def get_sign(self, body_json: str, timestamp: int):
        print(body_json, 'body_json')
        # 将请求报文进行md5
        m = hashlib.md5()
        m.update(body_json.encode("utf8"))
        body_md5 = m.hexdigest()
        if self.seller_id:
            # 商务对接模式
            s = f"{self.app_key},{body_md5},{timestamp},{self.seller_id},{self.app_secret}"
        else:
            # 拼接字符串生成签名-自研模式
            s = f"{self.app_key},{body_md5},{timestamp},{self.app_secret}"
        m = hashlib.md5()
        m.update(s.encode("utf8"))
        sign = m.hexdigest()
        return sign

    def get_url(self, path: str):
        """
        获取请求的完整URL
        :param path: 请求路径
        :return: 完整的URL
        """
        return f"{self.domain}{path}"

    def remove_null_values(self, data):
        """移除字典中值为 None 的键值对"""
        if isinstance(data, dict):
            return {k: self.remove_null_values(v) for k, v in data.items() if v is not None}
        elif isinstance(data, list):
            return [self.remove_null_values(item) for item in data]
        else:
            return data

    def request(self, data: json):
        # 将json对象转成json字符串
        # 特别注意：使用 json.dumps 函数时必须补充第二个参数 separators=(',', ':') 用于过滤空格，否则会签名错误
        # 时间戳秒
        timestamp = int(time.time())
        path = data.pop('path')
        method = data.pop('method')
        data = self.remove_null_values(data)  # 移除值为 None 的键值对
        body = json.dumps(data, separators=(",", ":"))
        # 生成签名
        sign = self.get_sign(body, timestamp)
        url = f"{self.domain}{path}?appid={self.app_key}&timestamp={timestamp}&sign={sign}"
        if self.seller_id:
            url = f"{url}&seller_id={self.seller_id}"
        conn = http.client.HTTPSConnection("open.goofish.pro")
        conn.request(
            "POST",
            url,
            body,
            self.headers,
        )
        res = conn.getresponse()
        reps = res.read().decode("utf-8")

        return reps

    def _check_response(self, res) -> ApiResponse:
        return res
