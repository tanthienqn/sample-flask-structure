from flask import jsonify
from server.utils import ErrorMessage


def handle_exception(error_return):
    code = str(error_return)
    message = ErrorMessage.errorMessage.get(code, None)
    if message is None:
        code = "NOT_DEFINE"
        message = "ECT-00000400"
    error = ErrorMessage.errorMessageVN.get(str(error_return), error_return)
    status_code = ErrorMessage.errorStatus.get(str(error_return))
    return jsonify(message=message, code=code, status="Error", statusCode=status_code, error=[error]), status_code
