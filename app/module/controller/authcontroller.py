from app.models import Auth
from flask import jsonify, request
from app import app
from .doresponse import *

@app.route("/auth", methods=['POST'])
def login():
    logindata = request.json
    response = Auth.fromlogindata(logindata)
    if response != None:
        return doSucces(
            data=response,
            status=HttpStatus.CREATED,
            meta=None
        )
    else:
        return doError(
            message="cant create auth token",
            status=HttpStatus.BAD_REQUEST
        )