def binary_search(container, item, left, right):
    if right < left:
        return -1

    middle_index = (left + right) // 2

    if container[middle_index] == item:
        return middle_index

    elif container[middle_index] > item:
        print("좌측 검색")
        return binary_search(container, item, left, middle_index - 1)

    elif container[middle_index] < item:
        print("우측 검색")
        return binary_search(container, item, middle_index + 1, right)


nums = [1, 5, -3, 10, 55, 100]
print(binary_search(sorted(nums), 100, 0, len(nums) - 1))
