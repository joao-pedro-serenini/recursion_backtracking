# m - capacity of the knapsack, w - weights list, v - values list, n - number of items we consider
def solve_recursion(self, m, w, v, n):
 
    # base case(s)
    if (n==0) or (m==0):
        return 0
    
    # the given item can NOT fit into the knapsack
    if w[n - 1] > m:
        return self.solve_recursion(m, w, v, n-1)
    else:
        # given item can fit into the knapsack so we have 2 options (include, exclude)
        n_include = v[n-1] + self.solve_recursion(m - w[n-1], w, v, n-1)
        n_exclude = self.solve_recursion(m, w, v, n-1)

        return max(n_include, n_exclude)
    
class KnapsackProblem:

    def __init__(self, n, M, w, v):
        self.n = n
        self.M = M
        self.w = w
        self.v = v
        self.S = [[0 for _ in range(M+1)] for _ in range(n+1)]
    
    def solve(self):
        # construct the S dynamic programming table
        for i in range(self.n+1):
            for w in range(self.M+1):
                not_taking_item = self.S[i - 1][w]
                taking_item = 0

                if self.w[i] <= w:
                    taking_item = self.v[i] + self.S[i - 1][w - self.w[i]]
                
                # memoization - we store the sub-results to avoid recalculate
                self.S[i][w] = max(not_taking_item, taking_item)
    
    def show_result(self):

        print("Total benefit: %d" % self.S[self.n][self.M])

        w = self.M
        for n in range(self.n, 0, -1):
            if self.S[n][w] != 0 and self.S[n][w] != self.S[n - 1][w]:
                print("We take item #%d" % n)
                w = w - self.w[n]

if __name__ == '__main__':
    num_of_items = 4
    knapsack_capacity = 7
    weights = [0, 1, 3, 4, 5]
    profits = [0, 1, 4, 5, 7]
    knapsack = KnapsackProblem(num_of_items, knapsack_capacity, weights, profits)
    knapsack.solve()
    knapsack.show_result()