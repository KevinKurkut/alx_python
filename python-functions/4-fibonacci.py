def fibonacci_sequence(n):
    sequence =[0, 1]
    for i in range(2, n):
        next_sequence = sequence[-1] + sequence[-2]
        sequence.append(next_sequence)
        return sequence