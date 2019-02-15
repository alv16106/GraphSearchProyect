
def sudokuActions(s):
  possibleActions = []


def fifteenActions(s):

def default(s):
  raise Exception('Defina un tipo de acciones')

def getActionCreator(type):
  switcher = {
    'sudoku': sudokuActions,
    'fifteen': fifteenActions,
  }
  return switcher.get(type, default(1))