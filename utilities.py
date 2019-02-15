def addNumber(matrix, position, number):
  if matrix[position]:
    raise Exception('Esta posicion ya tiene un numero')
  matrix[position] = number
  return matrix

def removeNumber(matrix, position):
  matrix[position] = None
  return matrix

ma = [1, 2, 3, None];
print(addNumber(ma, 3, 4))
print(removeNumber(ma, 1))
print(addNumber(ma, 2, 4))