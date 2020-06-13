# from app.models import Users
# from app.models import BaseModel
from app.models import *
from flask import request, jsonify
from app import app
from .doresponse import *
# from app.users import Users

@app.route("/users", methods=['GET'])
def getUser():

    limit = request.args.get('limit') if request.args.get('limit')!=None else 20
    offset = request.args.get('offset') if request.args.get('offset')!=None else 0
    users, rowsize= Users.getAll(limit,offset)
    metadata = ListMeta(limit,offset,rowsize).serialize()
    return doSucces(
        data=users,
        status=HttpStatus.OK,
        meta=metadata
        )

@app.route("/users", methods=['POST'])
def createUser():
    body = request.json
    user = Users.fromJson(body)
    isExist, data = user.save()
    if(isExist):
        return doError(
            status=HttpStatus.BAD_REQUEST,
            message="username is exist"
        )
    else:
        return doSucces(
            data=data,
            status=HttpStatus.CREATED,
            meta=None
        )

@app.route('/users/<int:id>', methods=['GET','PUT', 'DELETE'])
def singleUser(id):
    if request.method == 'GET':
        return getSingleuser(id)
        # return 'Method for get user'
    elif request.method == 'PUT':
        # return
        return updateUser(id)
        # return 'Method for update user'
    elif request.method == 'DELETE':
        return deleteUser(id)
        # return 'Method for delete user'
    else:
        return doError(HttpStatus.NOT_FOUND,message="method not available")

def getSingleuser(id):
    user = Users.getSingle(id)
    if(user!=None):
        return doSucces(
            data=user,
            status=HttpStatus.OK,
            meta=None
        )
    else:
        return doError(
            status=HttpStatus.NOT_FOUND,
            message="user not found"
        )

def updateUser(id):
    user = Users.getSingle(id)
    if(user!=None):
        user = Users.deSerialize(user)
        newdata = Users.fromJson(request.json)
        user.update(newdata)
        return getSingleuser(id)   
        # return ""
    else:
        return doError(
            status=HttpStatus.NOT_FOUND,
            message="user not found"
            )

def deleteUser(id):
    user = Users.getSingle(id)
    if user != None:
        user = Users.deSerialize(user)
        user.delete()
        return doError(
            status=HttpStatus.OK,
            message="deleted"
        )
    else:
        return doError(
            status=HttpStatus.NOT_FOUND,
            message="user not found"
        )
