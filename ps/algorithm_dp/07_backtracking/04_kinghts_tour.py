class KnightsTous:

    def __init__(
            self,
            board_size: int,
    ) -> None:
        self.board_size = board_size

        # x축, y축으로 움직이는 케이스를 배열로.
        self.x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
        self.y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

        self.solution_matrix = [
            [-1 for _ in range(self.board_size)]
            for _ in range(self.board_size)
        ]

    def solve_problem(self):

        # 좌상단부터 시작.
        self.solution_matrix[0][0] = 0

        # 첫 파라미터가 카운터다.
        # 2, 3번째 파라미터는 좌표다.
        if self.solve(1, 0, 0):
            self.print_solution()

        else:
            print("There is no feasible solution...")

    def solve(self, step_counter, x, y):

        # 카운터가 끝에 도달하면 끝난 것.
        if step_counter == self.board_size * self.board_size:
            return True

        # 가능한 모든 움직임을 체크한다.
        for move_index in range(len(self.x_moves)):

            next_x = x + self.x_moves[move_index]
            next_y = y + self.y_moves[move_index]

            if self.is_valid_move(next_x, next_y):
                # 제대로 된 스텝이므로 solution_matrix를 업데이트 한다.
                self.solution_matrix[next_x][next_y] = step_counter

                if self.solve(step_counter + 1, next_x, next_y):
                    return True

                # 안되면 백트래킹.
                self.solution_matrix[next_x][next_y] = -1

        return False

    def is_valid_move(self, x, y):
        # 체스보드 밖으로 나가는 움직임인지 체크 (가로)
        if x < 0 or x >= self.board_size:
            return False

        # 체스보드 밖으로 나가는 움직임인지 체크 (세로)
        if y < 0 or y >= self.board_size:
            return False

        # 혹시 값이 들어가있는지 점검
        if self.solution_matrix[x][y] > -1:
            return False

        return True

    def print_solution(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                print(f"{self.solution_matrix[i][j]:3}", end=" ")

            print("\n")


if __name__ == "__main__":
    tour = KnightsTous(8)
    tour.solve_problem()
