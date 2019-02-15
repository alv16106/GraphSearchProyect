def getParsedInput(input):
  parsedInput = []
  for i in input:
    if i == '.':
      parsedInput.append(None)
      break
    parsedInput.append(int(i, 16))
  return parsedInput