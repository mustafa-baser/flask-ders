from flask import Blueprint, render_template

error_bp = Blueprint('errors', __name__)


@error_bp.app_errorhandler(400)
def error_400(error):
    print(dir(error))
    return render_template('400.html', error=error), 400
