from asyncio.format_helpers import _format_callback_source
from flask import Flask, render_template, request
from waitress import serve

from UserModel import User
from setting import session
from sqlalchemy import *
from sqlalchemy.orm import *

app = Flask(__name__)


@app.route('/', methods=['POST'])
# 登録処理
def index_to():

    name = request.form['name']

    session.add(User(name))
    session.commit()

    message = name + "の登録が完了しました！"

    return message


@app.route('/', methods=["GET"])
def index():

    name = request.args.get('name')

    get_db = session.query(User.name).\
        filter(User.name == name).\
        all()

    if len(get_db) == 0:
        message = "登録が０件です。"
        return render_template('index.html')
    else:
        message = "登録あり:"
        return render_template('index.html', get_db=get_db)

    return str(name) + str(message)


@app.route('/<name>')
def hello(name):
    # URL からパラメータを受け取る
    return render_template("hello.html", name=name, method="URLパラメータ")


@app.route('/param', methods=['GET', 'POST'])
def hello_parameter():

    if request.method == 'POST':
        # post　受け取る
        name = request.form['name']
    else:
        # get 受け取る
        name = request.args.get('name')

    return render_template("hello.html", name=name, method=request.method)


# if __name__ == '__main__':
#    app.run()

if __name__ == "__main__":
    # app.run('0.0.0.0',port=5000)
    serve(app, host='0.0.0.0', port=5000)
