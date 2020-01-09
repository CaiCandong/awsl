from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_login import login_required

from app.extensions import db
from app.forms.admin import problemForm, teacherForm, AddStudent
from app.model import Single_Q, Student, Teacher, Paper, Paper_C
from app.views.teacher import delete_teacher_byId

admin_blue = Blueprint('admin_blue', __name__)


@admin_blue.route('/welcome/')
@login_required
def welcome():
    return render_template('admin/welcome.html/')


@admin_blue.route('/students/')
@login_required
def student():
    students = Student.query.paginate(per_page=10)
    return render_template('admin/students.html', pagination=students)


@admin_blue.route('/student_idcard', methods=['POST', 'GET'])
@login_required
def student_idcard():
    idcard = request.args.get('idcard')
    if idcard:
        print(idcard)
        idcard = int(idcard)
        student = Student.query.filter_by(idcard=idcard).first()
        return render_template('admin/students.html', student=student)
    return redirect(url_for('admin_blue.student'))


@admin_blue.route('/teachers/')
@login_required
def teachers():
    ts = Teacher.query.paginate(per_page=10)
    return render_template('admin/teachers.html', pagination=ts)


@admin_blue.route('/comments')
@login_required
def comments():
    ts = Paper_C.query.paginate(per_page=10)
    return render_template('admin/comments.html', pagination=ts)


@admin_blue.route('/problems')
@login_required
def problems():
    questions = Single_Q.query.paginate(per_page=10)
    return render_template('admin/problems.html', pagination=questions)


@admin_blue.route('/papers')
@login_required
def papers():
    papers = Paper.query.paginate(per_page=10)
    return render_template('admin/papers.html', pagination=papers)


@admin_blue.route('/profile/')
@login_required
def profile():
    return "个人中心"


@admin_blue.route('/paper_add')
@login_required
def paper_add():
    return render_template('admin/paper_add.html')


@admin_blue.route('/problem_add')
@login_required
def problem_add():
    form = problemForm()
    return render_template('admin/problem_add.html', form=form)


@admin_blue.route('/student_add', methods=["POST", "GET"])
@login_required
def student_add():
    form = AddStudent()
    if form.validate_on_submit():
        student = Student()
        student.idcard = form.userid.data
        student.password = form.password.data
        student.email = form.mail.data
        student.name = form.username.data
        student.sex = "未填写"
        student.confirmed = True
        try:
            db.session.add(student)
            db.session.commit()
            return "注册成功"
        except:
            db.session.rollback()
            return "注册失败:邮箱或者一卡通号重复"
    return render_template('admin/student_add.html', form=form)


@admin_blue.route('/teacher_add', methods=["POST", "GET"])
@login_required
def teacher_add():
    form = teacherForm()
    if form.validate_on_submit():
        teacher = Teacher()
        teacher.idcard = form.userid.data
        teacher.password = form.password.data
        teacher.email = form.mail.data
        try:
            db.session.add(teacher)
            db.session.commit()
            return "注册成功"
        except:
            db.session.rollback()
            return "注册失败:邮箱或者一卡通号重复"
    return render_template('admin/teacher_add.html', form=form)


from .student import delete_student_byId


@admin_blue.route('/delete_student')
@login_required
def delete_student():
    uid = request.args.get('uid')
    print(uid)
    uid = int(uid)
    if delete_student_byId(uid):
        return redirect(url_for('admin_blue.student'))
    else:
        return "删除失败"


@admin_blue.route('/delete_teacher')
@login_required
def delete_teacher():
    uid = request.args.get('uid')
    print(uid)
    uid = int(uid)
    if delete_teacher_byId(uid):
        return redirect(url_for('admin_blue.teachers'))
    else:
        return "删除失败"
