import os
from pathlib import Path
from flask import Blueprint, render_template, request, current_app, flash,\
    send_from_directory, redirect, url_for
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

    user_files_path = Path(current_user.upload_dir)

    return render_template('files/index.html', title=title, form=form, user_files_path=user_files_path)

@files_bp.route('/download/<filename>')
@login_required
def download(filename):
    if os.path.exists(os.path.join(current_user.upload_dir, filename)):
        return send_from_directory(current_user.upload_dir, filename)
    else:
        flash("Böyle bir dosya yok")
        return redirect(url_for('files.index'))

@files_bp.route('/delete/<filename>')
@login_required
def delete(filename):
    file_path = os.path.join(current_user.upload_dir, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        flash("Böyle bir dosya yok")
    return redirect(url_for('files.index'))
