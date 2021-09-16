def fibonacci_tail(n, a = 0, b = 1):
    
    if n == 0: 
        return a
    if n == 1: 
        return b
 
    return fibonacci_tail(n - 1, b, a + b)