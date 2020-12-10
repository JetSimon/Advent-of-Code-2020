from itertools import permutations

adapters = []

inputFile = open('input.txt', 'r') 


for line in inputFile:
  stripped = line.rstrip()
  adapters.append(int(stripped))

inputFile.close()

print(len(adapters))

#returns index of adapter best suited to use and then the difference amount
def getClosest(adapters, target, maxRange):
  out = None
  for i in range(len(adapters)):
    adapter = adapters[i]
    if(abs(target-adapter) <= range and (out == None or adapter < adapters[out])):
      out = i
  return [out, abs(target-adapters[out])]

#returns index of adapter best suited to use and then the difference amount
def isValid(adapters):
  for i in range(1,len(adapters)):
    before = adapters[i-1]
    current = adapters[i]
    if(before + 1 == current or before + 2 == current or before + 3 == current):
      continue
    return False
  return True

def swapPositions(l, pos1, pos2):      
    t1 = l[pos1]
    t2 = l[pos2]

    l[pos1] = t2
    l[pos2] = t1

    return l

def solve(adapters):
  adapters.append(max(adapters)+3)
  currentJolt = 0
  ones = 0
  threes = 0
  while len(adapters) > 0:
    closestAdapterArray = getClosest(adapters, currentJolt, 3)
    closestAdapter = closestAdapterArray[0]
    difference = closestAdapterArray[1]
    
    if(difference == 1):
      ones += 1
    elif(difference == 3):
      threes += 1

    currentJolt = adapters.pop(closestAdapter)
  
  return ones * threes

def getBestConfig(adapters):
  out = []
  currentJolt = 0
  while len(adapters) > 0:
    closestAdapterArray = getClosest(adapters, currentJolt, 3)
    closestAdapter = closestAdapterArray[0]
    out.append(adapters.pop(closestAdapter))

  return out

def solve2(adapters):

  builtIn = max(adapters) + 3

  triedAlready={str(adapters):True}
  counter = 1
  valids = [adapters]
  toRemove = []

  while len(valids)>0:
    for a in toRemove:
      valids.remove(a)
    toRemove=[]

    
    for a in valids:
      for i in range(len(a)):
        attempt = a[:]
        attempt.pop(i)
        

        attempt.append(builtIn)
        attempt.reverse()
        attempt.append(0)
        attempt.reverse()

        if(isValid(attempt)):
          attempt = attempt[1:-1]
          if(str(attempt) not in triedAlready):
            triedAlready[str(attempt)] = True
            counter+=1
          valids.append(attempt)
      toRemove.append(a)
  
  return counter
#print(solve2(getBestConfig(adapters)))
