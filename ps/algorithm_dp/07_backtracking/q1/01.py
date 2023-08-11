class HamiltonianProblem:

    def __init__(self, adjacency_matrix) -> None:
        self.n = len(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
        self.path = [0]  # 처음부터 시작함

    def hamiltonian_cycle(self):

        if self.solve(1):
            self.show_hamiltonian_cycle()

        else:
            print("there is no solution to the problem...")

    # vertex의 인덱스
    def solve(self, position):

        # 베스트케이스
        if position == self.n:
            for idx in range(0, self.n):
                if self.is_cycle_available(idx, position):
                    self.path.append(idx)
                    return True

            return False

        for vertex_index in range(1, self.n):
            if self.is_feasible(vertex_index, position):
                # 쫓아갈 경로에 추가?
                self.path.append(vertex_index)

                if self.solve(position + 1):
                    return True

                # 백트래킹 할 필요가 있으면
                # vertex 인덱스를 path 에서 뺀다
                self.path.pop()

        # 못찾으면 False
        return False

    def is_feasible(self, vertex, actual_position):

        # 노드간 연결이 끊어지는 순간.. False
        if self.adjacency_matrix[self.path[actual_position-1]][vertex] == 0:
            return False

        # 이미 순회한 경우에도?
        for i in range(actual_position):
            if self.path[i] == vertex:
                return False

        return True

    def is_cycle_available(self, vertex, actual_position):
        for i in range(actual_position):
            if self.path[i] == vertex:
                return True

    def show_hamiltonian_cycle(self):
        # for v in self.path:
        #     print(v)
        return self.path


if __name__ == "__main__":

    # this is a small example
    m = [[0, 1, 1],
         [1, 0, 1],
         [1, 1, 0]]

    hamiltonian = HamiltonianProblem(m)
    a = hamiltonian.hamiltonian_cycle()
