print("hey world!!!")
print("bye bye!!!")
print("no no no")

# new mean function
def mean(input):
  sum = 0
  for entry in input:
    sum += entry
  return sum / len(input)