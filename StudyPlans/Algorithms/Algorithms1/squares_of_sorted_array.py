from typing import Callable, List, Iterable, Any, Tuple


def parititon(
    xs: Iterable[Any], predicate: Callable[[Any], bool]
) -> Tuple[List[Any], List[Any]]:
    left = []
    right = []
    for x in xs:
        if predicate(x):
            left.append(x)
        else:
            right.append(x)
    return left, right


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negatives, positives = parititon(nums, predicate=lambda x: x < 0)
        negatives = negatives[::-1]

        def square_inplace(xs: List[int]):
            for i in range(len(xs)):
                xs[i] *= xs[i]

        def merge(xs: List[int], ys: List[int]) -> List[int]:
            res = [None] * (len(xs) + len(ys))
            i = j = c = 0
            while i < len(xs) and j < len(ys):
                if xs[i] < ys[j]:
                    res[c] = xs[i]
                    i += 1
                else:
                    res[c] = ys[j]
                    j += 1
                c += 1

            while i < len(xs):
                res[c] = xs[i]
                c += 1
                i += 1

            while j < len(ys):
                res[c] = ys[j]
                c += 1
                j += 1

            return res

        square_inplace(negatives)
        square_inplace(positives)

        return merge(positives, negatives)


if __name__ == "__main__":
    solver = Solution()
    print(solver.sortedSquares([-4, -1, 0, 3, 10]))
    print(solver.sortedSquares([-7, -3, 2, 3, 11]))
