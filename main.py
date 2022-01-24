
'''The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.'''


languages = ['Python', 'C', 'C++', 'C#', 'Java']

#Bad way

#Good Way


#this does binary operation between the stack elements

def revb(x,y,z):
  
  res = str(x)+str(z)+str(y)
  return eval(res)
# x + y



# This will determine if the string is a function or a number.


 

stack = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
print(stack) 
# append() function to push
# element in the stack

#stack.append('a')

#stack.append('b')

#stack.append('c')

for w in range(10):
  for i, x in enumerate(stack):
    x = str(x)
    try:
 
     
     eval(x)
    except:
     print(' operator found', x)
     print( "position",i)
     #print(stack)
   # Pop the first two items from the stack and then call my function to perform the mathematical
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

 
  

  
  

