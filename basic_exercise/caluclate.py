#Oh boy, this is a complicated set of instructions. Bear with me. Write a function called
#calculate that accepts a list of keyword arguments

#- make_float , a boolean which returns a float if True or an integer if False,
#- operation which is either 'add', 'subtract', 'multiply', and 'divide!.
#- first which is a number, second ,which is another number, and message which is
#a string that can be added.

#The function should return the result of actually running the specified operation with the first
#and second keyword arguments. The result of the operation with the first and
#second is an integer if the make _float keyword argument is False , otherwise the
#result of the operation is a float. If a message is specified, it should return the message
#keyword argument + the result of the operation. Otherwise, it should return the string "The
#recult is " ininer with the result nf the gneratinn

def calculate(**kwargs):
    resul = {'add': kwargs['first'] + kwargs['second'],
            'subtract': kwargs['first'] - kwargs['second'],
            'multiply': kwargs['first'] * kwargs['second'],
            'divide': kwargs['first'] / kwargs['second']
    }
    if kwargs['make_float']:
        resul_par =  float(resul[kwargs['operation']])
    else:
        resul_par = int(resul[kwargs['operation']])
    return "{} {}".format(kwargs.get('message','The result is'), resul_par)
    

print(calculate(make_float=True, operation='divide', first=3.5, second=5))