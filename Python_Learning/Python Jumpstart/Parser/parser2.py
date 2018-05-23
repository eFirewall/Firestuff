# -*- coding: utf-8 -*-

"""Parseator 2.0."""
import json
import io
import datetime
import os
import sys

print('---------------------------------------')
print('|            PARSEATOR 2.0            |')
print('---------------------------------------')
print('')
print('Comprobaciones iniciales:')
print('')

filename = 'lastrun.json'

if os.path.exists(filename):
    with io.open('lastrun.json', 'r', encoding='utf8') as lastrun:
        lastrun_item = json.load(lastrun)
    print('El fichero "lastrun.json" existe. Podemos continuar...')
    counter = len(lastrun_item["results"])

else:
    sys.exit('No se encuentra el fichero "lastrun.json". Fin.')


def main():
    """Orquestra todo el script."""
    test_plan = lastrun_item['name']
    fecha = datetime.datetime.now()
    hoy = fecha.date().strftime("%d-%m-%Y")

    sys.stdout = open("salida.mu", "a")

    mostrar_encabezado_reporte(test_plan, fecha, hoy)

    """LOOP"""
    for i in range(counter):

        caso_prueba = lastrun_item['results'][i]['name']
        url = lastrun_item['results'][i]['url']
        r_message = lastrun_item['results'][i]['responseCode']['name']
        r_code = lastrun_item['results'][i]['responseCode']['code']
        resp = ('El r_code de respuesta es: *{} {}*'.format(r_code, r_message))

        mostrar_caso_de_prueba(i, caso_prueba)
        mostrar_url_peticion(i, url)
        mostrar_resultado_esperado()  # TODO Hacer que haga algo
        mostrar_resultado_obtenido(i, r_message, r_code, resp)
        mostrar_valoracion()  # TODO Algo habra que hacer con esto
        mostrar_evidencias()  # TODO Realmente no hace nada aun...
    sys.stdout.close()


def mostrar_caso_de_prueba(i, caso_prueba):
    print('------------------------------------')
    print('')
    print('')
    print('*caso_prueba de Prueba:*')
    print(caso_prueba).encode('utf-8')
    print('')


def mostrar_url_peticion(i, url):
    print('*Peticion:*')
    print(url).encode('utf-8')
    print('')


def mostrar_resultado_esperado():
    print('*Resultado esperado:*')
    print('')
    print('')


def mostrar_resultado_obtenido(i, r_message, r_code, resp):
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


def mostrar_encabezado_reporte(test_plan, fecha, hoy):
    print('------------------------------------')
    print('')
    print('*Test test_plan:*')
    print('*{}*'.format(test_plan))
    print('')
    print('Numero de casos: *{}*'.format(counter))
    print('')
    print('Fecha de reporte: *{}*'.format(hoy))
    print('')
    print('------------------------------------')


if __name__ == '__main__':
    main()
