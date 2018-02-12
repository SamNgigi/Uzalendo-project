from flask import render_template,request,redirect,url_for
from . import main
from .. import photos


@main.route('/', methods=['POST'])
def index():
     if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f 'photos/{filename}'
        flash("Photo saved.")
        user._pic_path = path
        return redirect(url_for('show', id=rec.id))
    return render_template('index.html')
