def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    # first we find all the arrays
    for i in range(len(arrays)):
        # then we do a simple check if the number is
        # already in our cache or not
        for n in arrays[i]:
            if n not in cache:
                cache[n] = 1
            elif n in cache:
                cache[n] += 1

    # then we add everything to result that has the same amount of
    # values in the cache as the amount of arrays
    l = len(arrays)
    result = result + [k for k, v in cache.items() if v == l]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
