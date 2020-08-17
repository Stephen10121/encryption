import random
def goforit(input_value):
    key = random.randrange(11111111 , 99999999)
    #jeff = key
    #new = new.format(key , )
    #if my_number % 2 == 0
    value = key
    test = 1 + value
    test = str(test)
    input_value = input_value.replace("a", str(1 + value) + ".")
    input_value = input_value.replace("b", str(2 - value) + ".")
    input_value = input_value.replace("c", str(3 + value) + ".")
    input_value = input_value.replace("d", str(4 - value) + ".")
    input_value = input_value.replace("e", str(5 + value) + ".")
    input_value = input_value.replace("f", str(6 - value) + ".")
    input_value = input_value.replace("g", str(7 + value) + ".")
    input_value = input_value.replace("h", str(8 - value) + ".")
    input_value = input_value.replace("i", str(9 + value) + ".")
    input_value = input_value.replace("j", str(10 - value) + ".")
    input_value = input_value.replace("k", str(11 + value) + ".")
    input_value = input_value.replace("l", str(12 - value) + ".")
    input_value = input_value.replace("m", str(13 + value) + ".")
    input_value = input_value.replace("n", str(14 - value) + ".")
    input_value = input_value.replace("o", str(15 + value) + ".")
    input_value = input_value.replace("p", str(16 - value) + ".")
    input_value = input_value.replace("q", str(17 + value) + ".")
    input_value = input_value.replace("r", str(18 - value) + ".")
    input_value = input_value.replace("s", str(19 + value) + ".")
    input_value = input_value.replace("t", str(20 - value) + ".")
    input_value = input_value.replace("u", str(21 + value) + ".")
    input_value = input_value.replace("v", str(22 - value) + ".")
    input_value = input_value.replace("w", str(23 + value) + ".")
    input_value = input_value.replace("x", str(24 - value) + ".")
    input_value = input_value.replace("y", str(25 + value) + ".")
    input_value = input_value.replace("z", str(26 - value) + ".")
    return input_value