#algo : nb parfait()



#Declaration:

#	nb,s,i : entier 

#Debut :



#saisir nb ("entre un nombre : ")



#som <- 0



#pour i allant de ( 1 , nb -1) faire

#    si(nb%i =0 ) alors

#        som = som + 1

#    fin si

#fin pour (som = nb ) alors

#    afficher (nb parfait)

#sinon

#    afficher (nb pas parfait )



#fin algo nb parfait


nb = int(input('entrer un nombre : ' ))

som = 0

for i in range (1, nb - 1 ):
    if(nb % i == 0 ):
        som = som + i
        
        
if(som == nb ):
    print("votre nombre",nb," est parfait ")
    
else:
    print("votre nombre",nb,"n'est pas parfait ")
    




