def prune(num):
    num ^=15 
    num &=16777215
    return num

def calculate(num):
    num <<= 6
    num = prune(num)
    num >>= 5
    num = prune(num)
    num <<=11
    num = prune(num)
    return num
print(calculate(123))
