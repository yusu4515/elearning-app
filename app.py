import os
import psycopg2
from flask import Flask, render_template, request, redirect, url_for, session
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'isms-security-key') # セキュリティキー

# .envから読み込み
DATABASE_URL = os.environ.get('DATABASE_URL')

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

@app.route('/')
def index():
    return "E-Learning App is Running!" # まずは動作確認用

if __name__ == '__main__':
    app.run(debug=True)