class EightPuzzleID:
  def __init__(self, input_tiles):
    input_tiles = input_tiles.split(" ")
    for i in range(len(input_tiles)):
      input_tiles[i] = int(input_tiles[i])

    self.state = input_tiles
    self.solutionSteps = []

  def solve(self):
    limit = 1
    expanded = 0
    steps = ""
    backup = self.state

    while not self.solved() and expanded < 1000000:
      self.state = backup
      expanded, steps = self.depthLimitedSolve(limit)
      limit += 1

    if expanded >= 1000000:
      print(f"More than 1000000 nodes expanded and solution not found.")
    else:
      self.solutionSteps = steps

  # Return values: exp_count, dfs_stack
  def depthLimitedSolve(self, limit):
    depth = 0
    dfs_stack = list()
    expanded = 0
    steps = "S"

    dfs_stack.append([self.state, "S", 0])

    while True:
      if len(dfs_stack) == 0 or self.solved() or expanded > 1000000:
        return (expanded, steps)

      cur_node = dfs_stack.pop()
      self.state = cur_node[0]
      steps = cur_node[1]
      depth = cur_node[2]
      expanded += 1

      if depth == limit:
        continue

      successors = self.successors(steps, depth)
      dfs_stack.extend(successors)

  def successors(self, steps, depth):
    zero_index = self.state.index(0)

    # Zero is the middle tile
    if (zero_index == 4):
      res = []
      if steps[-1] != "D": res.append([self.moveUpCandidate(zero_index), steps + 'U', depth + 1])
      if steps[-1] != "U": res.append([self.moveDownCandidate(zero_index), steps + 'D', depth + 1])
      if steps[-1] != "R": res.append([self.moveLeftCandidate(zero_index), steps + 'L', depth + 1])
      if steps[-1] != "L": res.append([self.moveRightCandidate(zero_index), steps + 'R', depth + 1])

      return res

    # Zero is the top left tile
    elif (zero_index == 0):
      res = []
      if steps[-1] != "U": res.append([self.moveDownCandidate(zero_index), steps + 'D', depth + 1])
      if steps[-1] != "L": res.append([self.moveRightCandidate(zero_index), steps + 'R', depth + 1])
      
      return res
    
    # Zero is the top right tile
    elif (zero_index == 2):
      res = []
      if steps[-1] != "U": res.append([self.moveDownCandidate(zero_index), steps + 'D', depth + 1])
      if steps[-1] != "R": res.append([self.moveLeftCandidate(zero_index), steps + 'L', depth + 1])

      return res

    # Zero is the bottom left tile
    elif (zero_index == 6):
      res = []
      if steps[-1] != "D": res.append([self.moveUpCandidate(zero_index), steps + 'U', depth + 1])
      if steps[-1] != "L": res.append([self.moveRightCandidate(zero_index), steps + 'R', depth + 1])

      return res

    # Zero is the bottom right tile
    elif (zero_index == 8):
      res = []
      if steps[-1] != "D": res.append([self.moveUpCandidate(zero_index), steps + 'U', depth + 1])
      if steps[-1] != "R": res.append([self.moveLeftCandidate(zero_index), steps + 'L', depth + 1])

      return res

    # Zero is the top middle tile:
    elif (zero_index == 1):
      res = []
      if steps[-1] != "U": res.append([self.moveDownCandidate(zero_index), steps + 'D', depth + 1])
      if steps[-1] != "R": res.append([self.moveLeftCandidate(zero_index), steps + 'L', depth + 1])
      if steps[-1] != "L": res.append([self.moveRightCandidate(zero_index), steps + 'R', depth + 1])

      return res
    
    # Zero is the middle left tile:
    elif (zero_index == 3):
      res = []
      if steps[-1] != "D": res.append([self.moveUpCandidate(zero_index), steps + 'U', depth + 1])
      if steps[-1] != "U": res.append([self.moveDownCandidate(zero_index), steps + 'D', depth + 1])
      if steps[-1] != "L": res.append([self.moveRightCandidate(zero_index), steps + 'R', depth + 1])

      return res

    # Zero is the middle right tile:
    elif (zero_index == 5):
      res = []
      if steps[-1] != "D": res.append([self.moveUpCandidate(zero_index), steps + 'U', depth + 1])
      if steps[-1] != "U": res.append([self.moveDownCandidate(zero_index), steps + 'D', depth + 1])
      if steps[-1] != "R": res.append([self.moveLeftCandidate(zero_index), steps + 'L', depth + 1])

      return res

    # Zero is the bottom middle tile:
    else:
      res = []
      if steps[-1] != "D": res.append([self.moveUpCandidate(zero_index), steps + 'U', depth + 1])
      if steps[-1] != "R": res.append([self.moveLeftCandidate(zero_index), steps + 'L', depth + 1])
      if steps[-1] != "L": res.append([self.moveRightCandidate(zero_index), steps + 'R', depth + 1])

    return res
    
  def moveLeftCandidate(self, z_i):
    candidate = self.state[:]
    candidate[z_i], candidate[z_i - 1] = candidate[z_i - 1], candidate[z_i]
    return candidate

  def moveRightCandidate(self, z_i):
    candidate = self.state[:]
    candidate[z_i], candidate[z_i + 1] = candidate[z_i + 1], candidate[z_i]
    return candidate

  def moveUpCandidate(self, z_i):
    candidate = self.state[:]
    candidate[z_i], candidate[z_i - 3] = candidate[z_i - 3], candidate[z_i]
    return candidate

  def moveDownCandidate(self, z_i):
    candidate = self.state[:]
    candidate[z_i], candidate[z_i + 3] = candidate[z_i + 3], candidate[z_i]
    return candidate

  def solved(self):
    return self.state == [1, 2, 3, 4, 5, 6, 7, 8, 0]


def main():
  input_tiles = input("Input a list of 9 unique numbers from 0 - 8:")
  puzzle = EightPuzzleID(input_tiles)
  puzzle.solve()

  print(f"Puzzle solved? {puzzle.solved()}")
  print(f"Solution steps: {puzzle.solutionSteps[1:]}")
  print(f"Moves needed to solve: {len(puzzle.solutionSteps) - 1}")

main()
