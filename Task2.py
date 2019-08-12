print("Привіт,я простий калькулятор на чотири дії!")
x = float(input("Введіть перше число :"))
y = float(input("Введіть друге число :"))
z = input("Введіть дію :")
if z == "+":
    z = x + y
    print(str(z))
elif z == "-":
    z = x - y
    print(str(z))
elif z == "*":
    z = x * y
    print(str(z))
elif z == "/":
    if int(y) != 0:
        z = x / y
        print(str(z))
    else:
        print("Ділення на нуль неможливе!")
else:
    print("Не вірно обрано дію!")
