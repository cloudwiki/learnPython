def binarySearch(num_array, n, lower, upper):
    'binary search'
    if lower == upper:
        assert num_array[lower] == n, str(n) +' not found in array'
        return lower
    else:
        pivot = (lower + upper) / 2
        if n > num_array[pivot]:
            return binarySearch(num_array, n, pivot+1, upper)
        else:
            return binarySearch(num_array, n, lower, pivot)
        
            
random_nums = range(0,100)
#print random_nums
print binarySearch(random_nums, 191, 0, len(random_nums)-1)
