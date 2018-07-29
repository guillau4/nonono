from enum import Enum


class Case(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class Board:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.board = [[Case.EMPTY for x in range(w)] for y in range(h)]
        self.rows = [[] for y in range(h)]
        self.columns = [[] for x in range(w)]

    def iscorrect(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.board[i][j] == Case.EMPTY:
                    return False
        for i in range(self.width):
            if not self.checkcol(i):
                return False
        for j in range(self.height):
            if not self.checkrow(j):
                return False
        return True

    def checkrow(self, r):
        build = []
        consecutive = 0
        for i in range(self.width):
            case = self.board[i][r]
            if case == Case.EMPTY:
                return False
            if case == Case.BLACK:
                consecutive += 1
            elif consecutive != 0:
                build.append(consecutive)
                consecutive = 0
        if consecutive != 0:
            build.append(consecutive)
        return build == self.rows[r]

    def checkcol(self, c):
        build = []
        consecutive = 0
        for j in range(self.height):
            case = self.board[c][j]
            if case == Case.EMPTY:
                return False
            if case == Case.BLACK:
                consecutive += 1
            elif consecutive != 0:
                build.append(consecutive)
                consecutive = 0
        if consecutive != 0:
            build.append(consecutive)
        return build == self.columns[c]
