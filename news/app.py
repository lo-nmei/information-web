#!/usr/bin/env python3

import os
import json
from flask import Flask, render_template, abort

app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

with open('/home/shiyanlou/files/helloshiyanlou.json') as file:
    shiyanlou=json.loads(file.read())
with open('/home/shiyanlou/files/helloworld.json') as file:
    world=json.loads(file.read())

@app.route('/')
def index():
    return render_template('index.html',shiyanlou_title=\
            shiyanlou['title'],world_title=world['title'])

@app.route('/files/<filename>')
def file(filename):
    path_dir='/home/shiyanlou/files'
    file_name=filename + '.json'
    path=os.path.join(path_dir,file_name)
    if os.path.exists(path):
        if filename=='helloshiyanlou':
            return render_template('file.html',file_content=\
                    shiyanlou['content'])
        else:
            return render_template('file.html',file_content=\
                    world['content'])
    else:
        abort(404)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404



if __name__=='__main__':
    app.run(port=3000)
