from .Config import caches, jwt
from ..Models import RevokedToken


def getCache(id):
    return caches.get(str(id))


def setCache(id, data):
    return caches.set(str(id), data)


def updateCache(id, new_data):
    caches.delete(str(id))
    return caches.set(str(id), new_data)


def deleteCache(id):
    return caches.delete(str(id))


# Revoked token
@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    # get jti token
    jti = jwt_payload['jti']
    
    # query revoked token are exists
    query = RevokedToken.query.filter(RevokedToken.jti == jti).scalar()
    return query is not None

@jwt.unauthorized_loader
def unauthorized_callback(callback):
    datas = {
        "status": "error",
        "data": None,
        "message": "Unauthorize access"
    }

    return datas, 200