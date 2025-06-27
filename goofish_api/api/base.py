from goofish_api.utils.api_response import ApiResponse


class BaseAPI(object):
    """ Goofish API base class """

    def __init__(self, client=None):
        self._client = client

    def _request(self, data: dict = None) -> ApiResponse:

        return self._client.request(data=data)
