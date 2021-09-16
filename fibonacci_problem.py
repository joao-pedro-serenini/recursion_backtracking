def fibonacci_recursion(n):

    if n == 0:
        return 1

    if n == 1:
        return 1
    
    
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

# top-down approach
def fibonacci_memoization(n, table):

    if n not in table:
        table[n] = fibonacci_memoization(n-1, table) + fibonacci_memoization(n-2, table)
    
    # return table
    return table[n]

# bottom-up approach
def fibonacci_tabulation(n, table):

    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    
    # return table
    return table[n]

# print(fibonacci_recursion(5))

t = {0: 1, 1: 1}
# print(fibonacci_memoization(5, t))
print(fibonacci_tabulation(5, t))
