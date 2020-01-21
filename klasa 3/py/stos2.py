#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Stos:
    def __init__(self):
        self.elementy = []

    def push(self, element):
        self.elementy.append(element)

    def pop(self):
        return self.elementy.pop()

stos = Stos()
stos.push(4)
stos.push(6)
stos.push('dog')
stos.push(True)
print(stos.pop())
print(stos.pop())
print(stos.pop())
print(stos.pop())
