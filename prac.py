#!/usr/local/bin/python3
def partition_once(S):
    """Perform one partition step around the last element (pivot)."""
    a = 0
    b = len(S) - 1
    pivot = S[b]           # Last element as pivot
    left = a
    right = b - 1

    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left += 1
            right -= 1

    S[left], S[b] = S[b], S[left]  # Place pivot in correct position
    return S

arr = list("CAIEFBJLDGKH")
result = partition_once(arr)
print("".join(result))
