from flask.blueprints import Blueprint
from server.services import SampleService

sample_api = Blueprint('sample_api', __name__)


@sample_api.route('', methods=['GET'])
@sample_api.route('/', methods=['GET'])
def hello():
    sample_service = SampleService.SampleService()
    msg = sample_service.hello()
    output = sample_service.build_output(msg)
    return output
