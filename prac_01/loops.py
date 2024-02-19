for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

num_stars_1 = int(input("Number of stars:"))
for i in range(num_stars_1):
    print("*", end='')
print()

num_stars_2 = int(input("Number of increasing stars:"))
for i in range(num_stars_2+1):
    print("*" * i)
print()