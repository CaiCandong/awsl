from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import db
from flask_login import UserMixin
from app.extensions import login_manage


class Person(db.Model, UserMixin):
    __abstract__ = True
    # 系统内部编号
    id = db.Column(db.Integer, primary_key=True)
    # 一卡通号
    idcard = db.Column(db.Integer, unique=True)
    # 用户名
    name = db.Column(db.String(64), unique=True)
    # 密码
    password_hash = db.Column(db.String(128))
    # 身份标识 123为学生,教师,管理员
    tag = db.Column(db.String(32), default="student")

    @property
    def password(self):
        raise AttributeError('密码不可读')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Student(Person):
    '''
    编号，姓名，性别，电话，邮箱，密码
    '''
    __tablename__ = 'students'
    name = db.Column(db.String(64), unique=True)
    # 性别
    sex = db.Column(db.String(16), default="未填写")
    # 邮箱
    email = db.Column(db.String(64), unique=True)
    # 班级
    _class = db.Column(db.String(64))
    #  激活标记
    confirmed = db.Column(db.Boolean, default=False)
    # 评论引用本表,反向获取评论
    comments = db.relationship('Paper_C', backref='comments', lazy=True)
    # 做题记录引用本表,反向引用做题记录
    records = db.relationship("Record", backref='records', lazy=True)


class Teacher(Person):
    __tablename__ = "teachers"
    # 邮箱
    email = db.Column(db.String(64), unique=True)


class Admin(Person):
    __tablename__ = "admins"


@login_manage.user_loader
def user_loader(uid):
    uid = int(uid)
    if uid < 1000:
        return Admin.query.get(int(uid))
    elif uid < 3000:
        return Teacher.query.get(int(uid))
    else:
        return Student.query.get(int(uid))
