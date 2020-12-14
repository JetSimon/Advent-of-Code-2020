import itertools
commands = []



inputFile = open('input.txt', 'r') 

for line in inputFile:
  stripped = line.rstrip()
  commands.append(stripped)

inputFile.close()

def PadBinary(val, mask):
  out = list(val)
  out.reverse()
  while len(out) < len(mask):
    out.append("0")
  out.reverse()
  return "".join(out)

def ApplyMask(val, mask):
  out = list(val)
  for i in range(len(mask)):
    if(mask[i] != "X"):
      out[i] = mask[i]
  return int("".join(out), 2)

def ApplyMask2(val, mask):
  out = list(val)
  for i in range(len(mask)):
    if(mask[i] == "X"):
      out[i] = "X"
    elif(mask[i] == "1"):
      out[i] = "1"
  return "".join(out)

def GetAllPossible(val, memory, initial):
  binaryCombos = list(map(list, itertools.product([0, 1], repeat=val.count("X"))))
  floatingPositions = [i for i, x in enumerate(val) if x == "X"]
  for combo in binaryCombos:
    template = list(val)
    for position in floatingPositions:
      template[position] = str(combo.pop())
    #print(int("".join(template), 2))
    memory[int("".join(template), 2)] = initial

def solve(commands):
  mask = None
  memory = {}
  
  for command in commands:

    if(command.split("=")[0].strip() == "mask"):  
      mask = command.split("=")[1].strip()
      continue

    slot = int(command.split("=")[0].strip().split("[")[1].strip("]"))
    value = str(bin(int(command.split("=")[1].strip()))).split("b")[1]
    value = PadBinary(value, mask)
    newValue = ApplyMask(value, mask)
    memory[slot] = newValue

  return sum(memory.values())

def solve2(commands):
  mask = None
  memory = {}
  for command in commands:

    if(command.split("=")[0].strip() == "mask"):  
      mask = command.split("=")[1].strip()
      continue

    slot = int(command.split("=")[0].strip().split("[")[1].strip("]"))
    initial = int(command.split("=")[1].strip())
    value = str(bin(slot)).split("b")[1]
    value = PadBinary(value, mask)
    #print(value)
    newValue = ApplyMask2(value, mask)
    GetAllPossible(newValue, memory, initial)

  return sum(memory.values())





print(solve2(commands))