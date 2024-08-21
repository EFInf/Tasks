def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

A = [3,6,34,5,7,8,2,45,7,8,6,4,3,12,345,6]
even_odd(A)
print(A)