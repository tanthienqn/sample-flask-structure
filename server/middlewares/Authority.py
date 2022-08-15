from functools import wraps
from flask_jwt_extended.view_decorators import _decode_jwt_from_request
from flask import current_app as app
import os
import json
import requests


def update_publickey():
    url = os.getenv('AUTHEN_SERVICE', '0.0.0.0:5001')
    url = url + '/oauth/token_key'
    res_auth = requests.get(url)
    if res_auth.status_code != 200:
        raise Exception("PERMISSION_DENIED")
    pubkey = json.loads(res_auth.text)
    app.config["JWT_PUBLIC_KEY"] = pubkey["value"]


def decode_jwt():
    try:
        jwt_data = _decode_jwt_from_request(locations="headers", fresh=False)[0]
        return jwt_data
    except Exception as e:
        if str(e) == "Signature verification failed":
            update_publickey()
        else:
            raise Exception(str(e))
        jwt_data = _decode_jwt_from_request(locations="headers", fresh=False)[0]
    return jwt_data


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        jwt_data = decode_jwt()
        idUser = jwt_data.get("idUser", "")
        kwargs['idUser'] = idUser
        return fn(*args, **kwargs)

    return wrapper
