from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pagina1')
def pagina1():
    return render_template('pagina1.html')

@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')

@app.route('/pagina3')
def pagina3():
    return render_template('pagina3.html')

@app.route('/pagina4')
def pagina4():
    return render_template('pagina4.html')

@app.route('/pagina5')
def pagina5():
    return render_template('pagina5.html')

if __name__ == '__main__':
    app.run(debug=True)