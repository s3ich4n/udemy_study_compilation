class Solution:
    def __init__(self, data) -> None:
        self.data = data

    def partition(self, lo, hi):
        pivot = self.data[hi]
        i = lo

        for j in range(lo, hi):
            if self.data[j] < pivot:
                self.data[i], self.data[j] = self.data[j], self.data[i]
                i += 1

        self.data[i], self.data[hi] = self.data[hi], self.data[i]
        return i

    def quicksort(self, lo, hi):
        if lo < hi:
            pivot = self.partition(lo, hi)
            self.quicksort(lo, pivot - 1)
            self.quicksort(pivot + 1, hi)

    def sort(self):
        self.quicksort(0, len(self.data) - 1)


test = [2, 8, 7, 1, 3, 5, 6, 4]

s = Solution(test)
s.sort()
print(s.data)
