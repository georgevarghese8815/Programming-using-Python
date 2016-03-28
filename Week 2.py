# while loop
x = 4
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + '=' + str(ans))
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print "Number of apples: " + str(numberOfApples)

num = 10
while True:
    if num < 7:
        print 'Breaking out of loop'
        break
    print num
    num -= 1
print 'Outside of loop' 


num = 100
while not False:
    if num < 0:
        break
print 'num is: ' + str(num)


# lecture 3.2, slide 6
# Find the cube root of a perfect cube
x = int(raw_input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))


# lecture 3.3, slide 3
# Find the cube root of a perfect cube
x = int(raw_input('Enter an integer: '))
for ans in range(0, abs(x)+1):
    if ans**3 == abs(x):
        break
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))
    

# lecture 3.4, slide 3
# Converting Decimal to Binary

num = int(raw_input('Enter an integer: '))

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num/2
if isNeg:
    result = '-' + result

print('Result is: ' + result)


# lecture 3.4, slide 4

x = float(raw_input('Enter a decimal number between 0 and 1: '))

p = 0
while ((2**p)*x)%1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1

num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num/2

for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))


# lecture 3.5, slide 2

x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while (abs(ans**2 - x)) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print('numGuesses = ' + str(numGuesses))
if abs(ans**2-x) >= epsilon:
    print('Failed on square root of ' + str(x))
else:
    print(str(ans) + ' is close to the square root of ' + str(x))
    
    
# lecture 3.6, slide 2
# bisection search for square root

x = 12345
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))



num = int(raw_input(""))
print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = False
while not guess:
    mid = int((low + high)/2)
    print("Is your secret number " + str(mid) + '?')
    x = str(raw_input('Enter ''h'' to indicate the guess is too high. Enter ''l'' to indicate the guess is too low. Enter ''c'' to indicate I guessed correctly.'))
    if(x == 'h'):
        high = mid
    elif(x == 'l'):
        low = mid
    elif(x == 'c'):
        guess = True
        print("Game over. Your secret number was: " + str(mid))
    else:
        print("Sorry, I did not understand your input.")

    

# Lecture 3.7, slide 3
# Newton-Raphson for square root

epsilon = 0.01
y = .0
guess = y/2.0

while abs(guess*guess - y) >= epsilon:
    guess = guess - (((guess**2) - y)/(2*guess))
    print(guess)
print('Square root of ' + str(y) + ' is about ' + str(guess))




## Example of computation without and with functional abstraction

## Without functional abstraction

##x = raw_input('Enter a number: ')
##p = int(raw_input('Enter an integer power: '))
##
##result = 1
##
##for turn in range(p):
##    print('iteration: ' + str(turn) + ' current result: ' + str(result))
##    result = result * x


## With functional abstraction

def iterativePower(x,p):
    result = 1
    for turn in range(p):
        print ('iteration: ' + str(turn) + ' current result: ' + str(result))
        result = result * x
    return result
    
    

# From Lecture 4, How Environments Separate Variable Bindings

def square(x):
    return x*x

def twoPower(x,n):
    while n > 1:
        x = square(x)
        n = n/2
    return x




# From Lecture 4, How Environments Separate Variable Bindings

def square(x):
    return x*x

def twoPower(x,n):
    while n > 1:
        x = square(x)
        n = n/2
    return x
    
twoPower(2, 6)




# From Lecture 4, Understanding Root Finding

# root code

def findRoot1(x, power, epsilon):
    low = 0
    high = x
    ans = (high+low)/2.0
    while abs(ans**power - x) > epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0
    return ans

print findRoot1(25.0, 2, .00001)
print findRoot1(27.0, 3, .001)
print findRoot1(-27.0, 3, .001)


# so can't find cube root of negative number

def findRoot2(x, power, epsilon):
    if x < 0 and power%2 == 0:
        return None
    # can't find even powered root of negative number
    low = min(0, x)
    high = max(0, x)
    ans = (high+low)/2.0
    while abs(ans**power - x) > epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0
    return ans

##print findRoot2(25.0, 2, .001)
##print findRoot2(27.0, 3, .001)
##print findRoot2(-27.0, 3, .001)
##
##print findRoot2(0.25, 2, .001)
##print findRoot2(-0.125, 3, .001)



def findRoot3(x, power, epsilon):
    if x < 0 and power%2 == 0:
        return None
    # can't find even powered root of negative number
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high+low)/2.0
    while abs(ans**power - x) > epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0
    return ans

print findRoot3(25.0, 2, .001)
print findRoot3(27.0, 3, .001)
print findRoot3(-27.0, 3, .001)

print findRoot3(0.25, 2, .001)
print findRoot3(-0.125, 3, .001)