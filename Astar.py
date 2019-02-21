import problems
import time
import utilities
import sys
import htmlGenerator

class Node():
  """A node class for A* Pathfinding"""
  def __init__(self, parent=None, board=None):
      self.parent = parent
      self.board = board

      self.g = 0
      self.f = 0
  def __eq__(self, other):
    return self.board == other.board
  def __str__(self):
    return 'Nodo con costo: ' + str(self.g) + ' y costo total: ' + str(self.f) 

def aStar(problem):
  #Inicializacion de frontera
  initial = Node(None, problem['initialState'])
  initial.g = initial.h = initial.f = 0
  explored = []
  nonExplored = []
  nonExplored.append(initial)

  #Mientras aun se pueda explorar
  while(nonExplored):
    current = nonExplored[0]
    current_index = 0
    #Tratamos de encontrar el mejor nodo
    for index, item in enumerate(nonExplored):
      if item.f < current.f:
        current = item
        current_index = index

    # Eliminamos el escogido de la frontera y lo añadimos a los estados ya visitados
    nonExplored.pop(current_index)
    explored.append(current)

    # Lo logramos? Si si armar el path
    if problem['goalTest'](current.board):
      path = []
      while current is not None:
        path.append(current.board)
        current = current.parent
      print(len(path))
      return path[::-1]

    actions = problem['actions'](current.board)
    for action in actions:
      newState = problem['result'](current.board, action['action'])
      newNode = Node(current, newState)
      newNode.g = current.g + action['cost']
      newNode.f = problem['totalCost'](newNode.g, newState)
      if not utilities.isVisited(newNode, explored):
        nonExplored.append(newNode)

path = aStar(problems.getProblem(sys.argv[1])(sys.argv[2]))
htmlGenerator.createPath(path, sys.argv[1])
# 'B1E5C73F294D.A68'