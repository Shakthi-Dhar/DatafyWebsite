from flask import Flask, request, render_template, send_file
from Firebase_data import download_csv

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('Home.html')


@app.route('/get_data', methods=['POST'])
def download():
    file = request.form.get('Sector')
    ext = request.form.get('ext')
    if file is None:
        file = "All"
    if ext is None:
        ext = "csv"
    download_csv(file, ext)
    return send_file('Data\Datafy' + file + '.'+ext,
                     mimetype='text/'+ext,
                     attachment_filename='Datafy' + file + '.' + ext,
                     as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
