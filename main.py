from typing import List
import math

Vector = List[float]
def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def scalat_miltiplication(v: Vector, c: float) -> Vector:
    return [i * c for i in v]

def dot(v: Vector, w: Vector) -> Vector:
    return sum([v_i * w_i for v_i, w_i in zip(v, w)])

def sum_of_squares(v: Vector) -> float:
    return dot(v,v)

def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))

def squared_distance(v: Vector, w: Vector) -> Vector:
    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
    return math.sqrt(squared_distance(v, w))



v1 = [1.1, 1.2, 1.3]
v2 = [1.134, 1.234, 1.32342]
print(*add(v1, v2), " Сумма векторов")
print(*subtract(v1, v2), "Разность векторов")
print(*scalat_miltiplication(v1, 4), "Произведения v1 на 4")