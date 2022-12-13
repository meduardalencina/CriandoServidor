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
        print('o álbum selecionado foi {0}'.format(album))

        with sqlite3.connect('static\\database\\test.db') as con:
            cur = con.cursor()
            id_album = cur.execute('''SELECT id_album FROM albuns WHERE nome='{0}';'''.format(album)).fetchone()[0]

            musicas = cur.execute('''
                SELECT m.nome
                FROM musicas as m
                INNER JOIN musicas_para_albuns as mpa on m.id_musica = mpa.id_musica
                WHERE mpa.id_album = {0} 
            '''.format(id_album)).fetchall()

            lista_musicas = dict(musicas=[])
            for musica in musicas:
                lista_musicas['musicas'].append(musica[0])

            lista_musicas['musicas'] = ','.join(lista_musicas['musicas'])

        response = flask.jsonify(lista_musicas)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    @app.errorhandler(404)
    def page_not_found(page):
        return flask.render_template('404.html'), 404

    app.register_error_handler(404, page_not_found)

    app.run(debug=True)


if __name__ == '__main__':
    main()
