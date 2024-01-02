my_input = int(input("son kriting :"))
x = 1
while x <= my_input:
    num = 2 ** x
    if my_input >= num:
        print(x, num)
        x += 1