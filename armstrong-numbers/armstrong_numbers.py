def is_armstrong_number(number):
    number_len = len(str(number))
    result = 0
    for i in str(number):
        result += pow(int(i), number_len)

    return True if result == number else False


