#addition
def plus_one(number):
    return number + 1
    
def add(num1, num2):
    total_sum = num1
    for i in range(num2):
        total_sum = plus_one(total_sum)
    return total_sum
print(add(2,8))


#multiplication

def plus_one(number):
    return number + 1
    
def multiply(num1, num2):
    multiple = num1
    for i in range(1,num2): 
        for i in range(num1):
           multiple = plus_one(multiple)
    return multiple
print(add(2,9))