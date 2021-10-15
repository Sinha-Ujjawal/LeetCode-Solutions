from typing import List, Optional, Tuple

Interval = Tuple[int, int]


def merge_interval(intx: Interval, inty: Interval) -> Optional[Interval]:
    xs, xe = intx
    ys, ye = inty
    if xs <= ye and ys <= xe:
        return min(xs, ys), max(xe, ye)


class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals = sorted(map(tuple, intervals))
        ans = []
        for interval in intervals:
            if not ans:
                ans.append(interval)
            else:
                into = merge_interval(ans[-1], interval)
                if into:
                    ans[-1] = into
                else:
                    ans.append(interval)
        return ans


if __name__ == "__main__":
    solver = Solution()
    print(solver.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
