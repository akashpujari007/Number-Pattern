n = int(input())
i = 1
totalspace = 2*n - 2
while i <= n:
    num1 = 1
    while num1 <= i:
        print(num1, end='')
        num1 += 1
    space = 1
    while space <= totalspace:
        print(' ', end='')
        space = space + 1
    totalspace = totalspace -2
    num1 = i
    while num1 > 0:
        print(num1, end='')
        num1 = num1 - 1
    i = i + 1
    print()