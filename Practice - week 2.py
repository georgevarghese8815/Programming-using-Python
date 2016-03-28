myStr = '6.00x'

for char in myStr:
    print char

print 'done'


greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print letter 
    print letter

print 'done'


school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print char
    else:
        numCons -= 1
        
        
        
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print char
    else:
        numCons -= 1

print 'numVowels is: ' + str(numVowels)
print 'numCons is: ' + str(numCons)




num = 10
for num in range(5):
    print num
print num 



divisor = 2
for num in range(0, 10, 2):
    print num/divisor 
    
    
for variable in range(20):
    if variable % 4 == 0:
        print variable
    if variable % 16 == 0:
        print 'Foo!'
        

for letter in 'hola':
    print letter 



count = 0
for letter in 'Snow!':
    print 'Letter # ' + str(count) + ' is ' + str(letter)
    count += 1
    break
print count 



    
for num in range(2, 11, 2):
    print (str(num))
print('Goodbye!')


print('Hello!')
for num in range(10, 1, -2):
    print (str(num))
    
end = 6
ans = 0
for num in range(end + 1):
    ans = ans + num
print(ans)



iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1 


iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1
    

def a(x):
   '''
   x: int or float.
   '''
   return x + 1


x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)
g(x)
    

# can't find even powered root of negative number
x = -27
power = 3
epsilon = 0.01
low = min(0, x)
print low
high = max(0, x)
print high
ans = (high+low)/2.0
print ans
while abs(ans**power - x) > epsilon:
    if ans**power < x:
        low = ans
    else:
        high = ans
    print ("low = " + str(low) + ":" + "High = " + str(high))
    ans = (high+low)/2.0
    print(" Ans = " + str(ans))
print ans



x = -0.274625

power = 3
epsilon = 0.01
low = min(-1.0, x)
print low
high = max(1.0, x)
print high
ans = (high+low)/2.0
print ans
while abs(ans**power - x) > epsilon:
    if ans**power < x:
        low = ans
    else:
        high = ans
    print ("low = " + str(low) + ":" + "High = " + str(high))
    ans = (high+low)/2.0
    print(" Ans = " + str(ans))
    
print ans

print findRoot3(25.0, 2, .001)
print findRoot3(27.0, 3, .001)
print findRoot3(-27.0, 3, .001)

print findRoot3(0.25, 2, .001)
print findRoot3(-0.125, 3, .001)



s = 'sdasbobobasdasdbobasdebobob'
count = 0
for i in range(len(s) - 2):
    if (s[i:i+3] == 'bob'):
        count += 1
print ('Number of times bob occurs is: ' + str(count))



def item_order(order):
    sal = order.count('salad')
    ham = order.count('hamburger')
    wat = order.count('water')
    output = 'salad:' + str(sal) + ' hamburger:' + str(ham) + ' water:' + str(wat)
    return output

order = 'salad hamburger salad hamburger'   
item_order(order)

