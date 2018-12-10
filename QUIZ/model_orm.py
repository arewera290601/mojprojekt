#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  model_orm.py
import os
from peewee import *

baza_plik = 'quiz.db'
############## MODEL
baza = SqliteDatabase(baza_plik)
class BazaModel(Model):
    class Meta:
        database = baza


class Pytanie(BazaModel):
    pytanie = CharField(null=False, unique=true)


class Odpowiedz(BazaModel):
    pnr = ForeignKeyField(Pytanie, related_name= 'odpowiedź')
    odpowiedz = CharField(null = False)
    odpok = BooleanField(default=False)

