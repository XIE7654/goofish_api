import pprint


class ApiResponse:

    def __init__(self,  **kwargs):
        self.headers = kwargs

    def __str__(self):
        return pprint.pformat(self.__dict__)
