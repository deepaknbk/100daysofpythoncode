def isPhoneNumber(text):
  if len(text) != 12:
    return False
  for i in range(0, 3): # check area code
    if not text[i].isdecimal():
      return False
  if text[3] != '-':
    return False
  for i in range(4, 7): # check first 3 digits
    if not text[i].isdecimal():
      return False
  if text[7] != '-':
    return False
  for i in range(8, 12): # check last 4 digits
    if not text[i].isdecimal():
      return False
    return True

text = """Alice,
      My number is 415-730-0000.
      Call me when it's convenient.
                     -Bob"""
for i, _ in enumerate(text):
  if isPhoneNumber(text[i:i+12]):
    print(text[i:i+12])
