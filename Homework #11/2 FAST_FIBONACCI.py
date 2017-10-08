##21000348 Andre Seo
##Fast Fibonacci


def display(n, flag):
    if flag:
        print (" "*6*indent, "fib(%d)" % n, "Already computed")
    else:
        print (" "*6*indent, "fib(%d)" % n)

def compute(n, memo):
    return fast_fib(n-1, memo) + fast_fib(n-2, memo) ##fibonacci

def fast_fib(n, memo = {}):
    global indent, flag, count
    indent += 1
    
    if n in memo: #dyanmic programming
        flag = True
        display(n, flag)
        indent -= 1
        return memo[n]


    if n == 0 or n == 1:
        flag = False
        display(n, flag)
        indent -= 1
        return 1
    
    else:
        count += 1
        flag = False
        display(n, flag)
        result = fast_fib(n-1, memo) + fast_fib(n-2, memo)
        memo[n] = result
        indent -= 1
        return result



#Main Program
count = 0
indent = -1
print (fast_fib(6), count)
