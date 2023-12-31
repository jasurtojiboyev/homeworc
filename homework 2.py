list = [100, 233, 42, 22, 43, 334, 54, 254, 555,]
def foyiz(list):
    son = 100
    index = 0
    input1 = int(input("son kriting :"))
    while index < len(list):
        current_number = list[index]
        m = current_number / son * input1
        print(m)
        index += 1
foyiz(list)