from ..Config import db

from sqlalchemy.dialects.postgresql import UUID
import uuid
import time

class User(db.Model):
    __tablename__ = 'user'

    id       = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    user_xid = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
    ctime    = db.Column(db.Integer())
    utime    = db.Column(db.Integer())
    hash_val = db.Column(db.Text())
    email    = db.Column(db.Text())

    def __init__(self, **data):
        self.user_xid = data['user_xid']
        self.ctime    = time.time()
        self.utime    = data['utime']
        self.hash_val = data['hash_val']
        self.email    = data['email']