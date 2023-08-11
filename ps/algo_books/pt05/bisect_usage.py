import bisect


a = [1, 1, 1,1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 6]


print(f"bisect.bisect_left(a, 5): {bisect.bisect_left(a, 5)}")
print(f"bisect.bisect_right(a, 5) : {bisect.bisect_right(a, 5)}")
print(f"bisect.bisect_left(a, 5, lo=2): {bisect.bisect_left(a, 5, lo=2)}")


matrix1 = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30],
]
target1 = 13
