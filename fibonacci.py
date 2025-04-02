"""
Exemplo de Fibonacci iterativo.
"""

def fibonacci_iterativo(n):
    a, b = 0, 1
    
    for _ in range(n):
        a, b = b, a + b
    
    return a


def fibonacci_recursivo(n):
    if n <= 1:
        return 1
    
    return fibonacci_recursivo(n -1) + fibonacci_recursivo(n - 2)

for n in range(20):
    print(fibonacci_recursivo(n), end=" ")
    
# resultado = fibonacci(20000)
# print(f"{resultado}")