my_input = int(input("son kriting :"))
x = 1
while x <= my_input:
    num = x ** 2
    if my_input >= num:
        print(x, num)
    x += 11