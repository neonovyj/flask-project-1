from flask import Flask, render_template, request

from pswrdgen import pswrd

app = Flask(__name__)
topswrd = []


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":

        text = request.form['text']
        if type(text) != int:
            text = int(text)
        if text > 25:
            text = 24
        topswrd.append(text)
        topswrd.append(bool(request.form.get('uppercase')))
        topswrd.append(bool(request.form.get('digit')))
        topswrd.append(bool(request.form.get('special')))
        password = pswrd(topswrd)
        topswrd.clear()

        return render_template('index.html', password=password)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
