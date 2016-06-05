from engine import main
from timing.timer import timeit
from math import factorial
    
@timeit
def comp(x,q):
    summa = 0
    for i in xrange(x):
        summa += sum([factorial(elem) for elem in xrange(0,i)])
    q.put(summa)

@timeit
def thing(x):    
    listing = range(x)

    for i in listing:
        comp(i)

@timeit
def stress_test(x):
    listing = range(x)
    main(listing,comp)

for i in [5,50,100,200,300]:
    print stress_test(i)
