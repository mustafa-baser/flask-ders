from flask import Blueprint

from flask import Flask, render_template, request

index_bp = Blueprint('index', __name__, url_prefix='/')

@index_bp.route('/')
def index():

    title = 'BÖTE Ders Bloğu'
    posts = [
            { 'author': {'username':'emrah'}, 'body': 'Nasılsınız?'},
            { 'author': {'username':'melike'}, 'body': 'Kar yağdı derse gelemiyorum'},
            ]


    return render_template('index.html', title=title, posts=posts)
    

@index_bp.route('/test')
def test():
    return "TEST ROUTE"

@index_bp.route('/nedir')
def nedir():
    return "Nedir Bu?"
