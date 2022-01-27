from math import pi

def cube(val):
    val **= 3
    return val
    
def volumeSphere(r):
    return 4*pi*cube(r)/3
    
    
print("volume de la sphère = ",volumeSphere(42))