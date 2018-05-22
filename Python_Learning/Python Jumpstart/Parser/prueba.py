# -*- coding: utf-8 -*-
"""Parseator 1.0."""
import json
import io
import datetime
import os
import sys
import logging


with io.open('coleccion.json', 'r', encoding='utf8') as coleccion:
    coleccion_item = json.load(coleccion)
    tst = coleccion_item['item'][0]['item'][0]['item'][3]['request']['description']
    print(tst)
