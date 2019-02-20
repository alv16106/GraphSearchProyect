import math

def addNumber(matrix, position, number):
  if matrix[position]:
    raise Exception('En posicion: '+ str(position) + 'Esta posicion ya tiene un numero')
  newMatrix = matrix.copy()
  newMatrix[position] = number
  return newMatrix

def removeNumber(matrix, position):
  newMatrix = matrix.copy()
  newMatrix[position] = None
  return newMatrix

def changePositions(matrix, null, number):
  if matrix[null]:
    raise Exception('Una de estas posiciones no es un vacio')
  newMatrix = matrix.copy()
  newMatrix[null] = newMatrix[number]
  newMatrix[number] = None
  return newMatrix

def getInterchangeblePositions(matrix, null):
  positions = []
  size = int(math.sqrt(len(matrix)))
  positions += [null + size, null - size, null + 1, null - 1]
  if not null%size:
    positions .remove(null - 1)
  if null%size == size - 1:
    positions .remove(null + 1)
  if not int(null/4):
    positions .remove(null - size)
  if int(null/4) == size - 1:
    positions .remove(null + size)
  return positions

def isDuplicate(matrix, position, number):
  size = int(math.sqrt(len(matrix)))
  row = int(position/size)
  column = int(position%size)

  #look in sub-arrays containing row and column of the nmber
  for i in matrix[row*size: row*size+size]:
    if i == number:
      return True
  for j in matrix[column:column+size*(size-1) + 1:size]:
    if j == number:
      return True

  # Get information about the square
  rl = int(math.sqrt(size))
  bigSquareX = int(row/rl)
  bigSquareY = int(column/rl)
  #Iterate though indexes inside
  for k in range(bigSquareX*rl, bigSquareX*rl + rl):
    for l in range(bigSquareY*rl, bigSquareY*rl + rl):
      if matrix[k*size + l] == number:
        return True
  return False

def manhattanDistance(origin, end, size):
  x1 = int(origin/size)
  y1 = int(origin%size)
  x2 = int(end/size)
  y2 = int(end%size)
  return abs(x1 - x2) + abs(y1 - y2)

def isVisited(new, visited):
  for node in visited:
    if new == node:
      return True
  return False