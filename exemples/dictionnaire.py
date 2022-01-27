resistance={'noir' :0, 'marron':1, 'rouge':2, 'orange':3, 'jaune':4, 'vert':5, 'bleu':6, 'violet':7, 'gris':8, 'blanc':9, 'or':0.01}

a=input('couleur 1er anneau? ')
b=input('couleur 2eme anneau? ')
c=input('couleur 3eme anneau? ')

print("La resistance vaut", (int(resistance.get(a))*10+int(resistance[b]))*10**int(resistance[c]),'Ohm')

resistance['argent']=0.1

print("\nNombre d'entrees :", len(resistance))

#supprimer une entree
del resistance['argent']

if "or" in resistance.keys():
    print("or :", resistance.get('or'))

print("\nResistance :")
for cle, valeur in resistance.items():
    print(cle, valeur)