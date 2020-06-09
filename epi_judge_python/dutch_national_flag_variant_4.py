
def truesify(A):
    
    t_idx = len(A) - 1 
    f_idx = len(A) - 1

    while t_idx >= 0 and f_idx >= 0:
        # Swap when f_idx is in false and t_dx is in true
        if A[t_idx][1] and not A[f_idx][1]:
            A[t_idx], A[f_idx] = A[f_idx], A[t_idx]
            f_idx -= 1
            t_idx -= 1

        # Move f_idx until false
        if A[f_idx][1]: 
            f_idx -= 1
        # Move t_idx until true
        if not A[t_idx][1]: 
            t_idx -= 1
    return A
    
print(truesify([ (1, False), (1, True), (2, False), (2, True), (3, False), (4, False), (3,True), (5, False), (6, False) ]))
