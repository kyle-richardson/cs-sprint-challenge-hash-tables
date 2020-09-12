

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    for idx in range(length):
        solved = []
        current_weight = weights[idx]
        stored = hash_table.get(f'{limit-current_weight}')
        if stored is not None:
            if stored > idx:
                solved.append(stored)
                solved.append(idx)
            else:
                solved.append(idx)
                solved.append(stored)
            return solved
        else:
            hash_table[f'{current_weight}'] = idx

    return None
