from flask import render_template,request,redirect,url_for
from . import main
from .. import photos


@main.route('/', methods=['POST'])
def index():
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user._pic_path = path
    return render_template('index.html')
