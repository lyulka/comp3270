from heapq import heappush, heappop, heapify\

def misplacedTiles(state, cost_so_far = 0):
  count = 0
  for i in range(len(state)):
    if state[i] != i:
      count += 1

  return cost_so_far + count

def manhattanDistance(state, cost_so_far = 0):
  count = 0
  for i in range(len(state)):
    actual_x = i % 3
    actual_y = i // 3
    desired_x = state[i] % 3
    desired_y = state[i] // 3

    count += abs(desired_x - actual_x) + abs(desired_y - actual_y)

  return cost_so_far + count

class EightPuzzleAStar:
  def __init__(self, input_tiles):
    input_tiles = input_tiles.split(" ")
    for i in range(len(input_tiles)):
      input_tiles[i] = int(input_tiles[i])

    input_tiles = tuple(input_tiles)

    self.state = input_tiles
    self.solutionSteps = []

  def solve(self, heuristic):
    # S stands for start
    steps = "S"
    expanded = dict()
    successors = []

    h_cost = heuristic(self.state)
    heappush(successors, (h_cost, self.state, "S"))

    while True:
      # Not found!
      if len(successors) == 0:
        return
      
      if self.solved():
        self.solutionSteps = steps
        return

      cur_node = heappop(successors)
      h_cost = cur_node[0]
      self.state = cur_node[1]
      steps = cur_node[2]

      # Already expanded before with lower h_cost
      if self.state in expanded \
        and expanded[self.state] <= h_cost:
        continue

      expanded[self.state] = h_cost

      cur_successors = self.successors(heuristic, steps)
      for successor in cur_successors:
        heappush(successors, successor)      

  def successors(self, heuristic, steps):
    zero_index = self.state.index(0)

    # Zero is the middle tile
    if (zero_index == 4):
      res = []
      candidate = self.moveUpCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "D": res.append((h_cost, candidate, steps + 'U'))

      candidate = self.moveDownCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "U": res.append((h_cost, candidate, steps + 'D'))
      
      candidate = self.moveLeftCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "R": res.append((h_cost, candidate, steps + 'L'))
      
      candidate = self.moveRightCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "L": res.append((h_cost, candidate, steps + 'R'))

      return res

    # Zero is the top left tile
    elif (zero_index == 0):
      res = []
      candidate = self.moveDownCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "U": res.append((h_cost, candidate, steps + 'D'))
      
      candidate = self.moveRightCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "L": res.append((h_cost, candidate, steps + 'R'))
      
      return res
    
    # Zero is the top right tile
    elif (zero_index == 2):
      res = []
      candidate = self.moveDownCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "U": res.append((h_cost, candidate, steps + 'D'))
      
      candidate = self.moveLeftCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "R": res.append((h_cost, candidate, steps + 'L'))

      return res

    # Zero is the bottom left tile
    elif (zero_index == 6):
      res = []
      candidate = self.moveUpCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "D": res.append((h_cost, candidate, steps + 'U'))
      
      candidate = self.moveRightCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "L": res.append((h_cost, candidate, steps + 'R'))

      return res

    # Zero is the bottom right tile
    elif (zero_index == 8):
      res = []
      candidate = self.moveUpCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "D": res.append((h_cost, candidate, steps + 'U'))
      
      candidate = self.moveLeftCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "R": res.append((h_cost, candidate, steps + 'L'))

      return res

    # Zero is the top middle tile:
    elif (zero_index == 1):
      res = []
      candidate = self.moveDownCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "U": res.append((h_cost, candidate, steps + 'D'))
      
      candidate = self.moveLeftCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "R": res.append((h_cost, candidate, steps + 'L'))
      
      candidate = self.moveRightCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "L": res.append((h_cost, candidate, steps + 'R'))

      return res
    
    # Zero is the middle left tile:
    elif (zero_index == 3):
      res = []
      candidate = self.moveUpCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "D": res.append((h_cost, candidate, steps + 'U'))

      candidate = self.moveDownCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "U": res.append((h_cost, candidate, steps + 'D'))
      
      candidate = self.moveRightCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "L": res.append((h_cost, candidate, steps + 'R'))

      return res

    # Zero is the middle right tile:
    elif (zero_index == 5):
      res = []
      candidate = self.moveUpCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "D": res.append((h_cost, candidate, steps + 'U'))

      candidate = self.moveDownCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "U": res.append((h_cost, candidate, steps + 'D'))
      
      candidate = self.moveLeftCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "R": res.append((h_cost, candidate, steps + 'L'))

      return res

    # Zero is the bottom middle tile:
    else:
      res = []
      candidate = self.moveUpCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "D": res.append((h_cost, candidate, steps + 'U'))
      
      candidate = self.moveLeftCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "R": res.append((h_cost, candidate, steps + 'L'))
      
      candidate = self.moveRightCandidate(zero_index)
      h_cost = heuristic(candidate, len(steps))
      if steps[-1] != "L": res.append((h_cost, candidate, steps + 'R'))

    return res
    
  def moveLeftCandidate(self, z_i):
    candidate = list(self.state)
    candidate[z_i], candidate[z_i - 1] = candidate[z_i - 1], candidate[z_i]
    return tuple(candidate)

  def moveRightCandidate(self, z_i):
    candidate = list(self.state)
    candidate[z_i], candidate[z_i + 1] = candidate[z_i + 1], candidate[z_i]
    return tuple(candidate)

  def moveUpCandidate(self, z_i):
    candidate = list(self.state)
    candidate[z_i], candidate[z_i - 3] = candidate[z_i - 3], candidate[z_i]
    return tuple(candidate)

  def moveDownCandidate(self, z_i):
    candidate = list(self.state)
    candidate[z_i], candidate[z_i + 3] = candidate[z_i + 3], candidate[z_i]
    return tuple(candidate)

  def solved(self):
    return self.state == (0, 1, 2, 3, 4, 5, 6, 7, 8)


def main():
  input_tiles = input("Input a list of 9 unique numbers from 0 - 8\
  (this will be solved using number of misplaced tile heuristic): ")
  puzzle1 = EightPuzzleAStar(input_tiles)
  puzzle1.solve(misplacedTiles)

  print(f"Puzzle 1 solved? {puzzle1.solved()}")
  print(f"Solution steps: {puzzle1.solutionSteps[1:]}")
  print(f"Moves needed to solve: {len(puzzle1.solutionSteps[1:])}")

  input_tiles = input("Input a list of 9 unique numbers from 0 - 8\
  (this will be solved using sum of Manhattan distances heuristic): ")
  puzzle2 = EightPuzzleAStar(input_tiles)
  puzzle2.solve(manhattanDistance)

  print(f"Puzzle 2 solved? {puzzle2.solved()}")
  print(f"Solution steps: {puzzle2.solutionSteps[1:]}")
  print(f"Moves needed to solve: {len(puzzle2.solutionSteps[1:])}")

main()
