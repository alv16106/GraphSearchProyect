def getParsedInput(input):
  parsedInput = []
  for i in input:
    if i != '.':
      parsedInput.append(int(i, 16))
    else:
      parsedInput.append(None)
  return parsedInput