instructions = []

inputFile = open('input.txt', 'r') 


for line in inputFile:
  stripped = line.rstrip()
  instructions.append(stripped)

inputFile.close()

def solve(instructions):
  #array of indexes to be filled later
  acc = 0
  alreadyExecuted = []
  currentInstruction = 0
  while currentInstruction not in alreadyExecuted:
    alreadyExecuted.append(currentInstruction)
    instruction = instructions[currentInstruction]

    op = instruction.split(" ")[0]
    arg = int(instruction.split(" ")[1])
    
    if(op == "acc"):
      acc += arg
      currentInstruction+=1
      continue
    
    if(op == "jmp"):
      currentInstruction+= arg
      continue

    if(op == "nop"):
      currentInstruction+=1
      continue

  return acc

def CheckIfWorking(instructions):
  acc = 0
  alreadyExecuted = []
  currentInstruction = 0
  while True:

    if(currentInstruction in alreadyExecuted):
      return False

    if(currentInstruction == len(instructions)):
      return acc

    alreadyExecuted.append(currentInstruction)
    instruction = instructions[currentInstruction]

    op = instruction.split(" ")[0]
    arg = int(instruction.split(" ")[1])
    
    if(op == "acc"):
      acc += arg
      currentInstruction+=1
      continue
    
    if(op == "jmp"):
      currentInstruction+= arg
      continue

    if(op == "nop"):
      currentInstruction+=1
      continue

def solve2(instructions):
  for i in range(len(instructions)):
    testInstructions = instructions.copy()
    op = testInstructions[i].split(" ")[0]
    if(op == "acc"):
      continue
    elif(op == "jmp"):
      testInstructions[i] = testInstructions[i].replace("jmp","nop")
    elif(op == "nop"):
      testInstructions[i] = testInstructions[i].replace("nop","jmp")

    testRun = CheckIfWorking(testInstructions)

    if(testRun != False):
      return testRun
  return False
    

print(solve2(instructions))