def grid_path(n, m, memo={}):
    if (n, m) in memo:
        return memo[(n, m)]
    if n == 1 or m == 1:
        return 1
    
    memo[(n, m)] = grid_path(n, m-1) + grid_path(n-1, m)
    return memo[(n, m)]

print(grid_path(3, 3))
