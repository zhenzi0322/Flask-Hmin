# Flask-Hmin

## 安装
使用`pip`进行安装：
```shell
pip install Flask-Hmin
```

或者使用`pipenv`：
```shell
pipenv install Flask-Hmin
```

或者使用`poetry`：
```shell
poetry add Flask-Hmin
```

您也可以下载存储库并手动安装它，执行以下操作：
```shell
git clone https://github.com/zhenzi0322/Flask-Hmin.git
cd Flask-Hmin
python setup.py install
```

## 使用方法

### 所有模板视图html都压缩
```python
from flask import Flask, render_template
from flask_hmin import HMin

app = Flask(__name__)
app.config["HMIN_COMPRESS_HTML"] = True

HMin(app=app)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
```

### 指定某个模板视图不压缩
```python
from flask import Flask, render_template
from flask_hmin import HMin

app = Flask(__name__)
app.config["HMIN_COMPRESS_HTML"] = True

hmin = HMin(app=app)


@app.route("/")
@hmin.not_compress
def home():
    # 该视图模板不压缩
    return render_template("index.html")


@app.route("/test")
def test():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
```

### 把模板HTML内容加载到Redis中
```python
from flask import Flask, render_template
from flask_hmin import HMin

app = Flask(__name__)
app.config["HMIN_COMPRESS_HTML"] = True
app.config['HTML_LOAD_REDIS'] = True

hmin = HMin(app=app, redis_config={'host': "localhost", "port": 6379, "db": 0, "password": ''})


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
```
默认过期时间是一天。86400秒。

如果需要自定义`Redis`过期时间，如下：
```python
app.config['EXPIRIES_TIME'] = 300
```
上面是配置300秒过期。