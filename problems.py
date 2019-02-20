import parser
import goalTests
import actions
import heuristics

def sudoku(input):
  return {
    'initialState': parser.getParsedInput(input),
    'actions': actions.getActionCreator('sudoku'),
    'result': lambda s, a: a(s),
    'goalTest': lambda s: goalTests.sudokuTest(s),
    'totalCost': lambda g, s: g + heuristics.sudokuEuristic(s),
  }

def fifteen(input):
  return {
    'initialState': parser.getParsedInput(input),
    'actions': actions.getActionCreator('fifteen'),
    'result': lambda s, a: a(s),
    'goalTest': lambda s: goalTests.fifteenTest(s),
    'totalCost': lambda g, s: g + heuristics.fithteenHeuristics(s),
  }

def getProblem(type):
  switcher = {
    'sudoku': sudoku,
    'fifteen': fifteen,
  }
  return switcher.get(type)
