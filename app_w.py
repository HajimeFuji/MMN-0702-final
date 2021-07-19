import os
# Flask から importしてflaskを使えるようにする
import sqlite3, datetime as dt
from flask import Flask, render_template, request, redirect, session

# appの名前でFlaskアプリを作っていく
app_w = Flask(__name__)
# ここまでおまじない

app_w.secret_key="winkel"

@app_w.route("/")
def init():
    return render_template('init.html')

# DBへの接続
@app_w.route("/index/w")
def index():
    conn = sqlite3.connect("maintenance.db")
    c=conn.cursor()
    c.execute("select name from users where id = 1")
    user_info = c.fetchone()
    c.close()
    return render_template("index_w.html", user = user_info)


if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します。
    app_w.run(debug=True)