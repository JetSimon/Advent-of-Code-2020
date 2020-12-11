from copy import copy, deepcopy

seats = []

inputFile = open('input.txt', 'r') 


for line in inputFile:
  stripped = line.rstrip()
  seats.append(list(stripped))

inputFile.close()

def getSeatInDirection(array, y, x, vert, hor):
  currentX = x + hor
  currentY = y + vert

  try:
    currentTest = array[currentY][currentX]
  except:
    return 0

  if(currentX < 0 or currentY < 0):
    return 0
  try:
    while(True):
      if(currentTest == "#"):
        return 1
      if(currentTest == "L"):
        return 0
      currentX += hor
      currentY += vert
      currentTest = array[currentY][currentX]
      
      if(currentX < 0 or currentY < 0):
        return 0
  except:
    return 0 
  return 0

def SeeSeats(array, y, x):
  count = 0
  count += getSeatInDirection(array, y, x, 1, 0)
  count += getSeatInDirection(array, y, x, -1, 0)
  count += getSeatInDirection(array, y, x, 0, 1)
  count += getSeatInDirection(array, y, x, 0, -1)
  count += getSeatInDirection(array, y, x, 1, 1)
  count += getSeatInDirection(array, y, x, 1, -1)
  count += getSeatInDirection(array, y, x, -1, 1)
  count += getSeatInDirection(array, y, x, -1, -1)
  return count

def getOccupiedNextTo(array, y, x):
  count = 0
  xSize = len(array[0])
  ySize = len(array)
  
  #sides
  try:
    count += 1 if (x < xSize and array[y][x+1] == "#") else 0
  except:
    pass
  try:
    count += 1 if (x > 0 and array[y][x-1] == "#") else 0
  except:
    pass
  #verts
  try:
    count += 1 if (y < ySize and array[y+1][x] == "#") else 0
  except:
    pass
  try:
    count += 1 if (y > 0 and array[y-1][x] == "#") else 0
  except:
    pass

  #diagonal left right up
  try:
    count += 1 if (y > 0 and x > 0 and  array[y-1][x-1] == "#") else 0
  except:
    pass
  try:
    count += 1 if (y > 0 and x < xSize and  array[y-1][x+1] == "#") else 0
  except:
    pass

  #diagonal left right down
  try:
    count += 1 if (y < ySize and x > 0 and  array[y+1][x-1] == "#") else 0
  except:
    pass
  try:
    count += 1 if (y < ySize and x < xSize and  array[y+1][x+1] == "#") else 0
  except:
    pass

  return count

def countOccupied(array):
  count = 0
  for a in array:
    for e in a:
      if(e == "#"):
        count+=1
  return count

def solve(seats):
  hasChanged = True

  while hasChanged:

    tempSeats = deepcopy(seats)
    hasChanged = False
    for y in range(len(seats)):
      for x in range(len(seats[0])):
        seat = seats[y][x]
        occ = getOccupiedNextTo(seats, y, x)
        if(seat == "L" and occ == 0):
          hasChanged = True
          tempSeats[y][x] = "#"
          
        elif(seat == "#" and occ >= 4):
          hasChanged = True
          tempSeats[y][x] = "L"

    seats = deepcopy(tempSeats)
  
  return countOccupied(seats)

def printBoard(array):
  print("---")
  for a in array:
    print("".join(a))
  print("---")

def solve2(seats):
  hasChanged = True
  
  while hasChanged:
    #printBoard(seats)
    tempSeats = deepcopy(seats)
    hasChanged = False
    for y in range(len(seats)):
      for x in range(len(seats[0])):
        seat = seats[y][x]
        occ = SeeSeats(seats, y, x)
        if(seat == "L" and occ == 0):
          hasChanged = True
          tempSeats[y][x] = "#"
          
        elif(seat == "#" and occ >= 5):
          hasChanged = True
          tempSeats[y][x] = "L"

    seats = deepcopy(tempSeats)
  
  return countOccupied(seats)


print(solve2(seats))

