#algo : nb Premier()

#Declaration:

#Debut :

#    afficher ("entrer un nombre :")
#    saisir nb
#    compteur <- 0 
#    pour i allant de (1, nb)faire
#        si (nb % i = o ) alors
#           compteur <- compteur + 1
#        fin si
##fin pour 
#si (compteur = 2) alors
#    afficher ("votre nombre ",nb," est premier.")
#fin si
#sinon 
#   afficher("votre nombre",nb,"n'est pas premier.")
#fin sinon

#fin algo nb premier 

 

nb = int(input('entrer un nombre :   ' ))

cpt = 0
liste1 = []
for i in range (1,nb+1):
    if(nb % i ==0):
        cpt = cpt + 1
        liste1.append(i)
if(cpt == 2):
    print("votre nombre",nb,"est premier")
else:
    print("votre nombre",nb,"n'est pas premier")
    print("voici les diviseur de ",nb," :",liste1, )

