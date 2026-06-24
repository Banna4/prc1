def revers(a):
    left = 0
    right = len(a) - 1

    while left < right:
        a[left],a[right] = a[right],a[left]
        left += 1
        right -= 1
    return a
print(revers([1,2,3,4,5,5]))