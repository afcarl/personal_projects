from engine import main
from timing.timer import timeit
from math import factorial
from function import fib2    

@timeit
def comp(x,q):
    summa = 0
    for i in xrange(x):
        summa += sum([factorial(elem) for elem in xrange(0,i)])
    q.put(summa)

@timeit
def comp2(x):
    summa = 0
    for i in xrange(x):
        summa += sum([factorial(elem) for elem in xrange(0,i)])
    return summa

@timeit
def stress_test2(x):    
    listing = range(x)
    for i in listing:
        comp2(i)

@timeit
def stress_test(x):
    listing = range(2,x)
    main(listing,fib2)

@timeit
def test():
    for i in range(10):
        print fib(i)

    
def Main():
    print stress_test(30)

if __name__ == '__main__':
    stress_test(7500)
