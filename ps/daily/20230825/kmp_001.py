# from typing import List


# TEST = "abxab"
# # TEST = "abxabaxa"
# # TEST = "abxaa"
# lps = [0 for _ in range(len(TEST))]


# def compute_lps(
#         subject: str,
#         lps: List[int],
# ) -> List[int]:
#     """
#     lps 배열을 가지고온다
#     """
#     # left: 좌측값, right: 우측값
#     left, right = 0, 1

#     while right < len(subject):
#         if subject[right] == subject[left]:
#             left += 1
#             lps[right] = left
#             right += 1

#         else:
#             if left != 0:
#                 left = lps[left - 1]
#             else:
#                 lps[right] = 0
#                 right += 1


# compute_lps(TEST, lps)

# print(f"TEST lps: {lps}")
# a = 1
