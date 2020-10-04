class MissionariesAndCannibalsID:
  def __init__(self):
    # 3 missionaries and 3 cannibals on the left side of
    # the river along with the boat.
    self.state = (3, 3, True)
    self.solutionSteps = []

  def solve(self):
    limit = 0
    expanded = 0
    steps = []
    backup = self.state

    # The optimal solution, as stated in https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem,
    # is 11 steps long.
    while not self.solved() and limit <= 11:
      self.state = backup
      steps = self.depthLimitedSolve(limit)
      limit += 1

    self.solutionSteps = steps
  
  def depthLimitedSolve(self, limit):
    dfs_stack = list()
    expanded = {}
    steps = [(0, 0)]
    depth = 0

    # Starting state, prev boat ride (0 missionaries, 0 cannibals), depth 0
    dfs_stack.append((self.state, ((0, 0), ), 0))

    while True:
      if len(dfs_stack) == 0 or self.solved():
        return steps

      cur_node = dfs_stack.pop()
      self.state = cur_node[0]
      steps = cur_node[1]
      depth = cur_node[2]

      if (self.state in expanded and expanded[self.state] <= depth) \
        or not self.valid() or depth == limit:
        continue
      
      expanded[self.state] = depth

      successors = self.successors(steps, depth)
      dfs_stack.extend(successors)

  def successors(self, steps, depth):
    # One optimizing rule that we want to follow: do not reverse the previous boat ride
    res = []
    if steps[-1] != (1, 0): res.append((self.generateCandidate(1, 0), steps + ((1, 0), ), depth + 1))
    if steps[-1] != (0, 1): res.append((self.generateCandidate(0, 1), steps + ((0, 1), ), depth + 1))
    if steps[-1] != (1, 1): res.append((self.generateCandidate(1, 1), steps + ((1, 1), ), depth + 1))
    if steps[-1] != (2, 0): res.append((self.generateCandidate(2, 0), steps + ((2, 0), ), depth + 1))
    if steps[-1] != (0, 2): res.append((self.generateCandidate(0, 2), steps + ((0, 2), ), depth + 1))

    return res

  def generateCandidate(self, missionaries, cannibals):
    boat_is_in_left = self.state[2]

    if boat_is_in_left: # moving right
      return (self.state[0] - missionaries, self.state[1] - cannibals, False)
    else: # boat is in right, moving left
      return (self.state[0] + missionaries, self.state[1] + cannibals, True)

  def valid(self):
    if (self.state[0] > 0 and self.state[0] < self.state[1]):
      return False

    if (self.state[0] < 3 and self.state[0] > self.state[1]):
      return False

    if (self.state[0] < 0 or self.state[1] < 0):
      return False

    if (self.state[0] > 3 or self.state[1] > 3):
      return False

    return True
  
  def solved(self):
    return self.state == (0, 0, False)

def main():
  problem = MissionariesAndCannibalsID()
  problem.solve()

  print(f"Solved? {problem.solved()}")
  
  direction = "->"
  print(f"Solution steps:")
  for step in problem.solutionSteps[1:]:
    missionaries = f"{step[0]} missionaries " if step[0] > 0 else ""
    cannibals = f"{step[1]} cannibals " if step[1] > 0 else ""
    _and = "and " if cannibals and missionaries else ""
    print(f"{direction} {missionaries}{_and}{cannibals}")
    direction = "<-" if direction == "->" else "->"

main()