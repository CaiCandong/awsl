from flask_wtf import  FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,SelectField
from wtforms.validators import DataRequired,Length,EqualTo,Email

class AddStudent(FlaskForm):
    userid = StringField('',render_kw={'style':'width:400px;height:42px;text-indent:10px;margin-left:50px;margin-top:60px;','placeholder':"在此输入学生账号"}, validators=[DataRequired(), Length(10, 12, message="一卡通号长度不符合要求")])
    username = StringField('', validators=[DataRequired(),], render_kw={'placeholder': "在此输入姓名",
                                                                        'style': 'width:400px;height:42px;text-indent:10px;margin-left:50px;margin-top:10px;border-radius:8px'})
    password = PasswordField('',render_kw={'style':"width:400px;height:42px;text-indent:10px;margin-left:50px;margin-top:10px",'placeholder':"在此输入账号的密码"}, validators=[DataRequired(), Length(6, 20, message="密码长度不符合要求")])
    password2 = PasswordField('', render_kw={'style':"width:400px;height:42px;text-indent:10px;margin-left:50px;margin-top:10px",'placeholder':"再次输入账号的密码"},validators=[EqualTo('password', message="两次输入的密码不一致")])
    mail = StringField('',  render_kw={'style':"width:400px;height:42px;text-indent:10px;margin-left:50px;margin-top:10px",'placeholder':"在此输入邮箱地址"},validators=[DataRequired(), Email(message="邮箱格式不正确")])
    submit = SubmitField('', render_kw={'value': "注册", 'style':'margin-top:25px;margin-left:50px;height:40px;width:100px'})


class teacherForm(FlaskForm):
    userid = StringField('', render_kw={
        'style': 'width:400px;height:42px;text-indent:10px;margin-left:50px;margin-top:60px;',
        'placeholder': "在此输入教师账号"}, validators=[DataRequired(), Length(10, 12, message="一卡通号长度不符合要求")])
    password = PasswordField('', render_kw={
        'style': "width:400px;height:42px;text-indent:10px;margin-left:50px;margin-top:10px",
        'placeholder': "在此输入账号的密码"}, validators=[DataRequired(), Length(6, 20, message="密码长度不符合要求")])
    password2 = PasswordField('', render_kw={
        'style': "width:400px;height:42px;text-indent:10px;margin-left:50px;margin-top:10px",
        'placeholder': "再次输入账号的密码"}, validators=[EqualTo('password', message="两次输入的密码不一致")])
    mail = StringField('',
                       render_kw={'style': "width:400px;height:42px;text-indent:10px;margin-left:50px;margin-top:10px",
                                  'placeholder': "在此输入邮箱地址"}, validators=[DataRequired(), Email(message="邮箱格式不正确")])
    submit = SubmitField('',
                         render_kw={'value': "注册", 'style': 'margin-top:25px;margin-left:50px;height:40px;width:100px'})

class problemForm(FlaskForm):
    problem=TextAreaField('在此输入问题的描述',render_kw={'placeholder':'问题的描述，如：1+1=（）','style':'width:80%;height:80px;'})
    choiceA=TextAreaField('选项A',render_kw={'placeholder':'选项的描述，如：1','style':'width:80%;height:50px;'},validators=[DataRequired(),Length(min=1,message='选项的长度不符合要求')])
    choiceB = TextAreaField('选项B', render_kw={'placeholder': '选项的描述，如：2', 'style': 'width:80%;height:50px;'},validators=[DataRequired(),Length(min=1,message='选项的长度不符合要求')])
    choiceC = TextAreaField('选项C', render_kw={'placeholder': '选项的描述，如：3', 'style': 'width:80%;height:50px;'},validators=[DataRequired(),Length(min=1,message='选项的长度不符合要求')])
    choiceD = TextAreaField('选项D', render_kw={'placeholder': '选项的描述，如：4', 'style': 'width:80%;height:50px;'},validators=[DataRequired(),Length(min=1,message='选项的长度不符合要求')])
    correct = SelectField(label='请选择正确选项',validators=[DataRequired()],render_kw={ 'style':'width:100px;height:40px'},choices=[('A', 'A'), ('B', 'B'), ('C', 'C'),('D','D')],default = 'A',)
    # problemanalysis = TextAreaField('在此输入问题的解析', render_kw={'placeholder': '问题的描述，如：1+1=（）', 'style': 'width:80%;height:80px;'})
    submit=SubmitField('提交')
