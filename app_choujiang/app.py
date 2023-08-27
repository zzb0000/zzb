#支持通过游览器访问代码
#需要web框架
#pip install Flask
import t
from flask import Flask,render_template
from random import randint
#创建app
app = Flask(__name__)

hero = t.urls

@app.route("/index")
#创建访问内容
def index():
    return render_template('index.html',hero=hero)

@app.route("/choujiang")
#创建访问内容
def choujiang():
    num = randint(0,len(hero)-1)
    return render_template('index.html',hero=hero,h=hero[num])

#运行app
app.run(debug=True)
