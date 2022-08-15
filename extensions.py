from flask_jwt_extended.jwt_manager import JWTManager
from flask_mongoengine import MongoEngine
from flask_minio import Minio
from healthcheck import HealthCheck

db = MongoEngine()
jwt = JWTManager()
storage = Minio()
health = HealthCheck()


# add your own check function to the healthcheck
def print_ok():
    return True, "OK"


health.add_check(print_ok)
