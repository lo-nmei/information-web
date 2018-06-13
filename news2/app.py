#!/usr/bin/env python3

import os
import json
from datetime import datetime
from flask import Flask, render_template, abort, url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/shiyanlou'

db=SQLAlchemy(app)

class File(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(80))
    create_time=db.Column(db.DateTime)
    category_id=db.Column(db.Integer,db.ForeignKey('category.id'))
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


class Category(db.Model):

    id = db.Column( db.Integer, primary_key = True)
    name = db.Column( db.String(80) )

    def __init__(self,name):
        self.name = name

    def _repr__(self):
        return '<Category : %s>' % self.name



@app.route('/')
def index():
        return render_template('index.html',l=File.query.all())

@app.route('/files/<file_id>')
def file(file_id):
    f=File.query.get_or_404(file_id)
    return render_template('file.html',f=f)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404



if __name__=='__main__':
    app.run(port=3000)
