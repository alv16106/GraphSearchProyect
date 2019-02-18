import math
import utilities
import parser
import copy

def sudokuActions(s):
  possibleActions = []
  for i in range(len(s)):
    if s[i] == None:
      for k in range(1, int(math.sqrt(len(s)))+1):
        if not utilities.isDuplicate(s, i, k):
          possibleActions.append({
            'action': lambda state, i=i, k=k: utilities.addNumber(state, i, k),
            'cost': 1,
            'Description': 'Poner ' + str(k) + ' en la posicion ' + str(i),
          })
  return possibleActions


def fifteenActions(s):
  return 0

def default(s):
  raise Exception('Defina un tipo de acciones')

def getActionCreator(type):
  switcher = {
    'sudoku': sudokuActions,
    'fifthteen': fifteenActions,
  }
  return switcher.get(type)
