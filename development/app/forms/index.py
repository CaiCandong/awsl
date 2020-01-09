from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class LoginForm(FlaskForm):
    userid=StringField('一卡通号',validators=[DataRequired(),Length(10,12,message='一卡通号长度不符合要求')],render_kw={'class':"form-control",'id':"login" , 'placeholder':"一卡通号/职工号" ,'aria-describedby':"glyphicon-envelope-addon"})
    password=PasswordField('密码',validators=[DataRequired(),Length(6,20,message='密码长度不符合要求')],render_kw={'class':"form-control",'id':"password", 'aria-describedby':"password-addon" ,'placeholder':"请输入密码"})
    tag = SelectField('选择您的身份', validators=[DataRequired('请选择身份')],choices=[('student', '学生'), ('teacher', '教师'), ('admin', '管理员')])
    remember=BooleanField('记住登录')
    submit=SubmitField('立即登录',render_kw={'class':"btn btn-green", 'value':"登录"})

class RegisterForm(FlaskForm):
    userid=StringField('',validators=[DataRequired(),Length(10,12,message='一卡通号长度不符合要求')],render_kw={'placeholder':"在此输入一卡通号",'style':'width:300px;height:30px;text-indent:15px;margin-top:0px;border-radius:8px'})
    password=PasswordField('',validators=[DataRequired(),Length(6,20,message='密码长度不符合要求')],render_kw={'placeholder':"在此输入密码",'style':'width:300px;height:30px;text-indent:15px;margin-top:0px;border-radius:8px'})
    password2=PasswordField('',validators=[EqualTo('password',message="两次输入的密码不一致")],render_kw={'placeholder':"再次输入密码",'style':'width:300px;height:30px;text-indent:15px;margin-top:0px;border-radius:8px'})
    mail=StringField('',validators=[DataRequired(),Email(message='邮箱格式不正确')],render_kw={'placeholder':"在此输入邮箱",'style':'width:300px;height:30px;text-indent:15px;margin-top:0px;border-radius:8px'})
    username = StringField('', validators=[DataRequired(),], render_kw={'placeholder': "在此输入姓名",
                                                                        'style': 'width:300px;height:30px;text-indent:15px;margin-top:0px;border-radius:8px'})
    userclass = StringField('', validators=[DataRequired(),], render_kw={'placeholder': "在此输入学院班级",
                                                                         'style': 'width:300px;height:30px;text-indent:15px;margin-top:0px;border-radius:8px'})
    submit=SubmitField('',render_kw={'class':"button button-action button-pill",'value':"立即注册",'style':'margin-top:25px;margin-left:110px'})
