# Q = [
#     [".", ".", ".", "."],
#     [".", ".", ".", "."],
#     [".", ".", ".", "."],
#     [".", ".", ".", "."],
# ]
#
# # # y = 1
# # # x_size = (x for x in range(4))
# #
# # x_size = (x for x in range(4))
# # y_size = (y for y in range(4))
# #
# # if x, y in zip(x_size, y_size):
# #     print(x, y)
# #
# # triggered = False
# #
# # for x in x_size:
# #     if Q[x][y] == "Q":
# #         triggered = True
# #         print(f"Q detected. Q[{x}][{y}]")
# #     else:
# #         print(f"Q not detected Q[{x}][{y}]")
# #
# # if triggered:
# #     Q[x][y] = "!"
# # else:
# #     Q[x][y] = "Q"
# #
# # a = 1
# #
# #
# #
#
#
# def print_current_tile(tiles):
#     for tile_x in tiles:
#         for tile_y in tile_x:
#             print(f"{tile_y:2}", end="")
#         print("")
#
#
# def discriminate(Q, x, y) -> bool:
#     print(f"{x}, {y} 판별 시작.")
#     print_current_tile(Q)
#     triggered = False
#
#     # x 좌표가 겹치는가? (0, 0), (1, 0), (2, 0), ... (n, 0)
#     x_size = (x for x in range(x))
#     for _x in x_size:
#         if Q[_x][y] == "Q":
#             Q[_x][y] = "."
#             triggered = True
#             break
#
#     # y 좌표가 겹치는가? (0, 0), (0, 1), (0, 2), ... (0, n)
#     y_size = (y for y in range(y))
#     for _y in y_size:
#         if Q[x][_y] == "Q":
#             Q[x][_y] = "."
#             triggered = True
#             break
#
#     # x, y를 -1 계속하면서 둘 중 하나가 0값이 되면?
#     # abs(x2-x1) == abs(y2-y1) 이면?
#     x_size, y_size = x, y
#     while x_size > 0 and y_size > 0:
#         if abs(x - x_size) == abs(y - y_size):
#             Q[x_size][y_size] = "."
#             triggered = True
#             break
#
#     if triggered:
#         print(f"\n[제거됨] {x}, {y} 판별 끝.")
#         print_current_tile(Q)
#         return False
#     else:
#         Q[x][y] = "Q"
#         print(f"\n[추가됨] {x}, {y} 판별 끝.")
#         print_current_tile(Q)
#         return True
#
#
# x = 0
# y = 0
#
#
# def iterative(Q, x, y):
#     while x < 4 and y < 4:
#         if y < 4:
#             if discriminate(Q, x, y):
#                 x += 1
#                 y = 0
#             else:
#                 x -= 1
#                 y += 1
#                 # iterative(Q, x, y)
#
#
# iterative(Q, 0, 0)


import collections


tile = collections.defaultdict(int)


n = 4


for x in range(0, 2):
    for y in range(0, 2):
        if tile[x] == -1:
            tile[x] = y

        if tile[x] == y or tile[y] == x:
            tile[x] = -1

        else:
            tile[x] = y
