from flask import Blueprint, flash, render_template, redirect, url_for, request
from flask_login import login_required, current_user, logout_user
from pyecharts.charts import Line

from app.email import send_mail
from app.extensions import db
from app.forms import RegisterForm
from app.forms.student import StdinfoForm, Stdpwd, commentss
from app.forms.users import FindpswForm, ResetpwsFrom
from app.model import Student, Paper
from app.model.papers import Record, Paper_C, Single_Q
from app.util import id2Token, check_active_token, token2Id

student_blue = Blueprint('student_blue', __name__)


@student_blue.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        student = Student(idcard=form.userid.data, password=form.password.data,
                          email=form.mail.data, name=form.username.data, _class=form.userclass.data)
        try:
            db.session.add(student)
            db.session.commit()
            print('注册成功')
            token = id2Token(student.idcard)
            print(token)
            send_mail(student.email, '账户激活', 'email/active', username=student.name, token=token)
            flash("注册成功,请查看邮件进行激活")
            return redirect(url_for('index_blue.login'))
        except:
            flash("注册失败:邮箱或者一卡通号重复")
            db.session.rollback()
            return render_template('register.html', form=form)

    return render_template('register.html', form=form)


@student_blue.route('/welcome', methods=['POST', "GET"])
@login_required
def welcome():
    papers = Paper.query.order_by(-Paper.id).limit(5)
    return render_template('student/welcome.html', papers=papers)


@student_blue.route('/exam')
def exam():
    paper_id = request.args.get('paper_id')
    paper = Paper.query.get(paper_id)
    questions = []
    if paper.forms:
        i = 1
        for form in paper.forms:
            if i > 3:
                break
            temp = Single_Q.query.get(form.question_id)
            questions.append(temp)
            i=i+1
    return render_template('student/exam.html', questions=questions)


@student_blue.route('/history')
def history():
    student = Student.query.get(current_user.id)
    return render_template('student/history.html', bean=student)


@student_blue.route('/comment')
@login_required
def comment():
    student = Student.query.get(current_user.id)
    return render_template('student/comments.html', bean=student)


@student_blue.route('/info', methods=['POST', 'GET'])
@login_required
def info():
    form = StdinfoForm()
    if not current_user.is_authenticated:
        flash("请登录!")
        return redirect("/")
    else:
        form.stdname.data = current_user.name
        form.gender.data = current_user.sex
        form.stdclass.data = current_user._class
    if form.validate_on_submit():
        gender = form.gender.data
        stdclass = form.stdclass.data
        stdname = form.stdname.data
        student = Student.query.get(current_user.id)
        student.sex = gender
        student._class = stdclass
        student.name = stdname
        db.session.commit()
        flash("重新登录查看修改结果")
        logout_user()
        return redirect('/')
    return render_template('student/stdinfo.html', form=form)


@student_blue.route('/pwd', methods=['POST', 'GET'])
@login_required
def pwd():
    form = Stdpwd()
    if form.validate_on_submit():
        print("输入正确")
        psd_now = form.pswnow.data
        psd_new = form.psw.data
        if current_user.verify_password(psd_now):
            print('密码正确')
            if reset_passwd_idcard(current_user.idcard, psd_new):
                flash("修改成功,请重新登录")
                print("修改完成")
                logout_user()
                return redirect('/')
    return render_template('student/stdpwd.html', form=form)


@student_blue.route('/activate/<token>/')
def activate(token):
    if check_active_token(token):
        flash("激活成功")
    else:
        flash("激活失败")
    return redirect('/')


@student_blue.route('/findpwd/', methods=['POST', "GET"])
def findpwd():
    form = FindpswForm()
    if form.validate_on_submit():
        mail = form.mail.data
        student = Student.query.filter_by(email=mail).first()
        if student:
            token = id2Token(student.idcard)
            send_mail(mail, "找回密码", "email/findpwd", token=token)
        else:
            flash("您输入的邮箱有误!")
    return render_template('findpsw.html', form=form)


@student_blue.route('/reset/<token>', methods=['POST', 'GET'])
def reset(token):
    if check_active_token(token):
        form = ResetpwsFrom()
        if form.validate_on_submit():
            password = form.password.data
            id = token2Id(token)
            reset_passwd_idcard(id, password)
            return redirect('/')
        return render_template("findpsw.html", form=form)
    else:
        return "邮箱已经超时!"


@student_blue.route('/chart/')
@login_required
def chart():
    records = Record.query.filter_by(student_id=current_user.id).limit(5)
    x = [0, 1, 2, 3, 4, 5]
    y = []
    for record in records:
        y.append(record.score)
        # x.append(record.times)

    bar = (Line()
           .add_xaxis(x)
           .add_yaxis("近五次得分", y)
           )
    return render_template(
        "showcharts.html",
        bar_data=bar.dump_options()
    )


def reset_passwd_idcard(idcard, password):
    student = Student.query.filter_by(idcard=idcard).first()
    if student:
        student.password = password
        db.session.commit()
        flash("密码修改成功")
        return True
    return False


def delete_student_byId(uid):
    student = Student.query.get(uid)
    if student:
        db.session.delete(student)
        db.session.commit()
        return True
    return False


@student_blue.route('/result', methods=['POST', 'GET'])
def results():
    form = commentss()
    paper_id = request.args.get("paper_id")
    if form.validate_on_submit():
        # 获取信息
        com = Paper_C()
        print(type(form))
        com.comment = form.comments.data
        com.student_id = current_user.id
        com.paper_id = paper_id
        db.session.add(com)
        db.session.commit()
    paper = Paper.query.get(paper_id)
    paper.paper_comments
    return render_template('student/testresult.html', form=form, paper=paper)


@student_blue.route('/delete_comment', methods=["POST", "GET"])
def delete_comment():
    id = request.args.get('id')
    if id:
        temp = Paper_C.query.get(id)
        db.session.delete(temp)
        db.session.commit()
    return "删除成功"
