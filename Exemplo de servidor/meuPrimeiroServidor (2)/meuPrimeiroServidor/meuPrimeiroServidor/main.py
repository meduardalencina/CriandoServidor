import flask
import sqlite3


def main():
    app = flask.Flask(
        'meu servidor',
        template_folder='templates',
        static_folder='static'
    )

    @app.route('/', methods=['GET'])
    def main_page():
        return flask.render_template(
            'index.html',
            meu_novo_paragrafo='<p>Estas informações foram escritas pelo lado do servidor!</p>'
        )

    #para criar nova pag na web pra usar só colocar / e o nome da pagina

    @app.route('/albuns', methods=['GET'])
    def pagina_albuns():
        return flask.render_template(
            'albuns.html'
        )

    @app.route('/musicas_album', methods=['POST'])
    def musicas_album():
        album = flask.request.form.get('selecionado')
        print('o album selecionado foi {0}'.format(album))

        response = flask.jsonify({'musicas': 'nada ainda!'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    @app.errorhandler(404)
    def page_not_found(page):
        return flask.render_template('404.html'), 404

    app.register_error_handler(404, page_not_found)

    app.run(debug=True)


if __name__ == '__main__':
    main()
