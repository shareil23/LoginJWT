from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token

from ..Config import db, bcrypt
from ..Models import User, UserLog
from ..Schema import UserSchemaList


class UserAuthAPI(Resource):
    def post(self):
        """
        :target : API
        :return : information user successfully logged in
        """
        
        # get data from formdata and transform it to dict
        body = request.form.to_dict()
        
        validate_string = [
            "email",
            "password"
        ]
        
        if all(key in body for key in validate_string):
            # query are user exists
            query = User.query.filter(User.email == body['email'])
            
            # check is user exists
            if query.count() == 0:
                datas = {
                    "status": "error",
                    "data": None,
                    "message": "Please check username or password is wrong."
                }

                return datas, 400
            
            # get user data
            user_schema_list = UserSchemaList(many=True)
            output_user_data = user_schema_list.dump(query.all())
            
            # check the password is equal to hash
            if bcrypt.check_password_hash(output_user_data[0]['hash_val'], output_user_data[0]['user_xid'] + body['password']):
                datas = {
                    "status": "error",
                    "data": None,
                    "message": "Please check username or password is wrong."
                }

                return datas, 400
            
            # data for user log
            user_log_data = {
                "user_xid": output_user_data[0]['user_xid'],
                "action": "LOGIN"
            }
            
            # insert user log data to database
            user_log_insert_data = UserLog(**user_log_data)
            db.session.add(user_log_insert_data)
            db.session.flush()
            
            datas = {
                "status": "success",
                "data": {
                    "token": create_access_token(identity=output_user_data[0]['user_xid'], fresh=True),
                    "refesh_token": create_refresh_token(identity=output_user_data[0]['user_xid'])
                },
                "message": "Success Logged in"
            }

            return datas, 200
        else:
            datas = {
                "status": "error",
                "data": None,
                "message": "Missing required field in body request."
            }

            return datas, 400