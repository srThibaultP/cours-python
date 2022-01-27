def table(base, debut, fin, inc):
    result = debut
    while result < fin :
        result = result + inc
        if result < fin :
            print(result)
    

base=int(input("table de multiplication?"))
debut=int(input("nombre de départ ?"))
inc=int(input("nombres de chiffres à ne pas afficher ?"))
fin=int(input("valeur de fin ?"))

table(base, debut, fin, inc)