from flask import *
from mutagen.easyid3 import EasyID3

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
        f.save(f.filename)
        return render_template("acknowledgement.html", file = f, name = f.filename)

# runs once new file metadata is uploaded
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        audio = EasyID3(f)

        #edit tags
        audio["artist"] = 'artist'
        audio["album"] = 'album'
        audio["title"] = 'title'

        audio.save()
        return render_template("final.html", file=audio)

if __name__ == '__main__':
    app.run(debug=True)