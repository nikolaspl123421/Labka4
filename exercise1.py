# Дано два дійсних числа: x, y(x != y). Менше з них піднести до квадрату, а більше замінити пів-сумою цих чисел.

x = float(input("Введіть перше число ="))
y = float(input('Введіть друге число ='))

if x > y:
    x = (x+y)/2
    y = y**2
    print(x)
    print(y)
elif x < y:
    x = x**2
    y = (y+x)/2
    print(x)
    print(y)