DROP TABLE IF EXISTS pracownicy;
DROP TABLE IF EXISTS stanowiska;
DROP TABLE IF EXISTS kontakty;
DROP TABLE IF EXISTS place;

CREATE TABLE pracownicy(
id  INTEGER PRIMARY KEY AUTOINCREMENT,
imie TEXT(15),
nazwisko TEXT(20),
kod STRING(10),
miasto_z TEXT(40),
ulica TEXT,
data_u DATE,
miasto_u TEXT(40)
);

CREATE TABLE stanowiska(
id  INTEGER PRIMARY KEY AUTOINCREMENT,
stanowisko TEXT(20)
);

CREATE TABLE kontakty(
id_p INTEGER,
typ_k BOOLEAN,
kontakt STRING(15),
uwagi TEXT(30),
FOREIGN KEY (id_p) REFERENCES pracownicy(id)
);


CREATE TABLE place(
id_p INTEGER,
id_s INTEGER,
placa INTEGER,
data_z DATE,
FOREIGN KEY (id_p) REFERENCES pracownicy(id),
FOREIGN KEY (id_s) REFERENCES stanowiska(id)
);
