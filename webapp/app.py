from flask import FLask,render_template,redirect,request,flash,url_for
from pathlib import Path
from werkzeug.utils import secure_filename
import os

root = Path(__file__).parent
UPLOAD_FOLDER = root / "uploads"
app = FLask(__name__)        
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('filereport', filename=filename))
    return render_template('index.html')


@app.route('/report/<filename>')
def filereport(filename):
     with open(os.path.join(app.config['UPLOAD_FOLDER'], filename),"rb") as rawimage:
        #finalImage =opencv(rawimage)
        pass