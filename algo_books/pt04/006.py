from collections import defaultdict
from typing import List


class Solution:
    def course_schedule(
            self,
            num_of_courses: int,
            prerequisites: List[int],
    ) -> bool:
        graph = defaultdict(list)
        for departure, arrival in prerequisites:
            graph[departure].append(arrival)

        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False

            if i in visited:
                return True

            traced.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False

            # 갔다온 이력을 지워야함
            # 다른 참조때도 써먹을 수 있게 해야함
            traced.remove(i)
            visited.add(i)

            return True

        for x in list(graph.keys()):
            if not dfs(x):
                return False

        return True


if __name__ == "__main__":
    q = Solution()

    # print(q.course_schedule(
    #     num_of_courses=2,
    #     prerequisites=[[1, 0]],
    # ))

    # print(q.course_schedule(
    #     num_of_courses=2,
    #     prerequisites=[[1, 0], [0, 1]],
    # ))

    # print(q.course_schedule(
    #     num_of_courses=3,
    #     prerequisites=[[0, 1], [0, 2], [1, 2]],
    # ))

    print(q.course_schedule(
        num_of_courses=100,
        prerequisites=[[1,0],[2,0],[2,1],[3,1],[3,2],[4,2],[4,3],[5,3],[5,4],[6,4],[6,5]],
    ))
