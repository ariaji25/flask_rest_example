from .module.models.users import Users
from .module.models.auth import Auth

class BaseModel:
    def __init__(self,data,message,status,meta):
        self.data =data
        self.message =message
        self.status=status
        self.meta=meta
    
    def serialize(self):
        return {
            'data':self.data,
            'message':self.message,
            'status':self.status,
            'meta':self.meta
        }

class ListMeta:
    def __init__(self,limit,offset,size):
        self.limit=limit
        self.offset=offset
        self.size=size
    
    def serialize(self):
        return {
            'limit':self.limit,
            'offset':self.offset,
            'size':self.size
        }