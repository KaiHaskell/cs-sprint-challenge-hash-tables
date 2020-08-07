def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Your code here
    cache = {}
    result = []

    # if the num has a corresponding number in dictionary
    for num in a:
        cache[num] = num
        # if the number is not equal to 0 AND there's a negative version in the cache
        if num != 0 and -num in cache:
            # append the absolute version of that num into the result array
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
