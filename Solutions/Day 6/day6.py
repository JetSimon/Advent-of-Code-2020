inputRead = []

inputFile = open('input.txt', 'r') 

currentGroup = []
groups = []

totalCount = 0

for line in inputFile:
    stripped = line.rstrip()
    if(stripped != ''):
      currentGroup.append(stripped)
    else:
      groups.append(currentGroup)
      currentGroup = []
groups.append(currentGroup)

for group in groups:
  strGroup = "".join(group)
  for question in set(strGroup):
    if strGroup.count(question) == len(group):
      totalCount+=1

inputFile.close()

print(totalCount)