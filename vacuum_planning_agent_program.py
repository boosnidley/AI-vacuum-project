from search import Problem, Node, SimpleProblemSolvingAgentProgram, astar_search


class VacuumProblem(Problem):
    def __init__(self, initial, width, height, goal=None):
        super().__init__(initial, goal)
        self.width = width
        self.height = height

    def actions(self, state):
        cur_loc = state['agent']
        acts = ['Suck']
        left = (cur_loc[0]-1, cur_loc[1])
        right = (cur_loc[0]+1, cur_loc[1])
        up = (cur_loc[0]-1, cur_loc[1])
        down = (cur_loc[0]+1, cur_loc[1])
        if left not in state['obstacles'] and self.is_inbounds(left):
            acts.append('Left')
        if right not in state['obstacles'] and self.is_inbounds(right):
            acts.append('Right')
        if up not in state['obstacles'] and self.is_inbounds(up):
            acts.append('Up')
        if down not in state['obstacles'] and self.is_inbounds(down):
            acts.append('Down')

        return acts

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError

    def goal_test(self, state):


    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2. If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def is_inbounds(self, loc):
        """Check if loc is inside the walls"""
        x, y = loc
        return 0 < x < self.height - 1 and 0 < y < self.width - 1


class VacuumPlanningAgentProgram(SimpleProblemSolvingAgentProgram):
    def __init__(self, initial_state=None):
        """State is an abstract representation of the state
        of the world, and seq is the list of actions required
        to get to a particular state from the initial state(root)."""
        self.state = initial_state
        self.seq = []

    def __call__(self, percept):
        """[Figure 3.1] Formulate a goal and problem, then
        search for a sequence of actions to solve it."""
        self.state = self.update_state(self.state, percept)
        if not self.seq:
            goal = self.formulate_goal(self.state)
            problem = self.formulate_problem(self.state, goal)
            self.seq = self.search(problem)
            if not self.seq:
                return None
        return self.seq.pop(0)

    def update_state(self, state, percept):
        # Replace our stored state with the new one
        self.state = percept

    def formulate_goal(self, state):
        return None

    def formulate_problem(self, state, goal):
        return VacuumGridProblem(self.state)

    def search(self, problem):
        return astar_search(problem, lambda n: 2*len(n.state['dirts']))
