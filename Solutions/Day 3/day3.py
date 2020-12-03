inputRead = []

inputFile = open('input.txt', 'r') 

for line in inputFile:
  stripped = line.rstrip()
  stripped = list(stripped)
  inputRead.append(stripped)

inputFile.close()

def solve(inputRead, slopeX, slopeY):
  currentX = 0
  currentY = 0

  treeCount = 0

  while currentY < len(inputRead):
    currentTile = inputRead[currentY][currentX]
    currentY += slopeY
    currentX += slopeX
    if(currentX > len(inputRead[0])-1):
      currentX -= len(inputRead[0])
    
    if currentTile == "#":
      treeCount += 1

  return treeCount

#solution 1
#print(solve(inputRead, 3, 1))

#solution 2
print( solve(inputRead, 1, 1) * solve(inputRead, 3, 1) *solve(inputRead, 5, 1) * solve(inputRead, 7, 1) * solve(inputRead, 1, 2) )