print("hey world!!!")
print("bye bye!!!")
print("no no no")

# new median function
def median(inputList):
  median = -1
  listLength = len(inputList)
  middleIndex = (listLength - 1) // 2

  if listLength // 2 == 1:
    median = inputList(middleIndex)
  else:
    median = (inputList[middleIndex] + inputList[middleIndex + 1]) / 2

  return median