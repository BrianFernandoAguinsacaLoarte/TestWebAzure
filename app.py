from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/saludo', methods=['POST'])
def saludo():
    nombre = request.form.get('nombre')
    return render_template('saludo.html', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)
