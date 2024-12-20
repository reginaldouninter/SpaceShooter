import math

def colisao(obj1_x, obj1_y, obj2_x, obj2_y):
    distancia = math.sqrt(math.pow(obj1_x - obj2_x, 2) + math.pow(obj1_y - obj2_y, 2))
    return distancia < 27