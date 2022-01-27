class Rectangle:
    def __init__(self,longueur=5,largeur=3):
        self.nom = "rectangle"
        self.longueur = longueur
        self.largeur = largeur
    def surface(self):
        return self.longueur*self.largeur
    def __str__(self):
        return ("{} de longueur {} et de largeur {}".format(self.nom,self.longueur,self.largeur))
        
class Carre(Rectangle):
    def __init__(self, cote=10):
        Rectangle.__init__(self, cote,cote)
        self.nom = "carre"


monRectangle = Rectangle(10,5)
print(monRectangle)
print(monRectangle.surface())

monCarre = Carre()
print(monCarre)

