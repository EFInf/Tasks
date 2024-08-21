def find_maximum_subarray(A):
    max_seen = max_end = 0

    for a in A:
        max_end = max(a, a + max_end)
        max_seen = max(max_seen, max_end)
    return max_seen

A = [904, 40, 523, 12, -335, -385, -124, 481, -31]

print(find_maximum_subarray(A))