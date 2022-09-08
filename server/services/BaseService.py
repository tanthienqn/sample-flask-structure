import os
import requests
from flask import jsonify
from server.middlewares import HandleSuccess
from server.constants.FormatReturn import TypeReturn


class BaseService:

    @classmethod
    def handle(cls):
        pass

    @classmethod
    def build_output(cls, msg, format_return=TypeReturn.MSG):
        handle_success = HandleSuccess.HandleSuccess()
        output = handle_success.build_output(format_return, msg)
        return jsonify(output)

    @classmethod
    def build_output_pagination(cls, msg, format_return=TypeReturn.PAGINATION, page=1, max_size=1000, sort=1,
                                properties_sort="_id"):
        handle_success = HandleSuccess.HandleSuccess()
        handle_success.pagination(page, max_size, sort, properties_sort)
        output = handle_success.build_output(format_return, msg)
        return jsonify(output)

    @classmethod
    def post_requests(cls, url, data_json, headers=None):
        response = requests.post(
            url,
            headers=headers,
            json=data_json
        )
        if response.status_code != 200:
            raise Exception(response.text)
        body_data = response.json().get("data", {})
        return body_data
