import actions

def sudokuEuristic(s):
  return len(actions.getActionCreator('sudoku')(s))