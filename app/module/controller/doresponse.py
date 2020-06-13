from app.models import BaseModel
from flask import jsonify

class HttpStatus:
    OK = 200
    CREATED = 201
    NOT_FOUND = 404
    BAD_REQUEST = 400 

def doSucces(data, status, meta):
    res_status = status
    res_message = "succes"
    if(status==HttpStatus.CREATED):
        res_message = "created"
    
    res_data = BaseModel(
        data=data,
        message=res_message,
        status=res_status,
        meta=meta
    ).serialize()

    return jsonify(res_data)

def doError(status,message):
    res_data = BaseModel(
        data=None,
        message=message,
        status=status,
        meta=None
    ).serialize()

    return res_data
