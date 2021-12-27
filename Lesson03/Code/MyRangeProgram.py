# range(number): returns a sequence of number from 0 to number-1
# range(10): returns 0, 1, 2, 3, ..., 9
# range(360): return 0, 1, 2, 3, ..., 359

seq = range(6)
print(seq)
print(len(seq))

for x in range(10):
    print(x, x**2, x**3, x*2, x*3)
