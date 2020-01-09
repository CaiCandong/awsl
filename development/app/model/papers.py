from datetime import datetime



from app.extensions import db


# 单选题
class Single_Q(db.Model):
    __tablename__ = 'single_questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(128))
    ansA = db.Column(db.String(64))
    ansB = db.Column(db.String(64))
    ansC = db.Column(db.String(64))
    ansD = db.Column(db.String(64))
    correct = db.Column(db.String(8))
    tag = db.Column(db.String(8))


# 试卷组成
class Form(db.Model):
    __tablename__ = "forms"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('single_questions.id'))
    paper_id = db.Column(db.Integer, db.ForeignKey('papers.id'))


class Paper(db.Model):
    __tablename__ = 'papers'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(32))
    describe = db.Column(db.String(128))
    startDate = db.Column(db.Date, default=datetime.now)
    status = db.Column(db.Boolean, default=True)
    source_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))

    # 获取comments对象 反向引用 评论的paper_id指向本表
    paper_comments = db.relationship('Paper_C', backref='paper_comments', lazy=True)
    # 获取question对象 反向引用
    forms = db.relationship('Form', backref='forms', lazy=True)


class Record(db.Model):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True)
    paper_id = db.Column(db.Integer, db.ForeignKey('papers.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    # 得分
    score = db.Column(db.Integer, default=0)
    # 总分
    total = db.Column(db.Integer, default=100)
    times = db.Column(db.TIMESTAMP, default=datetime.utcnow)


# 试卷评论区
class Paper_C(db.Model):
    __tablename__ = 'paper_comments'
    id = db.Column(db.Integer, primary_key=True)
    # 学生与试卷多对多
    paper_id = db.Column(db.Integer, db.ForeignKey('papers.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    comment = db.Column(db.String(140), default="试卷太难,不想评论")
    times=db.Column(db.TIMESTAMP,default=datetime.utcnow)