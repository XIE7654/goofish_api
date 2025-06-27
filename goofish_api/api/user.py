from goofish_api.api.base import BaseAPI
from goofish_api.utils.api_response import ApiResponse
from goofish_api.utils.helpers import action


class User(BaseAPI):

    @action("/api/open/user/authorize/list")
    def get_authorize_list(self, **kwargs) -> ApiResponse:
        """ 查询闲鱼店铺 """
        return self._request(data={**kwargs})