from flask import Blueprint, render_template, request

from user_func import user_func
user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 这里实现登录逻辑，如验证用户名和密码
        pass
    return render_template('user/login.html')

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 这里实现注册逻辑，如保存新用户信息到数据库
        pass
    return render_template('user/register.html')