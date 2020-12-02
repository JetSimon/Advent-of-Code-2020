inputRead = []

inputFile = open('input.txt', 'r') 

for line in inputFile:
  stripped = line.rstrip()
  inputRead.append(stripped)

inputFile.close()

def solve(inputRead):
    validCount = 0

    for line in inputRead:
        first = line.split(" ")
        low = int(first[0].split('-')[0])
        high = int(first[0].split('-')[1])
        letter = first[1][0]
        password = first[2].strip()

        if password.count(letter) >= low and password.count(letter) <= high:
            validCount+=1
            

    return validCount

def solve2(inputRead):
    validCount = 0

    for line in inputRead:
        first = line.split(" ")
        low = int(first[0].split('-')[0])
        high = int(first[0].split('-')[1])
        letter = first[1][0]
        password = first[2].strip()
        if (password[low-1] == letter or password[high-1] == letter):
            if(not (password[low-1] == letter and password[high-1] == letter)):
                validCount+=1
            

    return validCount

print(solve2(inputRead))