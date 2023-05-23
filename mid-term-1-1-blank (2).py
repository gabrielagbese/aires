from mt_utils import *

# solved
class NumberedMaze(Problem):
    def __init__(self):
        self.T = ((1, 5, 3, 4, 3, 6, 7, 1, 1, 6),
                  (4, 4, 3, 4, 2, 6, 2, 6, 2, 5),
                  (1, 3, 9, 4, 5, 2, 4, 2, 9, 5),
                  (5, 2, 3, 5, 5, 6, 4, 6, 2, 4),
                  (1, 3, 3, 2, 5, 6, 5, 2, 3, 2),
                  (2, 5, 2, 5, 5, 6, 4, 8, 6, 1),
                  (9, 2, 3, 6, 5, 6, 2, 2, 2, 0))

        # Call the parent constructor and initialize with the initial and goal state
        # Write your code below this line!
        initial_state = (0, 0)  # Set the initial state
        goal_state = (len(self.T) - 1, len(self.T[0]) - 1)  # Set the goal state
        super().__init__(initial_state, goal_state)
        # Write your code above this line!

    def actions(self, state):
        # Return all possible actions from the input state.
        # Write your code below this line!
        actions = []
        row, col = state

        # Check the validity of moving up, down, left, and right
        if row > 0:
            actions.append("up")
        if row < len(self.T) - 1:
            actions.append("down")
        if col > 0:
            actions.append("left")
        if col < len(self.T[0]) - 1:
            actions.append("right")

        return actions
        # Write your code above this line!

    def result(self, state, action):
        # Return the new state when using the given action in the input state.
        # Write your code below this line!
        row, col = state

        if action == "up":
            return row - 1, col
        elif action == "down":
            return row + 1, col
        elif action == "left":
            return row, col - 1
        elif action == "right":
            return row, col + 1

        # If the action is invalid, return the current state
        return state
        # Write your code above this line!


def breadth_first_graph_search(problem):
    # Perform a breadth-first search to find the goal state.
    # Write your code below this line!
    frontier = deque([Node(problem.initial)])  # Initialize the frontier with the initial state
    explored = set()  # Initialize the explored set

    while frontier:
        node = frontier.popleft()  # Choose the node from the frontier (FIFO)
        if problem.goal_test(node.state):  # Check if the goal has been reached
            return node.solution()
        explored.add(node.state)  # Add the node to the explored set

        # Expand the node and add the resulting nodes to the frontier
        for child_node in node.expand(problem):
            if child_node.state not in explored and child_node not in frontier:
                frontier.append(child_node)

    return None  # Return None if no solution is found
    # Write your code above this line!


def main():
    # 1. Exercise: Fill in the missing parts of init function and print out the initial state (1 point)
    # Write your code below this line!
    maze = NumberedMaze()
    print("Initial state:", maze.initial)
    # Write your code above this line!

    # 2. Exercise: Fill out the actions function and test if it works correctly (using the initial state) (3 points)
    # Write your code below this line!
    initial_state = maze.initial
    possible_actions = maze.actions(initial_state)
    print("Possible actions from the initial state:", possible_actions)
    # Write your code above this line!

    # 3. Exercise: Fill out the result function and test if it works correctly (3 points)
    # Write your code below this line!
    state = (0, 0)
    action = "right"
    new_state = maze.result(state, action)
    print(f"New state after taking action '{action}':", new_state)
    # Write your code above this line!

    # 4. Fill out the breadth_first_graph_search function and solve the problem using it (1.5 points)
    # Write your code below this line!
    solution = breadth_first_graph_search(maze)
    if solution:
        print("Solution:", solution)
    else:
        print("No solution found.")
    # Write your code above this line!


if __name__ == '__main__':
    main()
