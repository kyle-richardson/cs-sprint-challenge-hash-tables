def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    result = []
    for x in a:
        if (x * -1) in d:
            result.append(abs(x))
        else:
            d[x] = x

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
