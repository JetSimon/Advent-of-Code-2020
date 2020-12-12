from math import sin, cos, radians
directions = []

inputFile = open('input.txt', 'r') 


for line in inputFile:
  stripped = line.rstrip()
  directions.append(stripped)

inputFile.close()

def solve(instructions):
  directions = ["east", "south", "west", "north"]
  direction = directions[0]
  x=0
  y=0
  for instruction in instructions:
    way = instruction[0]
    amount = int(instruction[1:])

    y+=amount if way == "N" else 0
    y-=amount if way == "S" else 0
    x+=amount if way == "E" else 0
    x-=amount if way == "W" else 0

    if way == "F":
      y+=amount if direction == "north" else 0
      y-=amount if direction == "south" else 0
      x+=amount if direction == "east" else 0
      x-=amount if direction == "west" else 0
    
    if way == "R":
      toTurn = int(amount / 90)
      currentDirectionIndex = directions.index(direction)
      newDirectionIndex = currentDirectionIndex + toTurn
      while newDirectionIndex >= len(directions):
        newDirectionIndex -= len(directions)
      direction = directions[newDirectionIndex]

    if way == "L":
      toTurn = int(amount / 90)
      currentDirectionIndex = directions.index(direction)
      newDirectionIndex = currentDirectionIndex - toTurn
      while newDirectionIndex < 0:
        newDirectionIndex += len(directions)
      direction = directions[newDirectionIndex]
    
    print(direction)
  
  return abs(x) + abs(y)

def solve2(instructions):
  directions = ["east", "south", "west", "north"]
  direction = directions[0]
  wx=10
  wy=1
  x=0
  y=0
  for instruction in instructions:
    way = instruction[0]
    amount = int(instruction[1:])

    wy+=amount if way == "N" else 0
    wy-=amount if way == "S" else 0
    wx+=amount if way == "E" else 0
    wx-=amount if way == "W" else 0

    if way == "F":
      
      #offset
      ox = wx - x
      oy = wy - y

      y += oy * amount
      x += ox * amount

      wy = y + oy
      wx = x + ox

    if way == "R" or way == "L":
      toTurn = -radians(int(amount))

      if way == "L":
        toTurn *= -1

      x1 = wx - x
      y1 = wy - y

      x2 = x1 * cos(toTurn) - y1 * sin(toTurn)
      y2 = x1 * sin(toTurn) + y1 * cos(toTurn)

      wx = x2 + x
      wy = y2 + y

 


  return int(abs(x) + abs(y))

print(solve2(directions))