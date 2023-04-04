print("*"*10 , "Калькулятор", "*"*10)

while True:
    print ("Введите q для выхода")
    print("Введите математическое выражение")
    s = input("Операция (+,-,*,/)")
    if s == "q": break
    if s in ("+","-","*","/"):
        x = int(input("x="))
        y = int(input("y="))
        if s == "+":
            print((x+y))
        elif s == "-":
            print((x-y))
        elif s == "*":
            print((x*y))
        elif s == "/":
            try:
                print((x/y))
            except ZeroDivisionError:
                print('ДУРАК???!')
    else:
        print("Неверный знак")
        
        