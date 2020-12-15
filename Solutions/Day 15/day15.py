
numbersDict = {0:[1],13:[2],1:[3],16:[4],6:[5],17:[6]}

def solve(numbersDict, target):
  turn = len(numbersDict)
  lastSaid = 17
  while turn < target:
    turn+=1
    
    if(len(numbersDict[lastSaid]) > 1):  
      firstTimeFound = numbersDict[lastSaid][-1]
      secondTimeFound = numbersDict[lastSaid][-2]
      lastSaid = firstTimeFound - secondTimeFound
    else:
      lastSaid = 0

    if(lastSaid in numbersDict):
      numbersDict[lastSaid].append(turn)
    else:
      numbersDict[lastSaid] = [turn]
    #print("Turn " + str(turn))
    #print(numbers)

  
  return lastSaid

print(solve(numbersDict, 30000000))
