from flask import flash, render_template, Blueprint, redirect, url_for
from flask_login import current_user, login_user, logout_user

from app.email import send_mail
from app.forms import LoginForm
from app.model import Student, Admin, Teacher
from app.util import id2Token

index_blue = Blueprint('index_blue', __name__)


@index_blue.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('index_blue.login'))


@index_blue.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect_tag(current_user.tag)
    elif form.validate_on_submit():
        user_id = form.userid.data
        user_passwd = form.password.data
        remember = form.remember.data
        tag = form.tag.data
        if tag == 'student':
            user = Student.query.filter_by(idcard=user_id).first()
        elif tag == 'teacher':
            user = Teacher.query.filter_by(idcard=user_id).first()
        else:
            user = Admin.query.filter_by(idcard=user_id).first()
        if not user:
            flash("登录密码错误，请重新输入")
        elif user.verify_password(password=user_passwd):
            if user.tag == 'student':
                if user.confirmed:
                    flash("登录成功")
                    login_user(user, remember=remember)
                    return redirect_tag(tag)
                else:
                    token = id2Token(user.idcard)
                    send_mail(user.email, '账户激活', 'email/active', username=user.name, token=token)
                    flash("您的账号还未激活，请查看邮件进行激活")
            else:
                flash("登录成功")
                login_user(user, remember=remember)
                return redirect_tag(tag)

    return render_template('login.html', form=form)


@index_blue.route('/logout/')
def logout():
    logout_user()
    return redirect('/')


def redirect_tag(tag):
    if tag == 'student':
        return render_template('commons/base4.html')
    if tag == "teacher":
        return render_template('commons/base2.html')
    else:
        return render_template('commons/base2.html')
