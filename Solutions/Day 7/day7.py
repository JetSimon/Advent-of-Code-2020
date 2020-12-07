inputRead = []

inputFile = open('input.txt', 'r') 


for line in inputFile:
  stripped = line.rstrip()
  inputRead.append(stripped)

inputFile.close()


def getGoldenCount(b, rules):
    count = 0
    if(b == "no other bag"):
        return 0

    for bag in b:
        if(bag == "no other bag"):
            continue

        bagName = bag.split(" ", 1)[1]
        amount = int(bag.split(" ", 1)[0])

        if(bagName == "shiny gold bag"):
            return 1

        count += getGoldenCount(rules[bagName], rules)
    
    return count

def getBagsIn(contains, rules):

    if(contains == []):
        return 0
    count = len(contains)
    for bag in contains:
        count += getBagsIn(rules[bag], rules)
    return count

def GetContents(input, d):
    
    name = input.split("s contain ")[0]
    contents = input.split("s contain ")[1].split(",")

    for i in range(len(contents)):
        contents[i] = contents[i].replace('bags', 'bag').strip(",").strip(".").strip()
    
    d[name] = contents

def GetContents2(input, d):
    
    name = input.split("s contain ")[0]
    contents = input.split("s contain ")[1].split(",")
    out = []
    for i in range(len(contents)):
        contents[i] = contents[i].replace('bags', 'bag').strip(",").strip(".").strip()
        if(contents[i] == "no other bag"):
            out = []
            break
        bagName = contents[i].split(" ", 1)[1]
        amount = int(contents[i].split(" ", 1)[0])
        for i in range(amount):
            out.append(bagName)
    
    
    d[name] = out

def solve(inputRead):
    count = 0
    rules = {}
    
    for rule in inputRead:
        GetContents(rule, rules)

    for rule in rules:
        canContain = rules[rule]
        count += 1 if getGoldenCount(canContain, rules) >= 1 else 0

    return count

def solve2(inputRead):
    rules = {}
    
    for rule in inputRead:
        GetContents2(rule, rules)
    return getBagsIn(rules["shiny gold bag"], rules)

print(solve2(inputRead))

