import decimal
import multiprocessing

def factorial(num, isOddFactorial):
    
    total = 1
    
    if num == 0:
        return total

    step = 1

    if isOddFactorial:
        step = 2

    for x in xrange(1,num+1, step):
        total *= x


    return total

def processInput(num):
    # Using Newton-Euler Conjecture for approximating the value of PI
    return  2*decimal.Decimal(factorial(num, False))/decimal.Decimal(factorial(2*num+1, True))
       

def main():
    decimal_place = raw_input("Enter a Decimal Place: ")

    decimal.getcontext().prec = 300
    
    pool = multiprocessing.Pool(multiprocessing.cpu_count())

    tasks = [(x,) for x in xrange(1000)]

    results = [pool.apply_async(processInput, t) for t in tasks]

    val = 0 

    for result in results:
         val += result.get()

    print format(val, '.%sf' % decimal_place)



if __name__ == "__main__":
    main()

    
