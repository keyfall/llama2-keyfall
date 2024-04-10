from flask import Flask, render_template, url_for, redirect
from flask_wtf.csrf import CSRFProtect
from apps.users.users_view import user_bp
import config
from import_third import session

app = Flask(__name__, static_url_path='/static', static_folder="static", template_folder='templates')
app.config.from_object(config)
# CSRF
CSRFProtect(app)
# blueprint
app.register_blueprint(user_bp)

# session
session.init_app(app)



@app.route("/", methods=["post",'get'])
def index():
    # 判断用户是否存在
    return redirect(url_for('user.login'))

@app.before_request
def before_request():
    # 判断用户是否在session
    if 'username' not in session:
        return redirect(url_for('user.login'))

if __name__ == '__main__':
    app.run(debug=True)