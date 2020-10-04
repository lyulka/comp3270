state = input("Input tiles: ")
state = state.split(" ")

def printState(state):
  print(f"{state[0]} {state[1]} {state[2]}")
  print(f"{state[3]} {state[4]} {state[5]}")
  print(f"{state[6]} {state[7]} {state[8]}")

def moveLeftCandidate(state, z_i):
  candidate = state[:]
  candidate[z_i], candidate[z_i - 1] = candidate[z_i - 1], candidate[z_i]
  return candidate

def moveRightCandidate(state, z_i):
  candidate = state[:]
  candidate[z_i], candidate[z_i + 1] = candidate[z_i + 1], candidate[z_i]
  return candidate

def moveUpCandidate(state, z_i):
  candidate = state[:]
  candidate[z_i], candidate[z_i - 3] = candidate[z_i - 3], candidate[z_i]
  return candidate

def moveDownCandidate(state, z_i):
  candidate = state[:]
  candidate[z_i], candidate[z_i + 3] = candidate[z_i + 3], candidate[z_i]
  return candidate

while True:
  printState(state)
  move = input("Enter a move: ")

  if move == "U": state = moveUpCandidate(state, state.index('0'))
  elif move == "D": state = moveDownCandidate(state, state.index('0'))
  elif move == "L": state = moveLeftCandidate(state, state.index('0'))
  else: state = moveRightCandidate(state, state.index('0'))
