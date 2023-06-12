import os
from flask import Blueprint, render_template, request, current_app, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from microblog.forms import FileUploadForm


files_bp = Blueprint('files', __name__)


@files_bp.route('/', methods=['GET','POST'])
@login_required
def index():

    title = "Dosyalar"
    form = FileUploadForm()
    if request.method == 'POST':
        uploaded_file = request.files['file_upload']
        if uploaded_file.filename:
            file_name = secure_filename(uploaded_file.filename)
            file_path = os.path.join(current_user.upload_dir, file_name) 
            uploaded_file.save(file_path)
            flash("Dosya {} kaydedildi".format(file_name))

    return render_template('files/index.html', title=title, form=form)
