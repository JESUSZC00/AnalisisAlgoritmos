def search(A, inicio, fin):
    if inicio <= fin:
        mid = (inicio + fin) // 2
        if mid == A[mid]:  
            return mid
        if mid > A[mid]:  
            return search(A, mid + 1, fin)
        else:  
            return search(A, inicio, fin - 1)
    return -1

if __name__ == "__main__":
    A = [-1, 0, 1, 2, 4, 10]
    print("Magic index", search(A, 0, len(A) - 1))