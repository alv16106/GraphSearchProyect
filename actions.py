import math
import utilities
import parser

def sudokuActions(s):
  possibleActions = []
  print(int(math.sqrt(len(s))))
  for i in range(len(s)):
    if s[i] == None:
      for k in range(1, int(math.sqrt(len(s)))+1):
        if not utilities.isDuplicate(s, i, k):
          possibleActions.append({
            'action': lambda state: utilities.addNumber(state, i, k),
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
    'fifteen': fifteenActions,
  }
  return switcher.get(type, default(1))

state = parser.getParsedInput('.4.13.4.1..4.21.')
for x in sudokuActions(state):
  print(x['Description'])