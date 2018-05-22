# -*- coding: utf-8 -*-
"""Parseator 1.0."""
import json
import io
import datetime
import os
import sys
import logging


def main():
    """Orquestra todo el script."""

    mostrar_encabezado_aplicacion()
    comprueba_existencia_fichero()
    mostrar_encabezado_reporte()
    mostrar_reporte()
    # TODO Hacer que escriba correctamente el resultado de la Prueba
    # TODO Importr el resultado esperado


def mostrar_encabezado_aplicacion():
    """Imprime el header."""
    print('---------------------------------------')
    print('           PARSEATOR 1.0')
    print('---------------------------------------')
    print('')


def comprueba_existencia_fichero():
    print('Comprobaciones iniciales:')
    print('')
    filename = ('lastrun.json')

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
    """Imprime, al principio del fichero, el nombre del test plan."""
    with io.open('lastrun.json', 'r', encoding='utf8') as data_file:
        lastrun_item = json.load(data_file)

        plan = lastrun_item['name']
        fecha = datetime.datetime.now()
        hoy = fecha.date().strftime("%d-%m-%Y")
        counter = len(lastrun_item["results"])

    sys.stdout = open("salida.mu", "a")
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
    sys.stdout.close()


def mostrar_reporte():
    """Hace un loop y va metiendo cosas en el reporte."""

    with io.open('lastrun.json', 'r', encoding='utf8') as lastrun:
        lastrun_item = json.load(lastrun)
    counter = len(lastrun_item["results"])

    for i in range(counter):

        passfail = (lastrun_item['results'][i]['tests']['status']).upper()
        codigo = lastrun_item['results'][i]['responseCode']['code']
        mensaje = lastrun_item['results'][i]['responseCode']['name']
        caso = lastrun_item['results'][i]['name']
        url = lastrun_item['results'][i]['url']
        resp = ('El codigo de respuesta es: *{} {}*'.format(codigo, mensaje))
        sys.stdout = open("salida.mu", "a")
        print('------------------------------------')
        print('')
        print('')
        print('*Caso de Prueba:*')
        print(caso).encode('utf-8')
        print('')
        print('*Peticion:*')
        print(url).encode('utf-8')
        print('')
        print('*Resultado esperado:*')
        print('')
        print('')
        print('*Resultado obtenido:*')
        print(resp).encode('utf-8')
        print('')
        print('')
        print('*Valoracion:*')
        print('*{}*'.format(passfail)).encode('utf-8')
        print('')
        print('*Evidencia:*')
        print('{code}')
        print('')
        print('{code}')
        print('')
        print('------------------------------------')
        sys.stdout.close()


if __name__ == '__main__':
    main()
