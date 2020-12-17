import itertools
from copy import deepcopy
startingCubes = []




inputFile = open('input.txt', 'r') 


for line in inputFile:
  stripped = list(line.rstrip())
  startingCubes.append(stripped)

inputFile.close()

def seedState(startingCubes, knownCoords):
  for y in range(len(startingCubes)):
    for x in range(len(startingCubes[0])):
      knownCoords[(x,y,0)] = startingCubes[y][x]

def seedState2(startingCubes, knownCoords):
  for y in range(len(startingCubes)):
    for x in range(len(startingCubes[0])):
      knownCoords[(x,y,0,0)] = startingCubes[y][x]

def IsActive(coords, knownCoords, temp):
  if(coords in knownCoords):
    if(knownCoords[coords] == "#"):
      return True
    return False
  else:
    temp[coords] = "."
    return False


def GetVariations(coord):
  out =[]

  adders = list(itertools.product([0, 1], repeat=3))

  for i in range(0, len(adders)):
    adder = adders[i]
    out.append((coord[0] + adder[0], coord[1] + adder[1],coord[2] + adder[2]))
    out.append((coord[0] - adder[0], coord[1] + adder[1],coord[2] + adder[2]))
    out.append((coord[0] + adder[0], coord[1] - adder[1],coord[2] + adder[2]))
    out.append((coord[0] + adder[0], coord[1] + adder[1],coord[2] - adder[2]))
    out.append((coord[0] - adder[0], coord[1] - adder[1],coord[2] + adder[2]))
    out.append((coord[0] + adder[0], coord[1] - adder[1],coord[2] - adder[2]))
    out.append((coord[0] - adder[0], coord[1] - adder[1],coord[2] - adder[2]))
    out.append((coord[0] - adder[0], coord[1] + adder[1],coord[2] - adder[2]))
  

  out = list(set(out))

  return out

def GetVariations2(coord):
  out =[]

  adders = list(itertools.product([0, 1], repeat=4))

  for i in range(0, len(adders)):
    adder = adders[i]

    #0000
    out.append((coord[0] - adder[0], coord[1] - adder[1], coord[2] - adder[2], coord[3] - adder[3]))
    
    #1111
    out.append((coord[0] + adder[0], coord[1] + adder[1], coord[2] + adder[2], coord[3] + adder[3]))

    #0111, 1011, 1101, 1110
    out.append((coord[0] - adder[0], coord[1] + adder[1], coord[2] + adder[2], coord[3] + adder[3]))
    out.append((coord[0] + adder[0], coord[1] - adder[1], coord[2] + adder[2], coord[3] + adder[3]))
    out.append((coord[0] + adder[0], coord[1] + adder[1], coord[2] - adder[2], coord[3] + adder[3]))
    out.append((coord[0] + adder[0], coord[1] + adder[1], coord[2] + adder[2], coord[3] - adder[3]))

    #0011, 1001, 1100, 0110
    out.append((coord[0] - adder[0], coord[1] - adder[1], coord[2] + adder[2], coord[3] + adder[3]))
    out.append((coord[0] + adder[0], coord[1] - adder[1], coord[2] - adder[2], coord[3] + adder[3]))
    out.append((coord[0] + adder[0], coord[1] + adder[1], coord[2] - adder[2], coord[3] - adder[3]))
    out.append((coord[0] - adder[0], coord[1] + adder[1], coord[2] + adder[2], coord[3] - adder[3]))

    #0101, 1010
    out.append((coord[0] - adder[0], coord[1] + adder[1], coord[2] - adder[2], coord[3] + adder[3]))
    out.append((coord[0] + adder[0], coord[1] - adder[1], coord[2] + adder[2], coord[3] - adder[3]))
    
    #0001, 0010, 0100, 1000
    out.append((coord[0] - adder[0], coord[1] - adder[1], coord[2] - adder[2], coord[3] + adder[3]))
    out.append((coord[0] - adder[0], coord[1] - adder[1], coord[2] + adder[2], coord[3] - adder[3]))
    out.append((coord[0] - adder[0], coord[1] + adder[1], coord[2] - adder[2], coord[3] - adder[3]))
    out.append((coord[0] + adder[0], coord[1] - adder[1], coord[2] - adder[2], coord[3] - adder[3]))
  

  out = list(set(out))

  return out

def getNeighbours(coords, knownCoords, temp):
  count = 0

  variations = GetVariations(coords)

  for coord in variations:
    count += 1 if IsActive(coord, knownCoords, temp) and coord != coords else 0

  return count

def getNeighbours2(coords, knownCoords, temp):
  count = 0

  variations = GetVariations2(coords)

  for coord in variations:
    count += 1 if IsActive(coord, knownCoords, temp) and coord != coords else 0

  return count

def CountActive(knownCoords):
  return list(knownCoords.values()).count("#")

def PrintBoardAtDepth(board, z):
  for y in range(-4,4):
    line = ""
    for x in range(-4,4):
      if((x,y,z) in board):
        line += board[(x,y,z)]
      else:
        line += "."
    print(line)

def solve(startingCubes):
  knownCoords = {}
  #coords will be in XYZ 
  seedState(startingCubes, knownCoords)
  cycle = 0

  while cycle < 6:


    #PrintBoardAtDepth(knownCoords, 0)
    cycle += 1

    temp = deepcopy(knownCoords)
    for coord in list(knownCoords):
      cube = knownCoords[coord]
      neighbours = getNeighbours(coord, knownCoords, temp)
    knownCoords = deepcopy(temp)

    temp = deepcopy(knownCoords)
    for coord in list(knownCoords):
      cube = knownCoords[coord]
      neighbours = getNeighbours(coord, knownCoords, temp)
      if(cube == "#" and neighbours not in [2,3]):
        temp[coord] = "."
      elif(cube == "." and neighbours == 3):
        temp[coord] = "#"

    knownCoords = deepcopy(temp)
    print("Starting Cycle " + str(cycle) + "...")
    #print("0,0,0" + ": " + str(knownCoords[(0,0,0,)]))
  #print(knownCoords)
  return CountActive(knownCoords)
  #return getNeighbours((1,1,0), knownCoords)

def solve2(startingCubes):
  knownCoords = {}
  #coords will be in XYZW
  seedState2(startingCubes, knownCoords)
  cycle = 0

  while cycle < 6:


    #PrintBoardAtDepth(knownCoords, 0)
    cycle += 1

    print("Finding Neighbours")
    temp = deepcopy(knownCoords)
    for coord in list(knownCoords):
      cube = knownCoords[coord]
      neighbours = getNeighbours2(coord, knownCoords, temp)
    knownCoords = deepcopy(temp)
    print("Done!")

    print("Checking Actives")
    temp = deepcopy(knownCoords)
    for coord in list(knownCoords):
      cube = knownCoords[coord]
      neighbours = getNeighbours2(coord, knownCoords, temp)
      if(cube == "#" and neighbours not in [2,3]):
        temp[coord] = "."
      elif(cube == "." and neighbours == 3):
        temp[coord] = "#"
    print("Done!")

    knownCoords = deepcopy(temp)
    print("Starting Cycle " + str(cycle) + "...")
    #print("0,0,0" + ": " + str(knownCoords[(0,0,0,)]))
  #print(knownCoords)
  return CountActive(knownCoords)
  #return getNeighbours((1,1,0), knownCoords)

  
print(solve2(startingCubes))

