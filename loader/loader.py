from flask import Blueprint, render_template, request
from functions import add_post, add_tegs, is_filename_allowed
import logging

# создание блюпринта и логера
loader = Blueprint('loader', __name__, template_folder='templates')
logging.basicConfig(filename="basic.log", level=logging.INFO)

# представление страницы для создания поста
@loader.route('/post')
def load_page():
    return render_template('post_form.html')


# сбор функций для создания поста и представление страницы результата создания
@loader.route('/post_uploaded', methods=['POST'])
def post_upload():

    picture = request.files.get('picture')

    if not picture:
        logging.info(f'Файл "{ picture.filename }" не удалось загрузить')
        return render_template('post_uploaded.html', error=True)

    fullname_picture = f'./uploads/images/{picture.filename}'

    if is_filename_allowed(picture.filename):
        picture.save(f'./uploads/images/{picture.filename}')
        post_text = request.form.get('content')
        add_post(f'./uploads/images/{picture.filename}', post_text)
        add_tegs(post_text)
        return render_template('post_uploaded.html', picture=fullname_picture, post_text=post_text)
    else:
        extension = picture.filename.split(".")[-1]
        logging.info(f'Файл "{picture.filename}" не картинка')
        return f"Тип файлов {extension} не поддерживается"

