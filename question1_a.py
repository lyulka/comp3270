import time

class EightPuzzleID:
  def __init__(self, input_tiles):
    input_tiles = input_tiles.split(" ")
    for i in range(len(input_tiles)):
      input_tiles[i] = int(input_tiles[i])

    self.state = input_tiles
    self.solutionSteps = []

  def solve(self):
    limit = 1
    exp_count = 0

    while not self.solved() \
      and exp_count <= 1000000:
      exp_count, dfs_stack = self.depthLimitedSolve(limit, exp_count)
      limit += 1

    if exp_count > 1000000:
      print(f"More than 1000000 nodes expanded and solution not found.")
    else:
      self.solutionSteps = [step[1] for step in dfs_stack]

  # Return values: exp_count, dfs_stack
  def depthLimitedSolve(self, limit, exp_count_so_far):
    depth = 0
    dfs_stack = list()
    expanded = set()
    exp_count = exp_count_so_far
    
    while True:
      # Add current state to expanded
      expanded.add(tuple(self.state))

      if exp_count > 1000000:
        return(exp_count, dfs_stack)

      if depth == limit:
        self.state = dfs_stack.pop()[0]
        depth -= 1

        continue

      if self.solved():
        return (exp_count, dfs_stack)

      # Attempt to go deeper
      successor = self.successor(expanded)

      # All neighbors have been expanded
      if (successor == None):
        if len(dfs_stack) == 0:
          return (exp_count, dfs_stack)

        self.state = dfs_stack.pop()[0]
        depth -= 1
        continue

      # Append current state to backtrack to later
      dfs_stack.append([self.state, successor[1]])

      self.state = successor[0]

      depth += 1

  def successor(self, expanded):
    zero_index = self.state.index(0)

    # Zero is the middle tile
    if (zero_index == 4):
      candidate = self.moveUpCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 up')

      candidate = self.moveDownCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 down')

      candidate = self.moveLeftCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 left')

      candidate = self.moveRightCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 right')

    # Zero is the top left tile
    elif (zero_index == 0):
      candidate = self.moveDownCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 down')

      candidate = self.moveRightCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 right')
    
    # Zero is the top right tile
    elif (zero_index == 2):
      candidate = self.moveDownCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 down')

      candidate = self.moveLeftCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 left')

    # Zero is the bottom left tile
    elif (zero_index == 3):
      candidate = self.moveUpCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 up')

      candidate = self.moveRightCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 right')

    # Zero is the bottom right tile
    elif (zero_index == 3):
      candidate = self.moveUpCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 up')

      candidate = self.moveLeftCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 left')

    # Zero is the top middle tile:
    elif (zero_index == 1):
      candidate = self.moveDownCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 down')

      candidate = self.moveLeftCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 left')

      candidate = self.moveRightCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 right')
    
    # Zero is the middle left tile:
    elif (zero_index == 3):
      candidate = self.moveUpCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 up')

      candidate = self.moveDownCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 down')

      candidate = self.moveRightCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 right')

    # Zero is the middle right tile:
    elif (zero_index == 3):
      candidate = self.moveUpCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 up')

      candidate = self.moveDownCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 down')

      candidate = self.moveLeftCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 left')

    # Zero is the bottom middle tile:
    else:
      candidate = self.moveUpCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 up')

      candidate = self.moveLeftCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 left')

      candidate = self.moveRightCandidate(zero_index)
      if tuple(candidate) not in expanded:
        return (candidate, 'Move 0 right')

    return None
    
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
    return self.state == [0, 1, 2, 3, 4, 5, 6, 7, 8]

def main():
    input_tiles = input("Input a list of 9 unique numbers from 0 - 8:")
    puzzle = EightPuzzleID(input_tiles)
    puzzle.solve()

    print(f"Puzzle solved? {puzzle.solved()}")
    for step in puzzle.solutionSteps:
      print(step)
    print(f"Steps needed to solve: {len(puzzle.solutionSteps)}")

main()
