first = 0
second = 1
set = int(input('Enter how many times you want to have it repeat: '))
print(first)
print(second)
for i in range(2, set):
    third = first + second
    print(third)
    first = second
    second = third
