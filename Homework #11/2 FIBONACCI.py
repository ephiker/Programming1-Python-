##21000348 Andre Seo
##Fibonacci


def display(n):
    print (" "*6*indent, "fib(%d)" % n)

    
##def compute(n):
##    return fib(n-1) + fib(n-2) ##fibonacci


def fib(n):
    global indent
    indent += 1
        
    if n == 1 or n == 0 :
        display(n)
        indent -= 1
        return 1
    
    else:
        display(n)
        result = fib(n-1) + fib(n-2)
        indent -= 1
        return result


#Main Program
indent = 0
fib(6)
