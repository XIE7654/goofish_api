from goofish_api import api
from goofish_api.utils.base_client import BaseClient


class GoofishClient(BaseClient):

    def __init__(self,  app_key, access_token, debug=False):
        super().__init__(app_key, access_token, debug)
        self.user = api.User(self)
        self.good = api.Good(self)