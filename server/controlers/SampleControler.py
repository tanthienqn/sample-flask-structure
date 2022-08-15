from flask.blueprints import Blueprint
from server.services import SampleService
from server.constants.FormatReturn import TypeReturn

sample_api = Blueprint('sample_api', __name__)


@sample_api.route('', methods=['GET'])
@sample_api.route('/', methods=['GET'])
def hello():
    msg = SampleService.hello()
    output = SampleService.build_output(msg, TypeReturn.MSG)
    return output
