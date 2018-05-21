"""Parseator 1.0."""

import json
import io
import datetime


def main():
    """Orquestra todo el script."""
    mostrar_header()
    mostrar_test_plan()
    looper()
    # TODO Limitar el numero de iteraciones
    # TODO guardar a un fichero externo nuevo
    # TODO Control de ficheros. Si el fichero no existe que arroje error p.ej.


def mostrar_header():
    """Imprime el header."""
    print('---------------------------------------')
    print('           PARSEATOR 1.0')
    print('---------------------------------------')
    print('')
    print('')
    print('')
    print('')


def mostrar_test_plan():
    """Imprime, al principio del fichero, el nombre del test plan."""
    with io.open('lastrun.json', 'r', encoding='utf8') as data_file:
        data_item = json.load(data_file)
        plan = data_item['name']
        fecha = datetime.datetime.now()
        hoy = fecha.date().strftime("%d-%m-%Y")
    print('------------------------------------')
    print('')
    print('Fecha de reporte: *{}*'.format(hoy))
    print('')
    print('*Test plan: *')
    print('*{}*'.format(plan))
    print('------------------------------------')
    print('')
    print('')


def looper():
    """Hace un loop y va metiendo cosas en el reporte."""
    with io.open('lastrun.json', 'r', encoding='utf8') as data_file:
        data_item = json.load(data_file)
    counter = int(66)
    """El loop en cuestion."""
    for i in range(0, counter + 1):
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
