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

def fifthteen(input):
  pass

def getProblem(type):
  switcher = {
    'sudoku': sudoku,
    'fifthteen': fifthteen,
  }
  return switcher.get(type)

sd = sudoku('.4.13.4.1..4.21.')
print(sd['result'](1, lambda s: s + 2))