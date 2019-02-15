import math

def addNumber(matrix, position, number):
  if matrix[position]:
    raise Exception('Esta posicion ya tiene un numero')
  matrix[position] = number
  return matrix

def removeNumber(matrix, position):
  matrix[position] = None
  return matrix

def isDuplicateInLines(matrix, position, number):
  size = int(math.sqrt(len(matrix)))
  row = int(position/size)
  column = int(position%size)
  for i in matrix[row*size: row*size+size]:
    if i == number:
      return True
  for j in matrix[column:column+size*(size-1) + 1:size]:
    if j == number:
      return True
  return False

ma = [1, 2, 3, 2];
print(isDuplicateInLines(ma, 1, 2))