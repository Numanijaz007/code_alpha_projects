def fibonacci_generator():
    """Generate an infinite sequence of Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    fib = fibonacci_generator()
    print("First 10 Fibonacci numbers:")
    for _ in range(10):
        print(next(fib))
    
