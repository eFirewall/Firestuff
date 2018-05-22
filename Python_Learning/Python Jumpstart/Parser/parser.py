"""Parseator 1.0."""
import json
import io
import datetime
import os
import sys


def main():
    """Orquestra todo el script."""
    mostrar_encabezado_aplicacion()
    comprueba_existencia_fichero()
    mostrar_encabezado_reporte()
    mostrar_reporte()
    # TODO guardar a un fichero externo nuevo


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
        print('El fichero "lastrun.json" NO existe')
        print('')
        print('No es posible continuar... OH POR DIOS!:')
        print('')
        sys.exit('ERROR CRITICO: NADA ES COMO DEBE!!!')


def mostrar_encabezado_reporte():
    """Imprime, al principio del fichero, el nombre del test plan."""
    with io.open('lastrun.json', 'r', encoding='utf8') as data_file:
        data_item = json.load(data_file)

        plan = data_item['name']
        fecha = datetime.datetime.now()
        hoy = fecha.date().strftime("%d-%m-%Y")
        counter = len(data_item["results"])

    print('------------------------------------')
    print('')
    print('*Test plan: *')
    print('*{}*'.format(plan))
    print('')
    print('Numero de casos: *{}*'.format(counter))
    print('')
    print('Fecha de reporte: *{}*'.format(hoy))
    print('')
    print('------------------------------------')


def mostrar_reporte():
    """Hace un loop y va metiendo cosas en el reporte."""

    with io.open('lastrun.json', 'r', encoding='utf8') as data_file:
        data_item = json.load(data_file)

    counter = len(data_item["results"])

    for i in range(counter):

        passfail = (data_item['results'][i]['tests']['status']).upper()
        codigo = data_item['results'][i]['responseCode']['code']
        mensaje = data_item['results'][i]['responseCode']['name']
        caso = data_item['results'][i]['name']
        url = data_item['results'][i]['url']
        resp = ('El codigo de respuesta es: *{} {}*'.format(codigo, mensaje))

        print('------------------------------------')
        print('')
        print('')
        print('*Caso de Prueba:*')
        print(caso)
        print('')
        print('*Peticion:*')
        print(url)
        print('')
        print('*Resultado esperado:*')
        print('')
        print('')
        print('*Resultado obtenido:*')
        print(resp)
        print('')
        print('')
        print('*Valoracion:*')
        print('*{}*'.format(passfail))
        print('')
        print('*Evidencia:*')
        print('{code}')
        print('')
        print('{code}')
        print('')
        print('------------------------------------')


if __name__ == '__main__':
    main()
