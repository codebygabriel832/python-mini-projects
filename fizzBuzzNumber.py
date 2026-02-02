print('Enter a number')
interger = int(input())

if interger % 3 == 0 and interger % 5 == 0:
    print('Fizz Buzz')
elif interger % 3 == 0:
    print('Fizz')
elif interger  % 5 == 0:
    print('Buzz')

else: 
    print(interger)