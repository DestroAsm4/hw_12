from flask import Flask, request, render_template, send_from_directory
from main.main import main
from loader.loader import loader
import os

picfolder = os.path.join('uploads','images')


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = picfolder


# открытие папки upload для внешнего доступа
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


# регистрации блюпринтов
app.register_blueprint(main)
app.register_blueprint(loader)
app.run()

