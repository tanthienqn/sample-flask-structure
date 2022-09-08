from flask import jsonify
from server.constants import ErrorMessage
from flask import current_app as app


class HandleError:
    __errorMessage = ErrorMessage.errorMessage
    __errorMessageVN = ErrorMessage.errorMessageVN
    __errorStatus = ErrorMessage.errorStatus

    @classmethod
    def logger_error(cls, e):
        app.logger.error("ERROR: %s" % str(e), exc_info=True)

    @classmethod
    def handle(cls, error_return):
        cls.logger_error(error_return)
        code = str(error_return)
        message = cls.__errorMessage.get(code, None)
        error = cls.__errorMessageVN.get(str(error_return), code)
        status_code = cls.__errorStatus.get(str(error_return), 500)
        if message is None:
            code = "NOT_DEFINE"
            message = "SAMPLE-00000500"
            status_code = 500
        return jsonify(message=message, code=code, status="Error", statusCode=status_code, error=[error]), status_code

