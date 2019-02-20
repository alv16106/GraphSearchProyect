def sudokuTest(s):
  if not s.count(None):
    return True
  return False

def fifteenTest(s):
  for i in range(1, len(s)-1):
    if not s[i] or not s[i-1]:
      return False
    if s[i] < s[i - 1]:
      return False
  return True