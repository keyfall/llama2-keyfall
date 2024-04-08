from flask import Flask, render_template, blueprints
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

from apps.users.users_view import user_bp
import config

db = SQLAlchemy()

app = Flask(__name__, static_url_path='/static', static_folder="static", template_folder='templates')
app.config.from_object(config)
# CSRF
CSRFProtect(app)
# blueprint
app.register_blueprint(user_bp)



@app.route("/", methods=["post",'get'])
def index():
    return render_template("users/index.html")


if __name__ == '__main__':
    app.run(debug=True)