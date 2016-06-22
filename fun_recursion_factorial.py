def factorial(n):
    'factorial array'
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)

        
print "factorial recursion:"
print factorial(1)
print factorial(10)



def binarySearch(num_array, n, lower, upper):
    'binary search'
    if(lower == upper):
        assert num_array[lower] == n
        return lower
    else:
        pivot = (lower + upper) / 2
        if(num_array[pivot] > n):
            binarySearch(num_array, n, lower, pivot)
        else:
            binarySearch(num_array, n, pivot, upper)
            
random_nums = range(1,100)
print random_nums

print binarySearch(random_nums, 10, 0, len(random_nums)