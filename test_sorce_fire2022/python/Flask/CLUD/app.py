import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# ====== DB 作成


class Post(db.Model):

    __tablename__ = 'Post_TB'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    body = db.Column(db.String(140), nullable=False)


# ====== index
@app.route('/')
def index():
    # === DB 一覧表示
    get_posts = Post.query.all()

    # get データ 1つ
    p_get = Post.query.get(2)

    # filter
    p02_get = Post.query.filter(Post.title == 'test_003')

    return render_template('index.html', get_posts=get_posts, p_get=p_get,
                           p02_get=p02_get)


# ====== 新規登録 ======
@app.route('/new', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # POST 送信時
        title = request.form.get('title')
        body = request.form.get('body')

        post = Post(title=title, body=body)

        # === DB に保存
        db.session.add(post)
        db.session.commit()

        return redirect('/')

    else:
        # GET
        return render_template('new.html')

# ====== 編集画面 ======

# === GET でアクセスの場合、編集画面を表示
# === POST 送信がきた場合は、編集を行う


@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def update_item(id):

    # Post テーブルから id 取得
    post = Post.query.get(id)
    # === 編集画面を表示
    if request.method == 'GET':
        return render_template('edit.html', post=post)
    # === 編集を行う
    else:
        post.title = request.form.get('title')
        post.body = request.form.get('body')
        db.session.commit()
        return redirect('/')

# ====== 削除処理 ======


@app.route('/<int:id>/delete', methods=['GET'])
def delete(id):
    # Post テーブルから id 取得
    post = Post.query.get(id)

    # 投稿を削除
    db.session.delete(post)

    # 削除を反映
    db.session.commit()

    # index ページへリダイレクト
    return redirect('/')


if __name__ == '__main__':
    app.run()
