from app import db, jsonify
import hashlib 
import datetime as dt

class Users(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer(), unique=True, primary_key=True, nullable=False)
    username = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    role = db.Column(db.String())
    created_on = db.Column(db.DateTime())

    def __init__(self,username,password,role):
        self.username = username
        self.password = hashlib.md5(str(password).encode()).hexdigest()
        self.role = role
        self.created_on = dt.datetime.now()

    def isExist(self):
        try:
            # print(self.username)
            user = Users.query.filter(Users.username == self.username).all()
            return user!=[]
        except Exception as e:
            # print(str(e))
            return False
    
    def __repr__(self):
        return "<User Id, id={}".format(self.id)

    def save(self):
        isExist = self.isExist()
        if(isExist):
            return isExist, None
        else:    
            db.session.add(self)
            db.session.commit()
            return isExist, self.serialize()
    
    def serialize(self):
        return {
            'id':self.id,
            'username':self.username,
            'password':self.password,
            'role':self.role
        }
    
    
    @staticmethod
    def getAll(limit=20,offset=0):
        try:
            users = Users.query.limit(limit).offset(offset).all()
            totaldata = Users.query.all()
            totaldata = [t.serialize() for t in totaldata]
            totaldata = totaldata.__len__()
            result = [u.serialize() for u in users]
            # print(result.__len__())
            return result, totaldata
        except Exception as e:
            return str(e)

    @staticmethod
    def getSingle(id):
        try:
            user = Users.query.filter(Users.id==id).all()
            result = [u.serialize() for u in user]
            if result.__len__()>0:
                return result[0]
            else:
                return None
        except Exception as e:
            return str(e)

    @staticmethod
    def getSingleByUsername(username):
        try:
            user = Users.query.filter(Users.username == username).all()
            result = [u.serialize() for u in user]
            return user
        except Exception as e:
            return str(e)
    
    @staticmethod
    def fromJson(obj):
        return Users(obj['username'], obj['password'], obj['role'])
    
    @staticmethod
    def userIsExist(username,password):
        pwd = hashlib.md5(str(password).encode()).hexdigest()
        user = Users.query.filter(Users.username==username, Users.password==pwd).all()
        result = [u.serialize() for u in user]
        return (result.__len__() > 0),result[0]
    
    @staticmethod
    def deSerialize(obj):
        user = Users.fromJson(obj)
        user.id = obj['id']
        return user

    def delete(self):
        user = Users.query.filter(Users.id==self.id).first()
        db.session.delete(user)
        db.session.commit()
    
    def update(self, newdata):
        user = Users.query.filter(Users.id==self.id).first()
        user.username = newdata.username
        user.role = newdata.role
        user.password = hashlib.md5(str(newdata.password).encode()).hexdigest()
        db.session.commit()
        