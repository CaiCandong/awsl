from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField,TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class StdinfoForm(FlaskForm):
    gender =SelectField('性别',validators=[DataRequired('请选择性别')],choices=[('boy','男'),('girl','女')],render_kw={'style':'width:250px;height:35px;'})
    stdclass=StringField('学院班级',validators=[DataRequired()],render_kw={"class":"layui-input",'style':'width:250px;height:35px;','placeholder':'输入你的学院班级'})
    stdname=StringField('姓名',validators=[DataRequired()],render_kw={"class":"layui-input",'style':'width:250px;height:35px;','placeholder':'输入你的姓名'})
    submit=SubmitField('提交修改',render_kw={'style':'width:100px;height:35px'})

class Stdpwd(FlaskForm):
    pswnow = PasswordField('输入当前账号的密码', validators=[DataRequired(), Length(6, 20, message='密码长度不符合要求')],
                        render_kw={"class": "layui-input", 'style': 'width:250px;height:35px;',
                                   'placeholder': ''})
    psw=PasswordField('输入要修改的密码',validators=[DataRequired(),Length(6,20,message='密码长度不符合要求')],render_kw={"class":"layui-input",'style':'width:250px;height:35px;','placeholder':'6到20个字符'})
    pwd1 = PasswordField('确认修改的密码', validators=[EqualTo('psw',message="两次输入的密码不一致")],render_kw={"class":"layui-input",'style':'width:250px;height:35px;','placeholder':''})
    submit=SubmitField('提交修改',render_kw={'style':'width:100px;height:35px'})

class commentss(FlaskForm):
    comments=TextAreaField('',render_kw={'placeholder':'在此留下你的评论，最长140个字','style':'width:1000px;height:100px;'},validators=[DataRequired(),Length(max=140,message="最多只能输入140个字")])
    submit=SubmitField('留言',render_kw={'style':'text-align: left;margin-top: 15px;width: 150px;height: 35px;'})
