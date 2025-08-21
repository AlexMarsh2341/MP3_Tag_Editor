from flask import *
from mutagen.easyid3 import EasyID3
import os
import tempfile

app = Flask(__name__)

# prompts user to upload file
@app.route('/')
def main():
    return render_template("index.html")

# runs when file is successfully uploaded
@app.route('/edit', methods=['POST'])
def edit():
    if request.method == 'POST':
        f = request.files['file']
        uploads_dir = os.path.join(app.root_path, 'uploads')
        os.makedirs(uploads_dir, exist_ok=True)
        file_path = os.path.join(uploads_dir, f.filename)
        f.save(file_path)
        return render_template("acknowledgement.html", file_path=file_path, name=f.filename)

# runs once new file metadata is uploaded
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        file_path = request.form.get('file_path')
        art = request.form.get('artist')
        al = request.form.get('album')
        ti = request.form.get('title')

        if not file_path or not os.path.exists(file_path):
            return "File not found", 400

        if not all([art, al, ti]):
            return "All metadata fields are required.", 400

        audio = EasyID3(file_path)
        audio["artist"] = art
        audio["album"] = al
        audio["title"] = ti
        audio.save()

        return render_template("final.html", file=audio, name=os.path.basename(file_path))

@app.route('/download/<filename>')
def download(filename):
    uploads_dir = os.path.join(app.root_path, 'uploads')
    return send_from_directory(uploads_dir, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)