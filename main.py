import csv
import os

from flask import Flask, request, redirect
from flask.templating import render_template
app = Flask(__name__)


def write_to_csv_file(data: dict):
    path = os.path.join(os.getcwd(), 'data', 'emails.csv')
    with open(path, 'a', newline='') as csv_file:
        email = data['email']
        subject = data['subject']
        message = data['message']

        csv_writer = csv.writer(csv_file,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/send_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv_file(data)

        return redirect('thanks.html')
    else:
        return 'error'


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