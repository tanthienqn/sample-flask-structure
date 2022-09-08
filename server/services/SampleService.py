from server.services.BaseService import BaseService


class SampleService(BaseService):

    @classmethod
    def hello(cls):
        return "hello"
