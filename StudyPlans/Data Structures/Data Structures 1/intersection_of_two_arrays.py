from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        return [k for k in c1 if k in c2 for _ in range(min(c1[k], c2[k]))]


class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = sorted(nums1), sorted(nums2)
        i = j = 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            n1, n2 = nums1[i], nums2[j]
            if n1 == n2:
                ans.append(n1)
                i += 1
                j += 1
            elif n1 > n2:
                j += 1
            else:
                i += 1
        return ans


if __name__ == "__main__":
    solver = Solution()
    solver2 = Solution2()
    nums1 = [1, 2, 2, 1, 2]
    nums2 = [2, 2]
    print(solver.intersect(nums1=nums1, nums2=nums2))
    print(solver2.intersect(nums1=nums1, nums2=nums2))
