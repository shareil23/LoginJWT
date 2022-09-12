from ..Controller import *
from .Config import api

def Routes(api):
    api.add_resource(UserRegisterAPI, '/api/v1/user/register')
    api.add_resource(UserAuthAPI, '/api/v1/user/login')
    api.add_resource(UserTokenRefreshAPI, '/api/v1/user/refresh')
    api.add_resource(UserLogoutAPI, '/api/v1/user/logout')
    api.add_resource(UserHistoryAPI, '/api/v1/user/history', '/api/v1/user/history/<int:page>/<int:totalData>')

Routes(api)