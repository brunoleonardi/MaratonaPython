x = int(input()) 
y = int(input())

if (x > 0) and (x <= 50) and (y > 0) and (y <= 50):
    print("R1", end = "")

elif (x < 0) and (x >= -50) and (y > 0) and (y <= 50):
    print("R2", end = "")

elif (x < 0) and (x >= -50) and (y < 0) and (y >= -50):
    print("R3", end = "")

elif (x > 0) and (x <= 50) and (y < 0) and (y >= -50):
    print("R4", end = "")

elif ((x == 0) and (y != 0)) or ((x != 0) and (y == 0)):
    print("Apenas pode ter dois zeros ou nenhum!!", end = "")

elif (x == 0) and (y == 0):
    print("NO ALVO!", end = "")
