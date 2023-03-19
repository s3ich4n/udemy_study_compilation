class QueensProblem:

    def __init__(self, n) -> None:
        self.n = n
        self.chess_table = [
            [None for i in range(n)]
            for j in range(n)
        ]

    def solve_n_queens(self):
        # 0번 인덱스부터 시작!
        if self.solve(0):
            self.print_queens()
        else:
            # 한 케이스도 못 찾으면 못한거
            print('the is no feasible solution.')

    # col_index는
    # 퀸의 인덱스와 같은 값이다
    def solve(self, col_index):

        # 문제를 찾은 경우
        if col_index == self.n:
            return True

        # 퀸의 올바른 포지션을 찾아보자
        for row_index in range(self.n):
            if self.is_place_valid(row_index, col_index):
                # 1은 queen이 있다는 얘기
                self.chess_table[row_index][col_index] = 1

                # 또 불러서 다음 컬럼의 퀸 위치를 찾아본다
                if self.solve(col_index + 1):
                    return True

                # 백트래킹!
                print("BACKTRACKING!!")
                self.chess_table[row_index][col_index] = 0

        # 특정 행의 열을 다 뒤졌을 때 안나오면 백트래킹하게 False를 리턴함
        return False

    def is_place_valid(self, row_index, col_index):

        # 1. 직선순회
        #   퀸이 서로를 공격할 수 있는지 row를 점검한다.
        #
        for i in range(self.n):
            if self.chess_table[row_index][i] == 1:
                return False

        #
        # 2. 대각선 순회
        #

        # 0까지 역순회
        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break

            if self.chess_table[i][j] == 1:
                return False

            j = j - 1

        # 0까지 역순회
        j = col_index
        for i in range(row_index, self.n):
            if j < 0:
                break

            if self.chess_table[i][j] == 1:
                return False

            j = j - 1

        return True

    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print(' Q ', end="")
                else:
                    print(' - ', end="")
            print("\n")


if __name__ == "__main__":
    queens = QueensProblem(20)
    queens.solve_n_queens()
