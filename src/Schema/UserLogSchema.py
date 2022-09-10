from ..Config import ma
from ..Models import UserLog


class UserLogSchemaList(ma.SQLAlchemyAutoSchema):
    class Meta:
        model      = UserLog
        include_fk = False