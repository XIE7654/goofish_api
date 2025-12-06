# 本仓库的所有内容仅供学习和参考之用，禁止用于商业用途。任何人或组织不得将本仓库的内容用于非法用途或侵犯他人合法权益。
# 本仓库所涉及的爬虫技术仅用于学习和研究，不得用于对其他平台进行大规模爬虫或其他非法行为
# 对于因使用本仓库内容而引起的任何法律责任，本仓库不承担任何责任。使用本仓库的内容即表示您同意本免责声明的所有条款和条件。

import requests
import csv
import hashlib
import time
import json
from typing import Dict, Tuple, Optional
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('xianyu_crawler.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)
# 从浏览器中复制的Cookie字符串
# 配置常量
COOKIE_STR = ''


API_URL = 'https://h5api.m.goofish.com/h5/mtop.taobao.idlemtopsearch.pc.search/1.0/'
APP_KEY = '34839810'
KEYWORD = 'bebebus安全座椅'
MAX_PAGE = 1  # 爬取的最大页数
CSV_FIELDS = ['用户名', '地区', '售价', '标题', '详情页']
DETAIL_URL_TEMPLATE = 'https://www.goofish.com/item?id={}'


class XianYuCrawler:
    """闲鱼爬虫类"""

    def __init__(self):
        self.cookies = self.parse_cookies(COOKIE_STR)
        self.token = self.extract_token()
        self.session = self.create_session()

    def parse_cookies(self, cookie_str: str) -> Dict[str, str]:
        """解析Cookie字符串为字典"""
        cookies = {}
        for item in cookie_str.split('; '):
            if '=' not in item:
                continue
            try:
                key, value = item.split('=', 1)
                cookies[key] = value
            except Exception as e:
                logger.warning(f"解析Cookie项失败: {item}, 错误: {e}")
        return cookies

    def extract_token(self) -> Optional[str]:
        """提取_m_h5_tk中的token"""
        if '_m_h5_tk' in self.cookies:
            token = self.cookies['_m_h5_tk'].split('_')[0]
            logger.info(f"提取到Token: {token}")
            return token
        logger.error("未找到_m_h5_tk Cookie")
        return None

    def create_session(self) -> requests.Session:
        """创建带持久化Cookie的Session"""
        session = requests.Session()
        session.cookies.update(self.cookies)
        session.headers.update({
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
            'Cookie': COOKIE_STR,
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://2.taobao.com/',
            'Accept': 'application/json, text/plain, */*'
        })
        return session

    def generate_sign(self, page: int) -> Tuple[str, int, str]:
        """生成签名和请求参数"""
        if not self.token:
            raise ValueError("Token不存在，无法生成签名")

        # 获取时间戳
        timestamp = int(time.time() * 1000)

        # 构建请求数据
        data_dict = {
            "pageNumber": page,
            "keyword": KEYWORD,
            "fromFilter": False,
            "rowsPerPage": 30,
            "sortValue": "",
            "sortField": "",
            "customDistance": "",
            "gps": "",
            "propValueStr": {"searchFilter": "publishDays:1;"},
            "customGps": "",
            "searchReqFromPage": "pcSearch",
            "extraFilterValue": "{}",
            "userPositionJson": "{}"
        }

        # 转换为JSON字符串
        data_json = json.dumps(data_dict, ensure_ascii=False, separators=(',', ':'))

        # 生成签名
        sign_str = f"{self.token}&{timestamp}&{APP_KEY}&{data_json}"
        sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest()

        return sign, timestamp, data_json

    def get_page_params(self, sign: str, timestamp: int) -> Dict[str, str]:
        """构建URL参数"""
        return {
            'jsv': '2.7.2',
            'appKey': APP_KEY,
            't': str(timestamp),
            'sign': sign,
            'v': '1.0',
            'type': 'originaljson',
            'accountSite': 'xianyu',
            'dataType': 'json',
            'timeout': '20000',
            'api': 'mtop.taobao.idlemtopsearch.pc.search',
            'sessionOption': 'AutoLoginOnly',
            'spm_cnt': 'a21ybx.search.0.0',
            'spm_pre': 'a21ybx.home.searchInput.0',
        }

    def fetch_page_data(self, page: int) -> Optional[Dict]:
        """获取单页数据"""
        try:
            logger.info(f"开始采集第{page}页数据")

            # 生成签名和参数
            sign, timestamp, data_json = self.generate_sign(page)
            params = self.get_page_params(sign, timestamp)
            data = {'data': data_json}

            # 发送请求
            response = self.session.post(
                API_URL,
                params=params,
                data=data,
                timeout=30
            )
            response.raise_for_status()  # 抛出HTTP错误

            # 解析响应
            json_data = response.json()

            # 保存响应数据用于调试
            with open(f'response_page_{page}.json', 'w', encoding='utf-8') as f:
                json.dump(json_data, f, ensure_ascii=False, indent=4)

            # 检查响应状态
            if json_data.get('ret') and 'SUCCESS' not in json_data['ret'][0]:
                logger.error(f"第{page}页请求失败: {json_data.get('ret')}")
                return None

            return json_data

        except requests.exceptions.RequestException as e:
            logger.error(f"第{page}页请求异常: {e}")
            return None
        except Exception as e:
            logger.error(f"第{page}页处理异常: {e}", exc_info=True)
            return None

    def parse_item_data(self, item: Dict) -> Optional[Dict]:
        """解析单个商品数据"""
        try:
            ex_content = item['data']['item']['main']['exContent']
            detail_params = ex_content.get('detailParams', {})

            # 构建商品信息字典
            item_data = {
                '用户名': ex_content.get('userNickName', '未知'),
                '地区': ex_content.get('area', '未知'),
                '售价': detail_params.get('soldPrice', '未知'),
                '标题': detail_params.get('title', '未知'),
                '详情页': DETAIL_URL_TEMPLATE.format(ex_content.get('itemId', ''))
            }

            return item_data

        except Exception as e:
            logger.warning(f"解析商品数据失败: {e}", exc_info=True)
            return None

    def save_to_csv(self, all_items: list):
        """保存数据到CSV文件"""
        try:
            with open('xianyu_data.csv', mode='w', encoding='utf-8', newline='') as f:
                csv_writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
                csv_writer.writeheader()
                csv_writer.writerows(all_items)
            logger.info(f"成功保存{len(all_items)}条数据到CSV文件")
        except Exception as e:
            logger.error(f"保存CSV文件失败: {e}")

    def run(self):
        """运行爬虫主程序"""
        all_items = []

        # 检查token是否有效
        if not self.token:
            logger.error("Token无效，爬虫终止")
            return

        # 遍历所有页面
        for page in range(1, MAX_PAGE + 1):
            # 获取页面数据
            page_data = self.fetch_page_data(page)
            if not page_data or 'data' not in page_data or 'resultList' not in page_data['data']:
                logger.warning(f"第{page}页无有效数据")
                continue

            # 解析商品列表
            result_list = page_data['data']['resultList']
            for item in result_list:
                item_data = self.parse_item_data(item)
                if item_data:
                    all_items.append(item_data)
                    logger.debug(f"解析到商品: {item_data['标题']}")

        # 保存数据
        if all_items:
            self.save_to_csv(all_items)
        else:
            logger.warning("未采集到任何商品数据")


def main():
    """主函数"""
    try:
        # 创建爬虫实例并运行
        crawler = XianYuCrawler()
        crawler.run()
        logger.info("爬虫执行完成")
    except Exception as e:
        logger.error("爬虫主程序异常", exc_info=True)


if __name__ == "__main__":
    main()