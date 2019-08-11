def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 != 0:
        print((number * 3) + 1)
        return (number * 3) + 1



print('Type in an integer: ')
n = int(input())
var = collatz(n)

while var != 1:
    var = collatz(var)
