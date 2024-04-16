from flask import Blueprint, render_template, request, redirect, url_for

from .Users import User
from .user_func import user_func
from import_third import session

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = User()
    if request.method == 'POST':
        # 这里实现登录逻辑，如验证用户名和密码
        if form.validate_on_submit():
            print(form.name.data)
            user_f = user_func(form.name.data,form.password.data)
            user_f.selectUserPwd()
            session["username"] = form.name.data
            session["password"] = form.password.data
            return render_template('chat/chat.html', form=form)

    return render_template('users/login.html', form=form)

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = User()
    if request.method == 'POST':
        # 这里实现注册逻辑，如保存新用户信息到数据库
        if form.validate_on_submit():
            user_f = user_func(form.name.data,form.password.data)
            user_f.insetinto()
            session["username"] = form.name.data
            session["password"] = form.password.data
            return render_template('chat/chat.html', form=form)
    return render_template('users/register.html', form=form)

@user_bp.route('/logout')
def logout():
    session.clear()  # 清除会话数据
    return redirect(url_for('user.login'))
