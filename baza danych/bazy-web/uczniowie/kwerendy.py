#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
#
#   fetch- pobierz  
#   row- wiersz
# % - dowolny ciąg znaków dowolnej długości
# DESC- uporządkowanie malejąco
# ASC- uporządkowan rosąco
# AVG- srednia zmiennoprzecinkowa
# MAX - zwraca pierwszy maksymalny wynik - min najmniejszy
# typy relacji tabel: 
# 1. 1 do wielu 
# 2.jeden do jednego 
# 3. wiele do wielu

import sqlite3


def kwerenda(cur):
    cur.execute("""
    WITH srednie AS (
        SELECT imie, nazwisko, AVG(ocena) AS sred FROM uczniowie 
        INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
        GROUP BY uczniowie.id
      ) SELECT nazwisko, imie, sred FROM srednie
      WHERE sred > 3.5  ORDER BY sred DESC
    """)
#  SELECT id FROM uczniowie WHERE imie = 'Anna' AND nazwisko = 'Ignaczuk' 
#  SELECT * FROM uczniowie WHERE nazwisko LIKE 'A%' (lub '%a')
#  SELECT COUNT(id) FROM uczniowie WHERE imie LIKE '%a' 
#  SELECT COUNT(id) FROM uczniowie WHERE plec=1
#  SELECT imie, nazwisko, egz_mat FROM uczniowie WHERE egz_mat > 40 ORDER BY egz_mat ASC/ DESC LIMIT 5 
#  SELECT MAX(egz_mat), MIN(egz_hum), AVG(egz_jez) FROM uczniowie 
#  SELECT imie, nazwisko, klasa FROM uczniowie INNER JOIN klasy ON uczniowie.id_klasa=klasy.id WHERE klasa='2A' AND rok_naboru=2012
#  SELECT imie, nazwisko, klasa FROM uczniowie INNER JOIN klasy ON uczniowie.id_klasa=klasy.id WHERE klasy.id=(SELECT klasy.id FROM klasy WHERE klasa='1A' AND rok_naboru=2012)
#  SELECT klasa, AVG(egz_mat), AVG(egz_hum), AVG(egz_jez) FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa GROUP BY klasa
#   SELECT klasa, AVG(egz_mat) AS srm, AVG(egz_hum) AS srh, AVG(egz_jez) AS srj FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa  GROUP BY klasa ORDER BY srm DESC 
#  WITH srednie AS (SELECT imie, nazwisko, AVG(ocena) AS sred FROM uczniowie INNER JOIN oceny ON uczniowie.id=oceny.id_uczen GROUP BY uczniowie.id) SELECT nazwisko, imie, sred FROM srednie WHERE sred > 3.5  ORDER BY sred DESC

    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)
    
    
    
def main(args):
    # KONFIGURACJA #######
    baza_nazwa = 'baza'
    tabele = ['uczniowie','klasy','przedmioty','oceny']
    
    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora
    
    
    kwerenda(cur)
    
    con.commit()
    con.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
