from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home_route():
    return render_template('index.html')


@app.route('/index.html')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def pages(page_name):
    return render_template(page_name)


if __name__ == '__main__':
    app.run()