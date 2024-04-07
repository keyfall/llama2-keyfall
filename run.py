from flask import Flask, render_template, blueprints

from apps.users.users_view import user_bp

app = Flask(__name__, static_url_path='/static', static_folder="static", template_folder='templates')


# blueprint
app.register_blueprint(user_bp)

@app.route("/", methods=["post",'get'])
def index():
    return render_template("users/index.html")


if __name__ == '__main__':
    app.run(debug=True)