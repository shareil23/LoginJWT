from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
import math

from ..Config import db
from ..Models import UserLog
from ..Schema import UserLogSchemaList


class UserHistoryAPI(Resource):
    @jwt_required()
    def get(self, page=1, totalData=10):
        # get user_xid data from refresh token
        get_user = get_jwt_identity()

        # data for user log
        user_log_data = {
            "user_xid": get_user,
            "action": "CHECK HISTORY"
        }

        # insert user log data to database
        user_log_insert_data = UserLog(**user_log_data)
        db.session.add(user_log_insert_data)
        db.session.commit()
        db.session.flush()
        
        # query user log
        query = UserLog.query \
            .filter(UserLog.user_xid == get_user) \
            .order_by(UserLog.utime.desc()) \
            .paginate(page, totalData, False)
        
        # get user log data
        user_log_schema = UserLogSchemaList(many=True)
        output          = user_log_schema.dump(query.items)
        
        # check the data is exists
        if len(output) == 0:
            result = {
                "status": 400,
                "data": None,
                "message": "No history data yet.",
                "totalPage": math.ceil(UserLog.query.filter(UserLog.user_xid == get_user).count() / totalData),
                "totalData": UserLog.query.filter(UserLog.user_xid == get_user).count()
            }
            return result, 400

        result = {
            "status": 200,
            "data": output,
            "message" : "Success",
            "totalPage": math.ceil(UserLog.query.filter(UserLog.user_xid == get_user).count() / totalData),
            "totalData": UserLog.query.filter(UserLog.user_xid == get_user).count()
        }
        
        return result, 200