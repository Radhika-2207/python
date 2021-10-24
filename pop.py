alpha = ['a','b','c']
print(alpha)

#using pop directly in the print 
print(alpha.pop())

#using pop through a variable
popped_alpha = alpha.pop()
print(popped_alpha)

alpha = ['a','b','c']

#pop on my own account
print(alpha.pop(2))

alpha = ['a','b','c']
#using remove to remove elements
alpha.remove('a')
print(alpha)