from flask import Flask, request, render_template
from datetime import datetime


app = Flask(__name__, 
            template_folder='./templates',
            static_folder='./static')


@app.route("/")
def index():
    return "Hello World!"


@app.route("/login")
def login():
    print("正在访问Login")
    return render_template("")


if __name__ == "__main__":
    # 开启debug模式
    app.run(debug=True,
            host="0.0.0.0",
            port=5001)