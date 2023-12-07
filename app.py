from flask import Flask, render_template

app = Flask(__name__, static_url_path='/', static_folder='static',template_folder='templates')


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index-0.html')


if __name__ == '__main__':
    app.run()
