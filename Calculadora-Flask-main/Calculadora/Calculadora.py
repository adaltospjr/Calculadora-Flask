from flask import Flask, render_template, request
from os import abort

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('calc.html')

@app.route('/calculaform', methods=['POST', 'GET'])
def calculaform():
    valor1 = request.form['valor1']
    valor2=request.form['valor2']
    operacao=request.form['operacao']

    print(operacao)

    try:
        v1 = int(valor1)
        
    except ValueError:

        abort(404)

    try:
        v2 = int(valor2)

    except ValueError:

        abort(404)

    if operacao == 'soma' or operacao == '+':
        resultado = v1 + v2
    elif operacao == 'multiplicacao' or operacao == '*' or operacao == 'x':
        resultado = v1 * v2
    elif operacao == 'subtracao' or operacao == '-':
        resultado = v1 - v2
    elif operacao == 'divisao' or operacao == '/':
        if v2 == 0:
            abort(422)
        else:
            resultado = v1 / v2
    else:
        abort(404)

    return str(resultado)

app.run(debug=True)
