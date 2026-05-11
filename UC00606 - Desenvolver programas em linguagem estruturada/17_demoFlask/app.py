
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template("pagina1.html", cod=11)


@app.route('/pag2')
def pag2():
    return render_template("pagina1.html", cod=21)

if __name__ == '__main__':
    app.run()
