x = int(input())
a = input()
y = int(input())
b = input()
z = int(input())
valor = 0
final = 0



if (x > 5 or y > 5 or z > 5 or x < -5 or y < -5 or z < -5):
    print("números entre -5 e 5 apenas!!")
    
elif (a == '+') and (b == '+'):
    valor = x + y + z

elif (a == '+') and (b == '-'):
    valor = x + y - z

elif (a == '+') and (b == '*'):
    valor = x + y * z

elif (a == '+') and (b == '/'):
    try:
        valor = x + y / z
    except ZeroDivisionError:
        print("erro", end = "")



elif (a == '-') and (b == '+'):
    valor = x - y + z

elif (a == '-') and (b == '-'):
    valor = x - y - z

elif (a == '-') and (b == '*'):
    valor = x - y * z

elif (a == '-') and (b == '/'):
    try:
        valor = x - y / z
    except ZeroDivisionError:
        print("erro", end = "")



elif (a == '*') and (b == '+'):
    valor = x * y + z

elif (a == '*') and (b == '-'):
    valor = x * y - z

elif (a == '*') and (b == '*'):
    valor = x * y * z

elif (a == '*') and (b == '/'):
    try:
        valor = x * y / z
    except ZeroDivisionError:
        print("erro", end = "")



elif (a == '/') and (b == '+'):
    try:
        valor = x / y + z
    except ZeroDivisionError:
        print("erro", end = "")

elif (a == '/') and (b == '-'):
    try:
        valor = x / y - z
    except ZeroDivisionError:
        print("erro", end = "")    

elif (a == '/') and (b == '*'):
    try:
        valor = x / y * z
    except ZeroDivisionError:
        print("erro", end = "")

elif (a == '/') and (b == '/'):
    try:
        valor = x / y / z
    except ZeroDivisionError:
        print("erro", end = "")


if (y == 0 and a =="/") or (z == 0 and b =="/"):
    print("")
else:
    print(int(valor), end = "")
