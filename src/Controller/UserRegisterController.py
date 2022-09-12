from flask_restful import Resource
from flask import request
import uuid

from ..Config import db, bcrypt
from ..Models import User


class UserRegisterAPI(Resource):
    def post(self):
        """
        :target : API
        :return : information user successfully registered
        """
        
        # get data from formdata and transform it to dict
        body = request.form.to_dict()
        
        validate_string = [
            "email",
            "password",
            "retry_password"
        ]
        
        if all(key in body for key in validate_string):
            # check the password equal
            if body['password'] != body['retry_password']:
                datas = {
                    "status": "error",
                    "data": None,
                    "message": "Password not match, please try again."
                }

                return datas, 400
            
            # init utime
            body['utime'] = 0
            
            # query are user exists
            query = User.query.filter(User.email == body['email']).count()
            
            # check are user exists
            if query != 0:
                datas = {
                    "status": "error",
                    "data": None,
                    "message": "Try again later."
                }

                return datas, 400 
            
            # init user_xid
            body['user_xid'] = str(uuid.uuid4())
            
            # init hash_val
            body['hash_val'] = bcrypt.generate_password_hash(body['user_xid'] + body['password'])
            
            # insert user data to database
            user_insert_data = User(**body)
            db.session.add(user_insert_data)
            db.session.flush()
            
            datas = {
                "status": "success",
                "data": None,
                "message": "Account registered, please continue login"
            }

            return datas, 200
        else:
            datas = {
                "status": "error",
                "data": None,
                "message": "Missing required field in body request."
            }

            return datas, 400