from server.middlewares import HandleSuccess
from flask import jsonify

def hello():
    return "hello"

def build_ouput(msg, format_return):
    handle_success = HandleSuccess.HandleSuccess()
    output = handle_success._build_output(format_return, msg)
    return jsonify(output)
