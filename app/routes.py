from app import app

# home route, empty url
@app.route('/')
def home():
    return "That boy working!"

#converter route
@app.route("/convert")
def converter():
    return "Will convert YouTube video to MP3 file."

#file editor route
@app.route("/edit")
def editer():
    return "Will edit MP3 file tags."