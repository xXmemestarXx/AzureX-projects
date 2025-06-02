x = int(input("Look for: "))
L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def BinarySearch(L, x, left, right) -> int:
    if left > right:
        return "Not found"  # Base case: if element is not found
    
    m = (left + right) // 2  # Middle index

    if L[m] == x:
        return m
    elif L[m] < x:
        return BinarySearch(L, x, m + 1, right)  # Search right half
    else:
        return BinarySearch(L, x, left, m - 1)  # Search left half

# Initial call to the function
result = BinarySearch(L, x, 0, len(L) - 1)
print(result)