# 2 задание
for y in range(2):
    for x in range(2):
        for z in range(2):
            f = (y <= z) and not(z and x)
            if f == 1:
print(z, x, y, '|', f * 1)
