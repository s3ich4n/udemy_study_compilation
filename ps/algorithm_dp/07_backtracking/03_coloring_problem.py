class ColoringProblem:

    def __init__(
            self,
            adjacency_matrix,
            num_colors,
    ) -> None:
        self.n = len(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
        self.num_colors = num_colors
        self.colors = [0 for _ in range(self.n)]

    def coloring_problem(self):

        # 0 번 인덱스 부터 문제풀이 시작
        if self.solve(0):
            self.show_result()
        else:
            print("no feasible solution")

    def solve(self, node_index):

        if node_index == self.n:
            return True

        # 색상 + 1 만큼 체크해보자.
        for color_index in range(1, self.num_colors + 1):
            if self.is_color_valid(node_index, color_index):
                self.colors[node_index] = color_index

                if self.solve(node_index + 1):
                    return True

                # 백트래킹!!!
                # 다음 순회를 하면 되니까, 백트래킹하는 것은 "아무것도 안 하는" 것이다.

        return False

    def is_color_valid(self, node_index, color_index):
        # 노드들이 연결되어있고, 근처 노드들의 색상이 공유되어 있는지 확인.
        for i in range(self.n):
            if self.adjacency_matrix[node_index][i] == 1 and color_index == self.colors[i]:
                return False

        return True

    def show_result(self):
        for v, c in zip(range(self.n), self.colors):
            print(f"Node {v} has color valud {c}")


if __name__ == "__main__":

    # 그래프 연결을 의미.
    m = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]

    problem = ColoringProblem(m, 3)
    problem.coloring_problem()
