from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

class User(FlaskForm):
    name = StringField('uname', validators=[DataRequired(message="用户名不能为空"),
                                            Length(0,16,message="长度不能超过0-16")],
                       render_kw={'placeholder': "输入用户名"})
    password = PasswordField('password', validators=[DataRequired(message="密码不能为空"),
                                            Length(0, 16, message="长度不能超过0-16")],
                       render_kw={'placeholder': "输入密码"})