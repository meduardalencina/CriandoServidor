import flask

def main(): #para fazendo uma pagina e ser retornada ára o usuario
    app = flask.Flask(
        'meu primeiro servidor',
        template_folder='templates',
        static_folder='static' #onde estao todos os elementos estaticos,para deixar quieto, não mexer
    )

    @app.route('/', methods=['GET'])

    def main_page():  #qualquer nome,# chama a função
        return flask.render_template(
            'pagina_inicial.html', #retorna o template criado
            meu_paragrafo='<p>Bob Marley jogou com Chico Buarque e torcia pro Santos</p>'
                      )
    app.run(debug=True)

if __name__ == '__main__':
    main()