from flask import Blueprint, render_template, request, url_for
from functions import *
import logging
import os


main = Blueprint('main', __name__, template_folder='templates')

picfolder = os.path.join('uploads', 'images')

logging.basicConfig(filename="basic.log", level=logging.INFO)



src = os.path.join(picfolder, 'dostoevskiy.jpg')


@main.route('/')
def index_page():
    return render_template('index.html')

@main.route('/page')
def test():
    return render_template('index.html', img=src)


@main.route('/search.html')
def list_post():
    key_search = request.args['s']
    index_posts = desaired_content(key_search)
    posts = desired_posts(index_posts)
    logging.info(f"Посты по запросу {key_search} запрошены")
    return render_template('search.html', posts=posts, quest=key_search)





