BOARD_SIZE = 9
MIN_NUMBER = 1
MAX_NUMBER = 9
BOX_SIZE = 3


class Sudoku:

    def __init__(
            self,
            table,
    ) -> None:
        self.table = table

    def run(self):
        if self.solve(0, 0):
            self.show_solution()

        else:
            print("There is no solution.")

    def solve(self, row, col):
        """ 한 행을 다 보고 아래 열로 내려가면서 푼다.
        """
        # 재귀 시 가장 완벽한 케이스
        if row == BOARD_SIZE:
            # 다음 행을 보자.
            col += 1

            # 한 행을 다 봤다.
            if col == BOARD_SIZE:
                return True
            else:
                # 다음 열의 맨 처음으로 돌아간다.
                row = 0

        # 이미 있는 값은 안 살펴본다.
        if self.table[row][col] != 0:
            return self.solve(row + 1, col)

        # 아래 케이스를 살펴본다.
        for num in range(MIN_NUMBER, MAX_NUMBER + 1):
            if self.is_valid(row, col, num):
                # 숫자를 대입한다.
                self.table[row][col] = num

                if self.solve(row + 1, col):
                    return True

                # 백트래킹 : 다시 0으로 돌린다
                self.table[row][col] = 0

        # 다 해봐도 해답을 못찾으면
        return False

    def is_valid(self, row, col, num):
        # 컬럼안에 숫자가 있으면 답이될 수 없다.
        for i in range(BOARD_SIZE):
            if self.table[i][col] == num:
                return False

        # row 안도 마찬가지.
        for j in range(BOARD_SIZE):
            if self.table[row][j] == num:
                return False

        # 3*3 박스 안의 값도 같으면 안됨. (변수 선언)
        box_row_offset = (row // 3) * BOX_SIZE
        box_col_offset = (col // 3) * BOX_SIZE

        # 3*3 박스 안의 값도 같으면 안됨. (로직)
        for i in range(BOX_SIZE):
            for j in range(BOX_SIZE):
                if self.table[box_row_offset + i][box_col_offset + j] == num:
                    return False

        return True

    def show_solution(self):
        print('\n'.join(str(i) for i in self.table))


if __name__ == "__main__":
    # 0 값은 빈 값이라고 가정하자.
    sudoku = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
              [5, 2, 0, 0, 0, 0, 0, 0, 0],
              [0, 8, 7, 0, 0, 0, 0, 3, 1],
              [0, 0, 3, 0, 1, 0, 0, 8, 0],
              [9, 0, 0, 8, 6, 3, 0, 0, 5],
              [0, 5, 0, 0, 9, 0, 6, 0, 0],
              [1, 3, 0, 0, 0, 0, 2, 5, 0],
              [0, 0, 0, 0, 0, 0, 0, 7, 4],
              [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    algorithm = Sudoku(table=sudoku)
    algorithm.run()
