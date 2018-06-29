from flask import Flask, render_template
from main.api.fileManagementApi import *
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/upload", methods=['POST'])
def upload(auth, file, option):
    res = upload_file(auth, file, option)
    return res


@app.route("/rename", methods=['POST'])
def rename(auth, new_name, old_name):
    res = rename_file(auth, new_name, old_name)
    return res


@app.route("/delete", method=['POST'])
def delete(auth, file):
    res = delete_file(auth, file)
    return res




