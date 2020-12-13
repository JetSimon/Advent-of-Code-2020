#currentTime = 939
#currentTime = 1000508

#busses = "7,13,x,x,59,x,31,19"
busses = "29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,467,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,19,x,x,x,x,x,x,x,x,x,x,x,443,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41"

def solve(bussesRaw, currentTime):
  busses = []
  for t in bussesRaw.split(","):
    if(t != "x"):
      busses.append(int(t))
  
  timeToReturn=None
  smallest = 99999999

  for time in busses:
    timeTried = time
    while timeTried < currentTime:
      timeTried+=time
    
    toWait = timeTried - currentTime

    if(toWait < smallest):
      smallest = toWait
      timeToReturn = time

  return timeToReturn * smallest

def solve2(bussesRaw):
  busses = []
  for t in bussesRaw.split(","):
    if(t != "x"):
      busses.append(int(t))
    else:
      busses.append("x")

  mods = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
  
  vals = list(reversed(sorted(mods)))
  val = mods[vals[0]]
  r = vals[0]
  for b in vals[1:]:
      while val % b != mods[b]:
          val += r
      r *= b
  return val
  

print(solve2(busses))