class Puzzle:
    def __init__(self, board, goal):
        self.board = board
        self.goal = goal
        self.blank_index = self.board.index('_')  # Find the index of the empty tile ('_')

    def is_goal(self):
        return self.board == self.goal

    def get_moves(self):
        """Generate possible moves"""
        moves = []
        row, col = divmod(self.blank_index, 3)
        if row > 0:  # Move the blank up
            moves.append(self.swap(self.blank_index, self.blank_index - 3))
        if row < 2:  # Move the blank down
            moves.append(self.swap(self.blank_index, self.blank_index + 3))
        if col > 0:  # Move the blank left
            moves.append(self.swap(self.blank_index, self.blank_index - 1))
        if col < 2:  # Move the blank right
            moves.append(self.swap(self.blank_index, self.blank_index + 1))
        return moves

    def swap(self, i, j):
        """Swap two positions"""
        new_board = self.board[:]
        new_board[i], new_board[j] = new_board[j], new_board[i]
        return new_board

    def manhattan_distance(self):
        """Calculate the total Manhattan distance of the tiles from their goal positions"""
        distance = 0
        for i, val in enumerate(self.board):
            if val != '_':
                target_pos = self.goal.index(val)
                current_row, current_col = divmod(i, 3)
                target_row, target_col = divmod(target_pos, 3)
                distance += abs(current_row - target_row) + abs(current_col - target_col)
        return distance

    def solve(self):
        from heapq import heappush, heappop
        open_list = []
        heappush(open_list, (self.manhattan_distance(), self.board))
        came_from = {tuple(self.board): None}
        cost_so_far = {tuple(self.board): 0}

        while open_list:
            _, current = heappop(open_list)
            current_puzzle = Puzzle(current, self.goal)

            if current_puzzle.is_goal():
                return self.reconstruct_path(came_from, tuple(current))

            for next_state in current_puzzle.get_moves():
                new_cost = cost_so_far[tuple(current)] + 1
                if tuple(next_state) not in cost_so_far or new_cost < cost_so_far[tuple(next_state)]:
                    cost_so_far[tuple(next_state)] = new_cost
                    priority = new_cost + Puzzle(next_state, self.goal).manhattan_distance()
                    heappush(open_list, (priority, next_state))
                    came_from[tuple(next_state)] = tuple(current)

        return None

    def reconstruct_path(self, came_from, current):
        """Reconstruct the path to the goal"""
        path = []
        while current:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path

def read_board(prompt):
    print(prompt)
    return input().split()

def print_matrix(board):
    """Print the board in a 3x3 matrix format"""
    for i in range(0, 9, 3):
        print(board[i:i+3])
    print()  # Add a newline for better separation between steps

# Read initial and goal states from user
initial_state = read_board("Enter the initial state (e.g., 1 2 3 4 5 6 _ 7 8):")
goal_state = read_board("Enter the goal state (e.g., 1 2 3 4 5 6 7 8 _):")

# Solve the puzzle
puzzle = Puzzle(initial_state, goal_state)
solution = puzzle.solve()

if solution:
    for step in solution:
        print_matrix(step)
else:
    print("No solution found.")
