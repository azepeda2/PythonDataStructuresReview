# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
# Print out the Fibonacci sequence until the given n-th in the sequence.
# Example: n = 7,
# Print out the sequence: 0, 1, 1, 2, 3, 5, 8

n = 7
fib_sequence = [0, 1]

for i in range(2, n):
    next_fib_number = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_fib_number)

print(fib_sequence)
