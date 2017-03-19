import random
import math

circle = 0
for count in range(0, 1000000):
    d = math.hypot(random.random(), random.random())
    if d < 1:
        circle += 1
    count += 1
print(4.0 * circle / count)
