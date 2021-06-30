
x = []
for num in range(200, 20, -1):
    if (num % 5 == 0) and (num % 3 != 0):
        x.append(num)
        continue
print(x)
