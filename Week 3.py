def iterMul(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result
    

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    while (exp > 0):
        result = result * base
        exp -= 1
    return result
    
    
def recurMul(a, b):
    if b == 1:
        return a
    else:
        return a + recurMul(a, b-1)
        
        
def factI(n):
    """assumes that n is an int > 0
       returns n!"""
    res = 1
    count = 1
    while n > 1:
        res = res * n
        n -= 1
        print(count)
        count += 1
    return res

def factR(n):
    """assumes that n is an int > 0
       returns n!"""
    if n == 1:
        return n
    return n*factR(n-1)
    
    

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if(exp == 0):
        return 1
    return (base * recurPower(base, exp-1))
    
    
    
def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if (exp == 0):
        return 1
    if(exp%2 == 0):
        return recurPowerNew(base**2, exp/2)
    if (exp%2 == 1):
        return base * recurPowerNew(base, exp-1)
        
        
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if (b == 0):
        return a
    else:
        return gcdRecur(b, a%b)
        
        
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
        

#Fibonacci Series

def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)



#Palindrome
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))



def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)


def testFib(n):
    for i in range(n+1):
        global numCalls
        numCalls = 0
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print('fib called ' + str(numCalls) + ' times')


## divisors using tuples
def findDivisors(n1, n2):
    """assumes that n1 and n2 are positive ints
       returns a tuple containing the common divisors of n1 and n2"""
    divisors = () # the empty tuple
    for i in range(1, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors = divisors + (i,)
    return divisors


divisors = findDivisors(20, 100)
total = 0
for d in divisors:
    print d
    total += d
print(total)



## universities

Techs = ['MIT', 'Cal Tech']
Ivys = ['Harvard', 'Yale', 'Brown']

Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]

Techs.append('RPI')

print('Univs = ')
print(Univs)
print('')
print('Univs1 =')
print(Univs1)


for e in Univs:
    print('Univs contains ')
    print(e)
    print('   which contains')
    for u in e:
        print('      ' + u)

#remove duplicates
def removeDups(L1, L2):
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)

L1 = [1,5,3,4]
L2 = [1,2,5,6]
removeDups(L1, L2)
print(L1)


def removeDupsBetter(L1, L2):
    L1Start = L1[:]
    for e1 in L1Start:
        if e1 in L2:
            L1.remove(e1)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDupsBetter(L1, L2)
print(L1)


L1 = [1,5,3,4]
L2 = L1
print (L1)
print L2

L1 = [1,5,3,4]
L3 = L1[:]
print (L1)
print L2
L1[2] = 'Hello'




# applyToEach
def applyToEach(L, f):
    """assumes L is a list, f a function
       mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])


L = [1, -2, 3.4]

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

applyToEach(L, abs)
print(L)

applyToEach(L, int)
print(L)

applyToEach(L, fact)
print(L)

applyToEach(L, fib)
print(L)