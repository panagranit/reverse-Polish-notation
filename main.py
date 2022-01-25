
'''The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

 This like reverse polish notation in calculator only the stack can be Infinite!  '''



stack = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']

#counts_of_operators
def operatorcount(stack):
  
  for i, x in enumerate(stack):
    x = str(x)
    try:
     eval(x)# eval works because it returns error if an operator is found
    except:
     
     i += 1
  return (i)
lenofop = operatorcount(stack)
#this does binary operation between the stack elements

def revb(x,y,z):
  
  res = str(x)+str(z)+str(y)
  return eval(res)


stack = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
print(stack) 

for w in range(lenofop):
  for i, x in enumerate(stack):
    x = str(x)
    try:
 
     
     eval(x)
    except:
     print(' operator found', x)
     print( "position",i)
     #print(stack)
   # Pop the first three items from the stack and then call my function to perform the mathematical
   # operation then put that result back into the stack then go to the next item in the list
     z =stack.pop(i)
     y = stack.pop(i-1)
     x = stack.pop(i-2)
     #print('x',x,'y',y)
   #print(stack)
     print(revb(x,y,z))
     stack.insert(i-2,(revb(x,y,z)))
     #print('index',i)
     print(stack)
   #need to restart for statement at begining of stack
     break

 
  

  
  

