#PGCD

a = int(input('entre un nombre  '))
b = int(input("entre un nombre  "))

if(a<b):
    a,b = b,a
while ( a%b != 0):
    r = a % b
    a,b = b,r
print(b)



     
    
