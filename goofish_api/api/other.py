from goofish_api.api.base import BaseAPI
from goofish_api.utils.api_response import ApiResponse
from goofish_api.utils.helpers import action


class Other(BaseAPI):

    @action("/api/open/express/companies")
    def get_express_companies(self, **kwargs) -> ApiResponse:
        """ 获取快递公司列表 """
        return self._request(data={**kwargs})