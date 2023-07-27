from collections import defaultdict
from typing import List


class Solution:
    def find_itinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for departure, arrival in sorted(tickets, reverse=True):
            graph[departure].append(arrival)

        results = []

        def dfs(v):
            while graph[v]:
                dfs(graph[v].pop())

            results.append(v)

        dfs("JFK")
        return results[::-1]


if __name__ == "__main__":
    q = Solution()

    tickets1 = [
        ["MUC", "LHR"],
        ["JFK", "MUC"],
        ["SFO", "SJC"],
        ["LHR", "SFO"],
    ]

    tickets2 = [
        ["JFK", "SFO"],
        ["JFK", "ATL"],
        ["SFO", "ATL"],
        ["ATL", "JFK"],
        ["ATL", "SFO"],
    ]

    tickets3 = [
        ["JFK", "KUL"],
        ["JFK", "NRT"],
        ["NRT", "JFK"],
    ]

    print(q.find_itinerary(tickets1))
    print(q.find_itinerary(tickets2))
    print(q.find_itinerary(tickets3))
