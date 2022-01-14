nombre = int(input('entre un nombre  '))

res = ''
d = '1'

while d != 0 : 
    r = nombre%2
    d = nombre//2
    nombre = d
    res = (str(r))+ res
print('voici le résultat :', res)