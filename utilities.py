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