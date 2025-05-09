from math import pi

def area_ret(ladoA, ladoB):

    area = ladoA * ladoB

    return area

def area_circ(diam):

    area = (pi * diam**2 ) / 4

    return area

def area_triang(base, altura):
    area = base * altura / 2    

    return area

def perimetro_triang(lado1, lado2, lado3):
    perimetro = lado1+lado2+lado3    

    return perimetro