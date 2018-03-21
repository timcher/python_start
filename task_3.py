import math
a_x=int(input("Введите координату X вершины A треугольника ABC: "))
a_y=int(input("Введите координату Y вершины A треугольника ABC: "))
b_x=int(input("Введите координату X вершины B треугольника ABC: "))
b_y=int(input("Введите координату Y вершины B треугольника ABC: "))
while b_x==a_x and b_y==a_y: 
    if b_y==a_y and b_x==a_x:
        b_x=int(input("Введите координату X вершины B треугольника ABC: "))
        b_y=int(input("Введите координату X вершины B треугольника ABC: "))
c_x=int(input("Введите координату X вершины C треугольника ABC: "))
c_y=int(input("Введите координату Y вершины C треугольника ABC: "))
while b_x==c_x or a_x==c_x and b_y==c_y or a_y==c_y:
    if b_x==c_x and b_y==c_y:
        c_x=int(input("Введите координату X вершины C треугольника ABC: "))
        c_y=int(input("Введите координату Y вершины C треугольника ABC: "))
    elif a_x==c_x and a_y==c_y:
        c_x=int(input("Введите координату X вершины C треугольника ABC: "))
        c_y=int(input("Введите координату Y вершины C треугольника ABC: "))
if b_x-a_x != 0 and b_y-a_y != 0:
    ab=(b_x-a_x)**2+(b_y-a_y)**2
if c_x-b_x != 0 and c_y-b_y != 0:
    bc=(c_x-b_x)**2+(c_y-b_y)**2
if c_x-a_x != 0 and c_y-a_y != 0:
    ac=(c_x-a_x)**2+(c_y-a_y)**2
l_ab=math.sqrt(ab)
l_bc=math.sqrt(bc)
l_ac=math.sqrt(ac)
if l_ab**2+l_bc**2==l_ac**2:
    print("Треугольник прямоугольный!")
elif l_ac**2+l_bc**2==l_ab**2:
    print("Треугольник прямоугольный!")
elif l_ac**2+l_ab**2==l_bc**2:
    print("Треугольник прямоугольный!")
else:
    print("Треугольник не прямоугольный")
    

        
