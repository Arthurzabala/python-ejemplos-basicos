

def fizzbuzz (limit):
    for i in range(limit):
        print('Analizando el numero ' + str(i))
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


respuesta= input ("¿HOLA, hasta que numero desea iterar?")
respuesta = int(respuesta)
fizzbuzz(respuesta)


