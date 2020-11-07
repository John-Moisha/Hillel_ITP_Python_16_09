# Задание 1. Треугольники.
#
# 1) Написать функцию create_randome_triangle() -> tuple, которая создает треугольник на плоскости со случайными
# координатами float (в диапазоне от -100.0 до 100.0 для каждой оси).
# функция дложна проверять, чтобы три точки не лежали на одной прямой.
# 3) Написать функцию create_right_triangle(vert:tuple) -> tuple, которая принимает координаты одной вершины и создает
# прямоугольный треугольник, площадь которого равна 100, с равными катетами параллельными осям координат.
# 2) написать функцию, которая считает площадь треугольника по координатем трех вершин.
#
import random

#1
def random_dot():
    return random.uniform(-100, 100)

def creat_triangle():
    _A = (random_dot(), random_dot())
    _B = (random_dot(), random_dot())
    _C = (random_dot(), random_dot())
    if abs(((_A[1] - _B[1]) / (_A[0] - _B[0])) - ((_A[1] - _C[1]) / (_A[0] - _C[0]))) < 0.001:
        # (((y1-y2) / (x1 - x2)) - ((y1 - y3) / (x1 - x3)))
        if _A[0] <= 97:
            _A[0] += 2
            print('Х точки A изменен: +2')
        else:
            _A[0] -= 2
            print('Х точки A изменен: -2')
        return(_A, _B, _C)
    return (_A, _B, _C)

print("▵ ABC",creat_triangle())

#2
def create_right_triangle(_t, S=100) -> tuple:
    _Ax = _t[0]
    _Ay = _t[1]
    _Bx = _Ax
    _By = ((2 * S) ** 0.5) + _Ay
    _Cx = _By
    _Cy = _Ay
    _A = (_Ax, _Ay)
    _B = (_Bx, _By)
    _C = (_Cx, _Cy)

    triangle = (_A, _B, _C)
    return triangle
_A = (1,1)
print("◺ ABC", create_right_triangle(_A))

#3
def S_triangle(_t):
    _A = _t[0]
    # print("A:",_A)
    _B = _t[1]
    # print("B:",_B)
    _C = _t[2]
    # print("C:",_C)
    # _S = ((_A[0] - _C[0]) * (_B[1] - _C[1]) - (_A[1] - _C[1]) * (_B[0] - _C[0])) / 2
    _Sa = abs((_A[0] - _C[0]) * (_B[1] - _C[1]) - (_A[1] - _C[1]) * (_B[0] - _C[0])) / 2

    # S▵ = ( (x1-x3)*(y2-y1) - (y1-y3)*(x2-x3) ) / 2
    return _Sa

print("S▲", S_triangle(creat_triangle()))