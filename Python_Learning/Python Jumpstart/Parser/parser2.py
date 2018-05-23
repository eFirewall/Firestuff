# -*- coding: utf-8 -*-

"""Parseator 2.0."""
import json
import io
import datetime
import os
import sys
import logging

with io.open('lastrun.json', 'r', encoding='utf8') as lastrun:
    lastrun_item = json.load(lastrun)
    counter = len(lastrun_item["results"])


def main():
    """Orquestra todo el script."""
    Abre_el_fichero()
    mostrar_encabezado_aplicacion()
    sys.stdout = open("salida.mu", "a")
    mostrar_encabezado_reporte()
    """LOOP"""
    for i in range(counter):
        caso = lastrun_item['results'][i]['name']
        url = lastrun_item['results'][i]['url']
        mensaje = lastrun_item['results'][i]['responseCode']['name']
        codigo = lastrun_item['results'][i]['responseCode']['code']
        resp = ('El codigo de respuesta es: *{} {}*'.format(codigo, mensaje))
        mostrar_caso_de_prueba(i, caso)
        mostrar_url_peticion(i, url)
        mostrar_resultado_esperado()  # TODO Hacer que haga algo
        mostrar_resultado_obtenido(i, mensaje, codigo, resp)
        mostrar_valoracion()  # TODO Algo habra que hacer con esto
        mostrar_evidencias()  # TODO Realmente no hace nada aun...
    sys.stdout.close()


def mostrar_caso_de_prueba(i, caso):  # FIXME llamar a i desde el loop global
    print('------------------------------------')
    print('')
    print('')
    print('*Caso de Prueba:*')
    print(caso).encode('utf-8')
    print('')


def mostrar_url_peticion(i, url):
    print('*Peticion:*')
    print(url).encode('utf-8')
    print('')


def mostrar_resultado_esperado():
    print('*Resultado esperado:*')
    print('')
    print('')


def mostrar_resultado_obtenido(i, mensaje, codigo, resp):
    print('*Resultado obtenido:*')
    print(resp).encode('utf-8')
    print('')
    print('')


def mostrar_valoracion():
    print('*Valoracion:*')
    print('')
    print('')


def mostrar_evidencias():
    print('*Evidencia:*')
    print('{code}')
    print('')
    print('{code}')
    print('')
    print('------------------------------------')


def mostrar_encabezado_aplicacion():
    """Imprime el header."""
    print('---------------------------------------')
    print('           PARSEATOR 2.0')
    print('---------------------------------------')
    print('')


def Abre_el_fichero():
    with io.open('lastrun.json', 'r', encoding='utf8') as lastrun:
        lastrun_item = json.load(lastrun)

    print('Comprobaciones iniciales:')
    print('')
    filename = 'lastrun.json'
    if os.path.exists(filename):
        print('El fichero "lastrun.json" existe.')
        print('')
        print('Podemos continuar...')
        print('')
    else:
        print('')
        print('El fichero "lastrun.json" NO existe')
        print('')
        print('No es posible continuar... OH POR DIOS!:')
        print('')
        sys.exit('ERROR CRITICO: NADA ES COMO DEBE!!!')


def mostrar_encabezado_reporte():
    plan = lastrun_item['name']
    fecha = datetime.datetime.now()
    hoy = fecha.date().strftime("%d-%m-%Y")

    # sys.stdout = open("salida.mu", "a")
    print('------------------------------------')
    print('')
    print('*Test plan:*')
    print('*{}*'.format(plan))
    print('')
    print('Numero de casos: *{}*'.format(counter))
    print('')
    print('Fecha de reporte: *{}*'.format(hoy))
    print('')
    print('------------------------------------')
    # sys.stdout.close()


if __name__ == '__main__':
    main()
