import json

def main():
    mostrar_header()
    mostrar_test_plan()
    read_file()
    # TODO Limitar el numero de iteraciones
    # TODO guardar a un fichero externo nuevo


def mostrar_header():
    print('---------------------------------------')
    print('             PARSER 1.0')
    print('---------------------------------------')
    print('')


def mostrar_test_plan():
    with open('lastrun.json') as data_file:
        data_item = json.load(data_file)
    print('------------------------------------')
    print('')
    print('')
    print('*Test plan: *')
    plan = data_item['name']
    print('*'+plan+'*')
    print('')
    print('------------------------------------')


def read_file():
    with open('lastrun.json') as data_file:
        data_item = json.load(data_file)
    counter = int(66)
    results = ['results']
    number = [0]
    name = ['name']

    for i in range(0, counter + 1):
        codigo = data_item['results'][i]['responseCode']['code']
        mensaje = data_item['results'][i]['responseCode']['name']
        print('------------------------------------')
        print('')
        print('')
        print('*Caso de Prueba:*')
        print(data_item['results'][i]['name'])
        print('')
        print('*Peticion:*')
        print(data_item['results'][i]['url'])
        print('')
        print('Resultado esperado:')
        print('')
        print('')
        print('Resultado obtenido:')
        print('El codigo de respuesta es: {} {}'.format(codigo, mensaje))
        print('')
        print('')
        print('*Valoracion:*')
        passfail = (data_item['results'][i]['tests']['status']).upper()
        print('*' + passfail + '*')
        print('')
        print('*Evidencia:*')
        print('{code}')
        print('')
        print('{code}')
        print('')
        print('------------------------------------')


if __name__ == '__main__':
    main()
