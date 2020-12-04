inputRead = []
pattern = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
eyes = ['amb','blu','brn','gry','grn','hzl','oth']
inputFile = open('input.txt', 'r') 
current = ""

for line in inputFile:
    stripped = line.rstrip()
    if(stripped != ''):
        current+=stripped+" "
    else:
        inputRead.append(current)
        current = ""

inputRead.append(current)



count = 0

for passport in inputRead:
    passportInfo = passport.split(" ")
    fieldsIn=[]
    for field in passportInfo:
        if(field!=""):
            var = field.split(":")[0]
            amt = field.split(":")[1]

            if(var == "byr"):
                if(int(amt) >= 1920 and int(amt) <= 2002):
                    if(var not in fieldsIn):
                        fieldsIn.append(var)
            if(var == "iyr"):
                if(int(amt) >= 2010 and int(amt) <= 2020):
                    if(var not in fieldsIn):
                        fieldsIn.append(var)
            
            if(var == "eyr"):
                if(int(amt) >= 2020 and int(amt) <= 2030):
                    if(var not in fieldsIn):
                        fieldsIn.append(var)
            
            if(var == "hgt"):
                if(amt[-2] + amt[-1] == "cm"):
                    hgt = int(amt.split("c")[0])
                    if(hgt >= 150 and hgt <= 193):
                        if(var not in fieldsIn):
                            fieldsIn.append(var)
                if(amt[-2] + amt[-1] == "in"):
                    hgt = int(amt.split("i")[0])
                    if(hgt >= 59 and hgt <= 76):
                        if(var not in fieldsIn):
                            fieldsIn.append(var)
            
            if(var == "hcl"):
                if(amt[0] == "#"):
                    matches = True
                    for c in amt[1:]:
                        if(c not in pattern):
                            matches = False
                    if(matches and len(amt) == 7):
                        if(var not in fieldsIn):
                            fieldsIn.append(var)
            
            if(var == "ecl"):
                if(len(amt) == 3 and amt in eyes):
                    if(var not in fieldsIn):
                        fieldsIn.append(var)

            if(var == "pid"):
                if(len(amt) == 9 and amt.isdigit()):
                    if(var not in fieldsIn):
                        fieldsIn.append(var)
    
    if(len(fieldsIn) == 7):
        #print(passport)
        count+=1

print(count)