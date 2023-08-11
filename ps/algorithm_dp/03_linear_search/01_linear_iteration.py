def linear_search(container, item):

    for idx in range(len(container)):
        if container[idx] == item:
            return idx

    return -1


nums = [1, 5, -3, 10, 55, 100]
print(linear_search(nums, 10))
