DROP TABLE IF EXISTS uczniowie;
DROP TABLE IF EXISTS przedmioty;
DROP TABLE IF EXISTS oceny;

CREATE TABLE uczniowie (
IDucznia INTEGER PRIMARY KEY,
nazwisko TEXT(20),
imie TEXT(15),
ulica TEXT(15),
dom INTEGER(3),
IDklasy TEXT(3)
);

CREATE TABLE przedmioty (
IDprzedmiotu INTEGER PRIMARY KEY,
NazwaPrzedmiotu TEXT(15),
Nazwisko_naucz TEXT(20),
Imie_naucz TEXT(15),
FOREIGN KEY (IDprzedmiotu) REFERENCES przedmioty(IDprzedmiotu)
);

CREATE TABLE oceny (
IDucznia INTEGER PRIMARY KEY,
Ocena INTEGER(3),
Data_ DATE(10),
IDprzedmiotu TEXT(1),
FOREIGN KEY (IDucznia) REFERENCES uczniowie(IDucznia),
FOREIGN KEY (IDprzedmiotu) REFERENCES przedmioty(IDprzedmiotu)
);
