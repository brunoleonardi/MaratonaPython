num = int(input())
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0

while num >= 100:
    num -= 100
    n100 += 1

while num >= 50:
    num -= 50
    n50 += 1

while num >= 20:
    num -= 20
    n20 += 1

while num >= 10:
    num -= 10
    n10 += 1

while num >= 5:
    num -= 5
    n5 += 1

while num >= 2:
    num -= 2
    n2 += 1

while num >= 1:
    num -= 1
    n1 += 1

print(f'{n100} nota(s) de R$ 100')
print(f'{n50} nota(s) de R$ 50')
print(f'{n20} nota(s) de R$ 20')
print(f'{n10} nota(s) de R$ 10')
print(f'{n5} nota(s) de R$ 5')
print(f'{n2} nota(s) de R$ 2')
print(f'{n1} nota(s) de R$ 1', end="")