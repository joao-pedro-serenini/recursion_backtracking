class MazeProblem:

    def __init__(self, mazeTable):
        self.mazeTable = mazeTable
        self.mazeSize = len(mazeTable)
        self.solutionTable = [[0]*self.mazeSize for x in range(self.mazeSize)]
    
    def solveMaze(self):

        if self.solve(0, 0):
            self.showResult()
        else:
            print("No feasible solution has found ...")
    
    def solve(self, x, y):
        if self.isFinished(x, y):
            return True
        
        if self.isValid(x, y):
            # it is valid so it is part of the solution
            self.solutionTable[x][y] = 1
        
            if self.solve(x+1, y):
                # go foward in direction x
                return True
            
            # if self.solve(x-1, y):
            #     # go left in direction x
            #     return True
        
            if self.solve(x, y+1):
                # go foward in direction y
                return True
            
            # if self.solve(x, y-1):
            #     # go up in direction y
            #     return True
        
            # no feaseble solution: bactrack
            self.solutionTable[x][y] = 0

        return False

    def isFinished(self, x, y):

        if x == self.mazeSize-1 and y == self.mazeSize-1:
            self.solutionTable[x][y] = 1
            return True
        return False
    
    def isValid(self, x, y):
        if x < 0 or x >= self.mazeSize: return False
        if y < 0 or y >= self.mazeSize: return False
        if self.mazeTable[x][y] == 0: return False

        return True

    def showResult(self):

        for i in range(self.mazeSize):
            for j in range(self.mazeSize):
                if self.solutionTable[i][j] == 1:
                    print(" S ", end=""),
                else:
                    print(" - ", end=""),
            print("\n")

if __name__ == '__main__':
    mazeTable = [[1, 1, 1, 1, 1],
                 [1, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0],
                 [1, 1, 1, 1, 1], 
                 [1, 1, 1, 0, 1]]

    mazeProblem = MazeProblem(mazeTable)
    mazeProblem.solveMaze()