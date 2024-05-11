from random import randint

HEX = '0123456789abcdef'


def hex_string(length):
    string = ''
    for i in range(length):
        string += HEX[randint(0, 15)]
    return string


uuid = f'''
    {hex_string(8)}-{hex_string(4)}-{hex_string(4)}-{hex_string(4)}-{hex_string(12)}
    '''

print(uuid)
