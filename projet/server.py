# -*- coding: utf-8 -*-
# @Author: Thibault PECH
# @Date:   2022-02-21 10:03:14
# @Last Modified by:   Thibault PECH
# @Last Modified time: 2022-02-21 10:04:55
#!/usr/bin/python

from flask import Flask, make_response

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Home page'


@app.route('/users/<name>', methods=['POST'])
def create_user(name):

    msg = f'user {name} created'
    return make_response(msg, 201)
