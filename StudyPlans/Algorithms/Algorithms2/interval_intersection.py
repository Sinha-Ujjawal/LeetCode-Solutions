from typing import List, Optional, Tuple

Interval = Tuple[int, int]


def overlap(intx: Interval, inty: Interval) -> Optional[Interval]:
    xs, xe = intx
    ys, ye = inty
    if xs <= ye and ys <= xe:
        return max(xs, ys), min(xe, ye)


class Solution:
    def intervalIntersection(
        self,
        firstList: List[Interval],
        secondList: List[Interval],
    ) -> List[Interval]:
        ans = []
        j = 0
        secondList.append((float("inf"), float("inf")))
        for i in range(len(firstList)):
            flag = False
            while j < len(secondList):
                intx, inty = map(tuple, [firstList[i], secondList[j]])
                into = overlap(intx, inty)
                if into:
                    ans.append(into)
                    flag = True
                elif flag:
                    j -= 1
                    break
                elif intx < inty:
                    break
                j += 1
        return ans


if __name__ == "__main__":
    solver = Solution()
    print(
        solver.intervalIntersection(
            firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
            secondList=[[1, 5], [8, 12], [15, 24], [25, 26]],
        )
    )
    print(solver.intervalIntersection(firstList=[[1, 7]], secondList=[[3, 10]]))
    print(
        solver.intervalIntersection(
            firstList=[[4, 6], [7, 8], [10, 17]],
            secondList=[[5, 10]],
        )
    )
    print(
        solver.intervalIntersection(
            firstList=[[0, 5], [12, 14], [15, 18]],
            secondList=[[11, 15], [18, 19]],
        )
    )
