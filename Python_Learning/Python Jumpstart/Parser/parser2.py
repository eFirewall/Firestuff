# -*- coding: utf-8 -*-
# TODO

"""Parseator 1.0."""
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
    mostrar_encabezado_aplicacion()
    comprueba_existencia_fichero()
    mostrar_encabezado_reporte()
    for i in range(counter):
        mostrar_caso_de_prueba()
    #     TODO mostrar_url_peticion()
    #     TODO mostrar_resultado_esperado()
    #     TODO mostrar_resultado_obtendo()
    #     TODO mostrar_valoracion()
    #     TODO mostrar_evidencias()


def mostrar_caso_de_prueba():  # FIXME llamar a i desde el loop global
        caso = lastrun_item['results'][i]['name']
        print('------------------------------------')
        print('')
        print('')
        print('*Caso de Prueba:*')
        print(caso).encode('utf-8')
        print('')


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
