from flask import Flask, render_template
from flask_hmin import HMin

app = Flask(__name__)
app.config["HMIN_COMPRESS_HTML"] = True
app.config['HTML_LOAD_REDIS'] = True
app.config['EXPIRIES_TIME'] = 300

hmin = HMin(app=app, redis_config={'host': "localhost", "port": 6379, "db": 0, "password": ''})


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
