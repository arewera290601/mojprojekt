#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.csv
#  
import sqlite3


def kwerenda(cur):
    cur.execute("""
        WITH srednia AS (
            SELECT nazwisko, imie, AVG(ocena) AS sred  FROM uczniowie
            INNER JOIN oceny ON uczniowie.id = oceny.id_uczen
            GROUP BY uczniowie.id
        ) SELECT nazwisko, imie, sred FROM srednie 
        WHERE sred > 3.5 ORDER BY sred DESC
    
    """)
    
    #   SELECT id FROM uczniowie WHERE imie = "Anna" AND nazwisko = "Ignaczuk"
    #   SELECT COUNT(id) FROM uczniowie WHERE imie LIKE "%a"
    #   SELECT * FROM uczniowie WHERE imie LIKE "%a"
    #   SELECT COUNT(id) FROM uczniowie WHERE plec = 1
    #   SELECT imie, nazwisko, egz_mat FROM uczniowie WHERE egz_mat > 40 ORDER BY egz_mat ASC LIMIT 5
    #   SELECT MAX(egz_mat), Min(egz_mat) FROM uczniowie
    #   SELECT AVG(egz_mat), AVG(egz_hum) FROM uczniowie
    #   SELECT imie, nazwisko, klasa FROM uczniowie INNER JOIN klasy ON uczniowie.id_klasa = klasy.id WHERE klasa = '1A' AND rok_naboru = '2012'  
    #   SELECT klasa, AVG(egz_mat) FROM klasy INNER JOIN uczniowie ON klasy.id = uczniowie.id_klasa GROUP BY klasa ORDER BY srm DESC
    
    #  % - dowolny ciag znakow dowolnej dlugosci
    # DESC - uporzadkowanie malejaco
    # ASC - rosnaco
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)

def main(args):
    # KONFIGURACJA 
    #######
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
