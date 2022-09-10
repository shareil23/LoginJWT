from flask_restful import Resource
from flask_jwt_extended import get_raw_jwt, jwt_required, get_jwt_identity

from ..Config import db, jwt
from ..Models import UserLog, RevokedToken


# Revoked token
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    # get jti token
    jti = decrypted_token['jti']
    
    # query revoked token are exists
    query = RevokedToken.query.filter(RevokedToken.jti == jti).count()
    return True if len(query) != 0 else False


class UserLogoutAPI(Resource):
    @jwt_required
    def get(self):
        # get user_xid data from token
        get_user = get_jwt_identity()
        
        # get jti data from token
        get_token = get_raw_jwt()['jti']
        
        try:
            # revoke access
            revoked_token_data        = {"jti": get_token}
            revoked_token_insert_data = RevokedToken(**revoked_token_data)
            db.session.add(revoked_token_insert_data)
            db.session.flush()
            
            # data for user log
            user_log_data = {
                "user_xid": get_user,
                "action": "LOGOUT"
            }
            
            # insert user log data to database
            user_log_insert_data = UserLog(**user_log_data)
            db.session.add(user_log_insert_data)
            db.session.flush()
            
            datas = {
                "status": "success",
                "data": None,
                "message": "Token has revoked"
            }

            return datas, 200
        except:
            datas = {
                "status": "error",
                "data": None,
                "message": "Please try again later"
            }

            return datas, 500