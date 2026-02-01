import os
from flask import Flask, render_template, request
from supabase import create_client
from dotenv import load_dotenv

load_dotenv() # .envから鍵を読み込む

app = Flask(__name__)

# データベース接続
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # データベースから講座一覧を取得
    response = supabase.table("courses").select("*").execute()
    return render_template('menu.html', courses=response.data)

if __name__ == '__main__':
    app.run(debug=True)