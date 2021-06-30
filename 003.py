x = []
for i in range(123, 567):
    if (i % 5 == 0) or (i % 6 == 0) or (i % 30 == 0):
        x.append(i)

print(x)
print("------------")
print(sum(x))
