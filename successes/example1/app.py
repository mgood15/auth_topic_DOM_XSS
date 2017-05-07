from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('start.html')
    #return redirect(url_for('newRedirect'))

@app.route('/newRedirect', methods=['POST'])
def newRedirect():
    ret = request.form['entry']
    retLink = request.form['injection']
    if retLink:
        return redirect(url_for('new_url', name=retLink))
    else:
        return render_template('start.html')

@app.route("/newRedirect#<path:name>")
def new_url(name):
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
