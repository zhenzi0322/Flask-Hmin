from flask import Flask, render_template
from flask_hmin import HMin

app = Flask(__name__)
app.config["HMIN_COMPRESS_HTML"] = True

hmin = HMin(app=app)


@app.route("/")
@hmin.not_compress
def home():
    return render_template("index.html")


@app.route("/test")
def test():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
