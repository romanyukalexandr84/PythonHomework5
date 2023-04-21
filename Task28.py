def Summa (a,b):
    if b == 0:
        return a
    else:
        return Summa(a+1,b-1)

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))

print(f"Сумма чисел равна {Summa(x,y)}")