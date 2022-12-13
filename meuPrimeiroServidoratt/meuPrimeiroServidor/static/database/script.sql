PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS albuns (
    id_album INTEGER NOT NULL,
    nome TEXT NOT NULL,
    PRIMARY KEY(id_album)
);

CREATE TABLE IF NOT EXISTS musicas (
    id_musica INTEGER NOT NULL,
    nome TEXT NOT NULL,
    PRIMARY KEY(id_musica)

);

--> cria relação entre tabelas <--
CREATE TABLE IF NOT EXISTS musicas_para_albuns(
    id_album INTEGER NOT NULL,
    id_musica INTEGER NOT NULL,
    PRIMARY KEY(id_album, id_musica),
    FOREIGN KEY(id_album) REFERENCES albuns(id_album),
    FOREIGN KEY(id_musica) REFERENCES musicas(id_musica)

);

INSERT INTO albuns(id_album, nome) VALUES (1, 'fearless');
INSERT INTO albuns(id_album, nome) VALUES (2, 'red');
INSERT INTO musicas(id_musica, nome) VALUES (1, 'love story');
INSERT INTO musicas(id_musica, nome) VALUES (2, 'fearless');
INSERT INTO musicas(id_musica, nome) VALUES (3, 'state of grace');
INSERT INTO musicas(id_musica, nome) VALUES (4, 'red');
INSERT INTO musicas_para_albuns(id_album, id_musica) VALUES (1,1);
INSERT INTO musicas_para_albuns(id_album, id_musica) VALUES (1,2);
INSERT INTO musicas_para_albuns(id_album, id_musica) VALUES (2,3);
INSERT INTO musicas_para_albuns(id_album, id_musica) VALUES (2,4);

COMMIT;
