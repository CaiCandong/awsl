from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class FindpswForm(FlaskForm):
    mail = StringField('', validators=[DataRequired(), Email(message='邮箱格式不正确')],
                           render_kw={'placeholder': "在此输入注册时的邮箱",
                                      'style': 'width:300px;height:40px;text-indent:15px;margin-top:0px;border-radius:8px'})
    submit = SubmitField('', render_kw={'class': "button button-action button-pill", 'value': "点击找回",
                                            'style': 'margin-top:25px;margin-left:110px'})
class ResetpwsFrom(FlaskForm):
    password = PasswordField('', validators=[DataRequired(), Length(6, 20, message='密码长度不符合要求')],
                                 render_kw={'placeholder': "在此输入修改的密码",
                                            'style': 'width:300px;height:40px;text-indent:15px;margin-top:0px;border-radius:8px'})
    password2 = PasswordField('', validators=[EqualTo('password', message="两次输入的密码不一致")],
                                  render_kw={'placeholder': "再次输入密码",
                                             'style': 'width:300px;height:40px;text-indent:15px;margin-top:0px;border-radius:8px'})
    submit = SubmitField('', render_kw={'class': "button button-action button-pill", 'value': "点击找回",
                                        'style': 'margin-top:25px;margin-left:110px'})
