print("hello world")
name = raw_input('Enter a name:')
age = int(raw_input('Enter your age:'))

#new code
x = 3
x = x * x
print(x)
y = float(raw_input('Enter a number: '))
print(y * y)


#new code
x = int(raw_input('Enter a number: '))
if (x%2 == 0):
    print('')
    print('The number you entered is even')
else:
    print('')
    print('The number you entered is odd')

print('Done')

#new code
temp = 120
if temp > 85:
   print "Hot"
elif temp > 100:
   print "REALLY HOT!"
elif temp > 60:
   print "Comfortable" 
else:
   print "Cold" 

varA = 2
varB = ''
#new code
if type(varA) == int or type(varB) == str:
    print 'string involved'
elif varA > varB:
    print 'bigger'
elif varA == varB:
    print 'equal'
elif varA < varB:
    print 'smaller'
    
print("Hi")
