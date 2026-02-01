import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# サイトのトップ（https://.../）にアクセスしたときに login.html を表示する命令
@app.route('/')
def index():
    return render_template('login.html')

# ログインボタンを押した後の動き
@app.route('/login', methods=['POST'])
def login():
    return "eラーニング農園へようこそ！あなたのスキルを育てましょう。"

if __name__ == '__main__':
    app.run(debug=True)