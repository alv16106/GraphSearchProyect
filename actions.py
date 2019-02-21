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
  possibleActions = []
  nullIndex = s.index(None)
  for i in utilities.getInterchangeblePositions(s, nullIndex):
    possibleActions.append({
      'action': lambda state, i=i: utilities.changePositions(state, nullIndex, i),
      'cost': 0,
      'Description': 'Intercambiar numero en la posicion ' + str(i) + ' con None ',
    })
  return possibleActions

def default(s):
  raise Exception('Defina un tipo de acciones')

def getActionCreator(type):
  switcher = {
    'sudoku': sudokuActions,
    'fifteen': fifteenActions,
  }
  return switcher.get(type)
