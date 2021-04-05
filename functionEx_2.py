

def add_and_subtract():
    num1 = int(input('Enter First number : '))
    num2 = int(input('Enter Second number : '))
    num3 = int(input('Enter Third number : '))
    result = sum_nums(num1,num2)
    subtract_nums(result,num3)


def sum_nums(num1, num2):
    result_1 = num1 + num2
    return result_1

def subtract_nums(result_1,num3):
    result_2 = result_1-num3
    print(result_2)

add_and_subtract()






        