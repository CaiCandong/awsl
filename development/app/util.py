from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
#
from app.extensions import db
from app.model import Student
#
#
# # id加密为token
def id2Token(id):
    s = Serializer(current_app.config['SECRET_KEY'])
    return s.dumps({'id': id})
#
#
# token 解密为id 失败返回false,成功返回id
def token2Id(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        return False
    return data.get('id')


# 对账号进行激活
def check_active_token(token):
    id_ = token2Id(token)
    if not id_:
        return False
    student =Student.query.filter_by(idcard=id_).first()
    if not student:
        return False
    if not student.confirmed:
        student.confirmed = True
        db.session.add(student)
    return True
