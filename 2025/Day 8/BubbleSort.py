#bubble sort

def bubble_sort(A, B):
    A = A[:]   # copy list (avoid modifying original if imported)
    B = B[:]

    n = len(A)

    for i in range(n):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                # swap in A
                A[j], A[j + 1] = A[j + 1], A[j]
                # matching swap in B
                B[j], B[j + 1] = B[j + 1], B[j]

    return A, B
