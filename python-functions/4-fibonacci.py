def fibonacci_sequence(n):
    """function takes a n as input parameter"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            next_seq = sequence[-1] + sequence[-2]
            sequence.append(next_seq)
        return sequence
    