#Number Theory; 
#Classes - Seive, 
#Functions - largestPrimeFactor, factors, numberOfFactors, 
#               properDivisors, sumDivisors, eulerPhi, 
#                   order of an integer modulo n

class Sieve(object):
    #This class generates both;
    # a list of primes up to given integer n 
    # and a list containing a factor of i at index i.
    def __init__(self, n):
        z = [0]*(n+1)
        k = 2
        while k<= n:
            for i in range(k,len(z),k):
                z[i] =  k
            j=k+1
            while j < len(z)-1:
                if z[j]==0:
                    k = j
                    z[k] = k
                    break
                j+=1
            if j == len(z)-1:
                break
        l = []
        for i in range(2,len(z)):
            if z[i]==i:
                l.append(i)

        self.seive = z
        self.primes = l

    def getAll(self):
        return self.seive
    
    def getPrimes(self):
        return self.primes

    def contract(self,n):
        if self.primes[-1]<=n:
            return self.primes
        else:
            i = 0
            while self.primes[i]<= n:
                i+=1
            return self.primes[:i]

def egcd(a, b): #Euclidean GCD
    if a == 0:
        return (b, 0, 1)
    else:
        d, y, x = egcd(b % a, a)
        return (d, x - (b // a) * y, y)

def gcd(a,b, t = 0):
    if b % a == 0:
        return a
    return gcd(b%a, a)

def lcm(arr):
    a = arr[0]
    if len(arr) == 2:
        b = arr[1]
    else:   
        b = lcm(arr[1:])
    return (a*b)/gcd(a,b)

def inverse(a, m):  
    #Modular inverse for a mod m
    d, x, y = egcd(a, m)
    if d != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def largestPrimeFactor(n):
    P = Seive(n+1).contract(int(n**0.5) + 1)
    for i in range(1,len(P)+1):
        if n%P[-i] == 0:
            return P[-i]
    return n

def factors(n):
    if n == 1:
        return []
    p = largestPrimeFactor(n)
    return [p] + factors(n/p)

def numFactors(n):
    f= factors(n)
    df = [f.count(x) for x in set(f)]
    numfacts = 1
    for j in range(len(df)):
        numfacts = numfacts*(df[j]+1)
    return numfacts

def properDivisors(n):
    f = factors(n)
    nf = numFactors(n)
    divisors = []
    for i in range(2**len(f)-1):
        b = str(bin(i)[2:])
        b = b.zfill(len(f))
        x = 1
        for i in range(len(f)):
            x = x*(f[i]**int(b[i]))
        divisors.append(x)
    if n in divisors:
        divisors.remove(n)
    return set(divisors)
    
def sumDivisors(k):
    f = factors(k)
    df = {x:f.count(x) for x in set(f)}
    sum = 1
    for p in set(f):
        sum = sum * int((p**(df[p]+1)-1)/(p-1)) 
    return sum

def eulerPhi(n):
    vf = n
    for p in set(factors(n)):
        vf = vf*(p - 1)/p
    return vf

def power(a,n,m,memo = {1:1,2:4}):
    s = [int(c) for c in bin(n)[2:]]
    s.reverse()
    if s[0] == 1:
        total = a
    else:
        total = 1
    for i in range(1,len(s)):
        a = pow(a,2,m)
        if s[i]==1:
            total = (total * a) % m
    return total

def order(a,n):
    if n == 1:
        return 0
    else:
        x = 1
        i = 0
        while True:
            i+=1
            x = (x*a) % n
            if x == 1:
                break
        return i

def nCk(n,k, memo = {(2,1):2}):
    if k>n/2:
        k = n-k
        
    if k in {0,n}:
        return 1
    elif k in {1,n-1}:
        return n
    elif (n,k) not in memo:        
        memo[(n,k)] = nCk(n-1,k-1) + nCk(n-1,k)
    
    return memo[(n,k)]
