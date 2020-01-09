from flask import Blueprint

from app.extensions import db
from app.model import Teacher

teacher_blue= Blueprint('teacher', __name__)

def delete_teacher_byId(uid):
    teacher = Teacher.query.get(uid)

    try:
        db.session.delete(teacher)
        db.session.commit()
    except:
        db.session.rollback()
        return False
    return True