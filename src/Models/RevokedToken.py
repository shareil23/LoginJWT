from ..Config import db

import time


class RevokedToken(db.Model):
    __tablename__ = 'revoked_tokens'

    id    = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    jti   = db.Column(db.Text())
    utime = db.Column(db.Integer())
    
    def __init__(self, **data):
        self.jti      = data['jti']
        self.utime    = time.time()
        
    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti = jti).first()
        return bool(query)