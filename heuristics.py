import actions
import utilities

def sudokuEuristic(s):
  return len(actions.getActionCreator('sudoku')(s))

def fithteenHeuristics(s):
  heuristic = 0
  for index, item in enumerate(s):
    if item:
      heuristic += utilities.manhattanDistance(index, item - 1, 4)
  return heuristic