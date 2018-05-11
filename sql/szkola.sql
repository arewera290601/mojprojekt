DROP TABLE IF EXISTS tbUczniowie;
DROP TABLE IF EXISTS tbKlasa;

CREATE TABLE tbUczniowie
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	imie TEXT,
	nazwisko TEXT,
	plec INTEGER,
	id_klasa INTEGER,
	egzHum NUMERIC NOT NULL DEFAULT 0,
	egzMat NUMERIC NOT NULL DEFAULT 0,
	egzJez NUMERIC NOT NULL DEFAULT 0,
	FOREIGN KEY (id_klasa) REFERENCES tbKlasa(id)
);

CREATE TABLE tbKlasa
(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		klasa TEXT,
		rokNaboru INTEGER,
		rokMatury INTEGER
);

INSERT INTO tbklasa(id, klasa, rokNaboru, rokMatury) VALUES (NULL, '1A', 2017, 2020);
INSERT INTO tbklasa VALUES (NULL, '2A', 2016, 2019);
INSERT INTO tbklasa VALUES (NULL, '1C', 2017, 2020);
INSERT INTO tbUczniowie(id, imie, nazwisko, plec, id_klasa, egzHum, egzMat, egzJez)
VALUES(NULL, 'Adam', 'Słodki', 0, 3, 70.5, 80.4, 98.4);
INSERT INTO tbUczniowie VALUES (NULL, 'Aleksandra', 'Rewera', 1, 1, 83, 75, 70);

UPDATE tbUczniowie SET egzJez = 100 WHERE id = 1;