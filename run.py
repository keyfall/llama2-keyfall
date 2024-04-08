from flask import Flask, render_template, url_for, redirect
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from apps.users.users_view import user_bp
import config


app = Flask(__name__, static_url_path='/static', static_folder="static", template_folder='templates')
app.config.from_object(config)
# CSRF
CSRFProtect(app)
# blueprint
app.register_blueprint(user_bp)

# session
session = Session(app)



@app.route("/", methods=["post",'get'])
def index():
    # 判断用户是否存在
    return redirect(url_for('user.login'))

@app.before_request
def before_request():
    # 判断用户是否有存储
    # session.get
    pass

if __name__ == '__main__':
    app.run(debug=True)