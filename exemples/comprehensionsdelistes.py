#liste en compréhension
#new_list = [function(item) for item in list if condition(item)]
a = [1,4,2,7,1,9,0,3,4,6,6,6,8,3]
print(a,'\nFiltre des valeurs supérier à 5')
#filtre pour garder le valeurs >5
b=[]
for i in a:
    if i>5:
        b.append(i)
print(b)
#par liste en compréhention
b=[i for i in a if i > 5]
print(b)

#Créer une liste des 15 premiers entiers pairs
c=[i for i in range(2,30,2)]
print('15 premiers entiers pairs : \n',c)