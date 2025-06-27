import hashlib
import http.client
import json
import time

# 应用配置示例，请替换应用配置
appKey = 1107484643411461
appSecret = "KPpWWqOQIj88n3vcQgivqB0i1lxfWX2e"
domain = "https://open.goofish.pro"


# 请求函数
def request(url: str, data: json):
    # 将json对象转成json字符串
    # 特别注意：使用 json.dumps 函数时必须补充第二个参数 separators=(',', ':') 用于过滤空格，否则会签名错误
    body = json.dumps(data, separators=(",", ":"))
    print(body)
    # 时间戳秒
    timestamp = int(time.time())

    # 生成签名
    sign = genSign(body, timestamp)

    # 拼接地址
    url = f"{domain}{url}?appid={appKey}&timestamp={timestamp}&sign={sign}"

    # 设置请求头
    headers = {"Content-Type": "application/json"}

    # 请求接口
    conn = http.client.HTTPSConnection("open.goofish.pro")
    conn.request(
        "POST",
        url,
        body,
        headers,
    )
    res = conn.getresponse()
    reps = res.read().decode("utf-8")

    return reps


# 签名函数
def genSign(bodyJson: str, timestamp: int):
    # 将请求报文进行md5
    m = hashlib.md5()
    m.update(bodyJson.encode("utf8"))
    bodyMd5 = m.hexdigest()

    # 拼接字符串生成签名-自研模式
    s = f"{appKey},{bodyMd5},{timestamp},{appSecret}"

    # 商务对接模式
    # s = f"{appKey},{bodyMd5},{timestamp},{sellerId},{appSecret}"

    m = hashlib.md5()
    m.update(s.encode("utf8"))
    sign = m.hexdigest()

    return sign


# 查询商品详情报文示例，请替换管家商品ID
resp = request("/api/open/user/authorize/list", {})
print(resp)