import json


def main():
    mostrar_header()
    mostrar_test_plan()
    read_file()
    # TODO Limitar el numero de iteraciones
    # TODO guardar a un fichero externo nuevo


def mostrar_header():
    print('---------------------------------------')
    print('              PARSER 1.0')
    print('---------------------------------------')
    print('')
    print('')
    print('')
    print('')


def mostrar_test_plan():
    with open('lastrun.json') as data_file:
        data_item = json.load(data_file)
        plan = data_item['name']
    print('------------------------------------')
    print('*Test plan: *')
    print('*{}*'.format(plan))
    print('------------------------------------')


def read_file():
    with open('lastrun.json') as data_file:
        data_item = json.load(data_file)
    counter = int(66)

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
