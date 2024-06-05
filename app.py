from flask import Flask, request, render_template
from pyswip import Prolog

app = Flask(__name__)
prolog = Prolog()

prolog.consult("filmes.pl")

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        genero = request.form.get('genero', '')
        diretor = request.form.get('diretor', '')
        ator = request.form.get('ator', '')

        query = "recomendar_filme('{0}', '{1}', '{2}', Filme)".format(genero, diretor, ator)

        try:
            filmes = list(prolog.query(query))
            if filmes:
                resultado = filmes[0]['Filme']
            else:
                resultado = 'Nenhum filme encontrado.'
        except Exception as e:
            resultado = f"Erro na consulta Prolog: {e}"

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
