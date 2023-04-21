def Stepen (x,y):
    if y == 0:
        return 1
    else:
        return Stepen(x,y-1)*x

a = int(input("Введите число A: "))
b = int(input("Введите степень числа A: "))

print(f"Число {a} в степени {b} равно {Stepen(a,b)}")