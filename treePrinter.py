print("Enter tree size: ")
size = int(input())

for row_num in range(1,size + 1):
    spaces =" " * (size - row_num)
    branch = '^' * (row_num*2 - 1)
    print(spaces+branch)
    
#print trunk
spaces =" " * (size - 1)
print(spaces + '#')
print(spaces + '#')
print(spaces + '#')