from app import db
import hashlib
import datetime as dt
from .users import Users

class Auth(db.Model):

    __tablename__="auth"

    id = db.Column(db.Integer(), unique=True, primary_key=True)
    token = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey(Users.id))
    created_on = db.Column(db.DateTime())
    updated_on = db.Column(db.DateTime())

    def __init__(self, username, user_id):
        logintime = str(dt.datetime.now())
        self.token = hashlib.sha384((str(username)+logintime).encode()).hexdigest()
        self.user_id = user_id
        self.created_on = dt.datetime.now()
        self.updated_on = dt.datetime.now()
    
    def __repr__(self):
        return '<Auth token: token = {}'.format(self.token)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.srialize()
    
    def srialize(self):
        return {
            'id':self.id,
            'token':self.token,
            'user_id':self.user_id,
        }
    
    @staticmethod
    def fromlogindata(obj):
        username = obj['username']
        password = obj['password']
        isExist, userId = Users.userIsExist(username,password)
        if(isExist):
            # user_id = 
            auth = Auth(username,userId['id'])
            auth.save()
            return auth.srialize()
        else :
            return None