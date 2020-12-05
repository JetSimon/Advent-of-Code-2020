import math



def FillArray(n):
    out = []
    for i in range(0,n):
        out.append(i)
    return out

def GetSeat(id):
    
    row = FillArray(128)
    
    col = FillArray(8)

    #Get row
    for i in range(0,7):
        if(id[i] == "F"):   
            row = row[0:len(row)/2]
        elif(id[i] == "B"):   
            row = row[len(row)/2:len(row)]
    
    #Get col
    for i in range(7,10):
        if(id[i] == "L"):   
            col = col[0:len(col)/2]
        elif(id[i] == "R"):   
            col = col[len(col)/2:len(col)]
    
    if(row[0] == 127 or row[0] == 0):
        print("nad")
        return -1

    return (row[0] * 8) + col[0]

inputRead = []

inputFile = open('input.txt', 'r') 

for line in inputFile:
  stripped = line.rstrip()
  seat = GetSeat(stripped)
  if(seat != -1):
    inputRead.append(seat)

inputFile.close()

inputRead = sorted(inputRead)

lastSeat = inputRead[0]
for i in range(1, len(inputRead)):
    if(lastSeat+1 != inputRead[i]):
        
        print(inputRead[i])
    lastSeat = inputRead[i]