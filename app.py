import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 最初のログイン画面
@app.route('/')
def index():
    return render_template('login.html')

# ログインボタンを押した時の処理
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # 【重要】今はテスト用。どんなID/パスでも「menu.html」へ飛ばす設定です
    # 次のステップで、ここを「データベース照合」に進化させます
    if username and password:
        return render_template('menu.html')
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)