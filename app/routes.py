from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/edit', methods=['POST'])
def edit():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = f"./uploads/{uploaded_file.filename}"
        uploaded_file.save(file_path)
        # Now you can modify the file at file_path
    return redirect('/')