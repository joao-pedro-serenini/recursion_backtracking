class RodCutting:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.s = [[0]*(n+1) for _ in range(len(p))]
    
    def solve(self):

        for i in range(1, len(self.p)):
            for j in range(self.n+1):
                if i <= j:
                    self.s[i][j] = max(self.s[i-1][j], self.p[i]+self.s[i][j-i])
                else:
                    self.s[i][j] = self.s[i-1][j]

    def show_results(self):
        print("Max profit: %d" % self.s[len(self.p)-1][self.n])

        col_index = self.n
        row_index = len(self.p)-1

        while (col_index > 0) or (row_index > 0):
            # we have to compare the items right above each other
            # if they are the same value then the given row (piece) is not in the solution
            if self.s[row_index][col_index] == self.s[row_index - 1][col_index]:
                row_index = row_index - 1
            else:
                print("We make cut: ", row_index, "m")
                col_index = col_index - row_index

if __name__ == '__main__':

    problem = RodCutting(5, [0, 2, 5, 7, 3, 9])
    problem.solve()
    problem.show_results()

