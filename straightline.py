x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

m = (y2 - y1)/(x2 - x1)# gradient
c = y1 - m * x1# y intercept

print(f"{x1}, {y1}") # printing 1st coordinates
print(f"{x2}, {y2}") # printing 2nd coordinates
print(f"y = {m}x + {c}") # y = mx + c
