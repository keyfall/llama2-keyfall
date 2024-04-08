from flask import Blueprint, render_template, request

from .Users import User
from .user_func import user_func

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = User()
    if request.method == 'POST':
        # 这里实现登录逻辑，如验证用户名和密码
        if form.validate_on_submit():
            return 'ok'
    return render_template('users/login.html', form=form)

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 这里实现注册逻辑，如保存新用户信息到数据库
        pass
    return render_template('user/register.html')