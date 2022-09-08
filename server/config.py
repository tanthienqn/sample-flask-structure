import os
from datetime import timedelta

RSA_PUBLIC = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAza7n18GVgt5akP9mw845Ng0lEril4tdUncigI5Oci9YO8JLHIVEty4UBycnhoLdPWnbSILeVJZfOSViBpdA6NvyOANTnkIovcKA93IYldkXSuayCXEuGSuX+4m/jB/SRi8rUs6LppaKjSYqAFYHo9Fr5mq8j1kylYgeIqAymBe3M8/HEeVxvboEH6vhLihfFN/R4F2/nuqBaswGeF5gkbhKmUCxcBMJRJ6OJnSin03T9ZZ8lReJkEaKfuDP53ktRiy+MPwfEDABsI+0mxIdTOnmqmvwR+9QcQKSZjEWWGMUyfEB60jzB7z4+drersWYbOav6jX4AfALV9A3M6lj+jwIDAQAB
-----END PUBLIC KEY-----
"""


class BaseConfig(object):
    """Base configuration."""
    SERVICE_NAME = os.getenv('SERVICE_NAME', 'sample-service')
    # Flask BCRYPT setting
    SECRET_KEY = os.getenv('BCRYPT_SECRET_KEY', '94722952-64cf-4729-a78a-3e6ffd5ae210')
    BCRYPT_LOG_ROUNDS = 13
    # Flask-JWT-EXTENDED
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', '48f48882-5d0b-4c33-80be-5e9f381fe268')
    # Enable blacklisting and specify what kind of tokens to check
    JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'RS256')
    JWT_DECODE_AUDIENCE = ["restservice"]
    JWT_IDENTITY_CLAIM = "client_id"
    JWT_PUBLIC_KEY = RSA_PUBLIC
    # against the blacklist
    JWT_BLACKLIST_ENABLED = False
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=1)
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', '/tmp')
    # config mongodb
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGO_DATABASE', 'vqc-dev'),
        'host': os.getenv('MONGO_URI', 'mongodb://admin:admin@127.0.0.1:2017/dev?replicaSet=rs')
    }
    # config minio
    MINIO_ENDPOINT = os.getenv('MINIO_ENDPOINT', '0.0.0.0:9007')
    MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY', 'TESTING')
    MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY', 'TESTING')
    MINIO_SECURE = True
    if os.getenv('MINIO_SECURE', 'False') == 'False':
        MINIO_SECURE = False
    MINIO_REGION = os.getenv('MINIO_REGION', None)
    MINIO_HTTP_CLIENT = os.getenv('MINIO_HTTP_CLIENT', None)
    MINIO_BUCKET = os.getenv('MINIO_BUCKET', 'develop')


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True,
    BCRYPT_LOG_ROUNDS = 4,


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    BCRYPT_LOG_ROUNDS = 4


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}
