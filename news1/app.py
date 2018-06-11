#!/usr/bin/env python3

import os
import json
from datetime import datetime
from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/shiyanlou.db']
db=SQLAlchemy(app)

class File(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(80))
    create_time=db.Column(db.Datetime)
    category_id=db.Colulmn(db.Integer,db.ForeignKey(category.id))
    content=db.Column(db.Text)
    category = db.relationship( 'Category',backref =db.backref('files',lazy='dynamic'))

    def __init__(self,title,category,content,create_time=None):
        self.title=title
        if create_time is None:
            create_time=datetime.utcnow()
        self.create_time=create_time
        self.category=category
        self.content=content

    def __repr__(self):
        return '<File : %s>' % self.title


class Category(db.model):

    id = db.Column( db.Integer, primary_key = True)
    name = db.Column( db.String(80) )

    def __init__(self,name):
        self.name = name

    def _repr__(self):
        return '<Category : %s>' % self.name

file = File()
category  = Category()

@app.route('/')
def index():
    file_t=File.query.all()
    for i in file.id:
        return render_template('index.html',file_title=\
            category.files)

@app.route('/files/<file_id>')
def file(file_id):
    file_c=File.query().all()
    for k  in file.id:
        if file_id == k:
            return render_template('file.html',file_title=file.tilte,\
                    content = file.content,\
                    create_time = file.create_time,category=file.category)
         else:
             abort(404)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404



if __name__=='__main__':
    app.run(port=3000)
