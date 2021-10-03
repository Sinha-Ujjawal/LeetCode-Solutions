from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ans = [None] * (m + n)
        i = j = c = 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                ans[c] = nums1[i]
                i += 1
            else:
                ans[c] = nums2[j]
                j += 1
            c += 1

        while i < m:
            ans[c] = nums1[i]
            i += 1
            c += 1

        while j < n:
            ans[c] = nums2[j]
            j += 1
            c += 1

        for i in range(m + n):
            nums1[i] = ans[i]


class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solver = Solution()
    solver.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solver2 = Solution2()
    solver2.merge(nums1, m, nums2, n)
    print(nums1)
