from . import app
from flask import render_template


@app.route('/manage')
def manage():
    return render_template('manage.html')
