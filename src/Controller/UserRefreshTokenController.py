from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_refresh_token_required

from ..Config import db
from ..Models import UserLog


class UserTokenRefreshAPI(Resource):
    @jwt_refresh_token_required
    def post(self):
        # get user_xid data from refresh token
        get_user = get_jwt_identity()
        
        # data for user log
        user_log_data = {
            "user_xid": get_user,
            "action": "REFRESH TOKEN"
        }
        
        # insert user log data to database
        user_log_insert_data = UserLog(**user_log_data)
        db.session.add(user_log_insert_data)
        db.session.flush()
        
        datas = {
            "status": "success",
            "data": {
                "token": create_access_token(identity=get_user)
            },
            "message": "Success Logged in"
        }

        return datas, 200