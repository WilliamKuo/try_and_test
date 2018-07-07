#!/usr/bin/python
import json
from pprint import pprint
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)



@app.route('/', defaults={'test_id': None}, methods=['GET', 'DELETE', 'POST'])
@app.route('/<test_id>', methods=['GET', 'DELETE', 'POST'])
def index(test_id):
    if test_id:
        nu = test_id
    else:
        nu ='' 

    if request.method == 'GET':
        r = 'GET METHOD' + nu
    elif request.method == 'POST':
        r = 'POST METHOD' + nu
        # data = request.form.get('test_data', 'FAIL!!!!!!!!!!!!!!!!!!')
        data = request.get_json('test_data')
        pprint(data)
    elif request.method == 'DELETE':
        r = 'DELETE METHOD' + nu
    else:
        r = render_template('home.html')

    return r 


if __name__ == '__main__':
    app.run(debug=True)
