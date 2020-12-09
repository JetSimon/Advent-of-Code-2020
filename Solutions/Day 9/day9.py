inputRead = []

inputFile = open('input.txt', 'r') 


for line in inputFile:
  stripped = line.rstrip()
  inputRead.append(int(stripped))

inputFile.close()

def isSumOfTwo(n,numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                if(numbers[i] + numbers[j] == n):
                    return True
    return False

def solve(numbers, preamble):
    current = preamble
    for i in range(current, len(numbers)):
        num = numbers[i]
        chunk = numbers[i-preamble:i]
        if(not isSumOfTwo(num, chunk)):
            return num
    return None



def solve2(numbers, preamble):
    toAddTo = solve(numbers, preamble)
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            chunk = numbers[i:j]
            if(sum(chunk) == toAddTo):
                return min(chunk) + max(chunk)
    return None

print(solve2(inputRead, 25))