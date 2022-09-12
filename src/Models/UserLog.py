from ..Config import db

import time
from sqlalchemy.dialects.postgresql import UUID
import uuid

class UserLog(db.Model):
    __tablename__ = 'user_log'

    id       = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    user_xid = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
    action   = db.Column(db.Text())
    utime    = db.Column(db.Integer())

    def __init__(self, **data):
        self.user_xid = data['user_xid']
        self.action   = data['action']
        self.utime    = time.time()