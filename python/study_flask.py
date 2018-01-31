#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/22 16:47
# @Author  : shaoyong_li
# @Site    : 
# @File    : study_flask.py
from flask import Flask
from flask import request
from flask import make_response
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# todo 传递多个值?？
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

def valid_login(username, passwd):
    return True


def log_the_user_in(username):
    return 'Hello ' + username

@app.route('/login', methods=['POST', 'GET'])
def login():
    "curl -XPOST http://127.0.0.1: -d 'username=test&password=test1' -i"
    error = None
    if request.method == 'POST':
        print(request.form)
        if valid_login(request.form['username'],
                       request.form['password']):
            return request.form['username'] + ':' + request.form['password'] + '\r\n'
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return render_template('login.html', error=error)
    return 'must post'


@app.route('/use_cookies')
def use_cookies():
    resp = make_response()
    resp.set_cookie('username', 'test')
    return resp


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """
    curl -F "file=@shell.c" -XPOST http://127.0.0.1:5000/upload
    :return:
    """
    print ('enter upload_file:%s', request.files)
    # 获取当前代码目录
    print (app.root_path)
    if request.method == 'POST':
        try:
            for key in request.files.keys():
                f = request.files[key]
                f.save('./' + secure_filename(f.filename))
            return 'succ'
        except Exception as e:
            print (str(e))
            return 'failed'



if __name__ == '__main__':
    """
    运行python3 **.py 
    默认运行在5000端口
    """
    app.run()