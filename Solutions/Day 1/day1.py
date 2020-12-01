inputRead = []

inputFile = open('input.txt', 'r') 

for line in inputFile:
  stripped = line.rstrip()
  inputRead.append(int(stripped))

inputFile.close()

def solution(input):
    for i in range(len(input)):
        num1 = int(input[i])
        for j in range(len(input)):
            num2 = input[j]
            if(i!=j and num1 + num2 == 2020):
                return num1 * num2
    return None

def solution2(input):
    for i in range(len(input)):
        num1 = int(input[i])
        for j in range(len(input)):
            num2 = input[j]
            for k in range(len(input)):
                num3 = input[k]
                if(i!=j and j!=k and num1+num2+num3 == 2020):
                    return num1 * num2 * num3
    return None

print(solution2(inputRead))