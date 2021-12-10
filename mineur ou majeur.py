age = int(input('entre votre age :  '))
if(age < 18):
    print("vous êtes mineur ! ")
elif(age >= 18 and age < 60):
    print("vous êtes majeur ! ")
else:
    print("vous êtes retraité")
    