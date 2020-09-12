def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    first_intersection = {}
    result = []
    for arr in arrays:
        for x in arr:
            if first_intersection.get(x) is not None:

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
