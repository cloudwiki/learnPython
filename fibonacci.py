print "demo for fibnocci numbers"

def fibFun(n):
    'Calculate Fibnocci numbers'
    fib_array = [1,1]
    if(n==1):
        pass
    else:
        for num in range(n-2):
            print num
            fib_array.append(fib_array[-2] + fib_array[-1])
    return fib_array
    
    
print fibFun(1)

print fibFun(100)