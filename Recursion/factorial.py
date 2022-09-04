def factorial(n):
    " Calculate n! "
    if n == 1:
        return 1  # Condition for recursion: base case & return statement
    return factorial(n - 1) * n


print(factorial(4))
