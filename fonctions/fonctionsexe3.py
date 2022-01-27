def tuple(val):
    if val < 0 :
        signe = "Négatif"
    else:
        signe ="Positif"
    typeval = type(val)
    valabsol = abs(val)
    tupl = (signe, typeval, valabsol)
    return tupl

print(tuple(56))