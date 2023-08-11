def linear_search(
    container,
    item,
    idx: int = 0,
):
    if idx == len(container):
        return -1

    if container[idx] == item:
        return idx

    else:
        return linear_search(container, item, idx + 1)


nums = [1, 5, -3, 10, 55, 100]
print(linear_search(nums, 10430, 0))
