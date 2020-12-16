rulesRaw = []

ticket = []

otherTickets = []

inputFile = open('input.txt', 'r') 

readingInto = rulesRaw
for line in inputFile:
  stripped = line.rstrip()
  if(stripped == "your ticket:"):
    readingInto = ticket
    continue
  elif(stripped == "nearby tickets:"):
    readingInto = otherTickets
    continue
  readingInto.append(stripped)

inputFile.close()

def InRange(n, rangeString):
  n = int(n)
  return n >= int(rangeString.split("-")[0]) and n <= int(rangeString.split("-")[1])

def FollowsRule(n, field):
  return InRange(n, field[0]) or InRange(n, field[1])

def FollowsAllRules(n, rules):
  for rule in rules.keys():
    if(not FollowsRule(n , rules[rule])):
      return False
  return True

def FollowsAnyRules(n, rules):
  for rule in rules.keys():
    if(FollowsRule(n , rules[rule])):
      return True
  return False

def ParseRules(rulesRaw):
  rules = {}
  for rule in rulesRaw:
    fieldName = rule.split(":")[0]
    range1 = rule.split(":")[1].split("or")[0].strip()
    range2 = rule.split(":")[1].split("or")[1].strip()
    rules[fieldName] = [range1, range2]
  return rules


def GetValidTickets(rules, nearbyTickets):
  valids = []
  for ticket in nearbyTickets:
    parsedTicket = ticket.split(",")
    valid = True
    for value in parsedTicket:
      if not FollowsAnyRules(int(value), rules):
        valid = False
    if valid:
      valids.append(parsedTicket)
    
  return valids

def GetNameForIndex(rules, validTickets, i, alreadyUsed):
  options = []
  for rule in rules.keys():
    follows = True
    for ticket in validTickets:
      if(not FollowsRule(ticket[i], rules[rule])):
        follows=False
    if(follows and rule not in alreadyUsed):
      options.append(rule)
  if(len(options) != 1):
    return None
  alreadyUsed.append(options[0])
  return options[0]

def solve(rulesRaw, nearbyTickets):
  rules = ParseRules(rulesRaw)
  errors = 0
  for ticket in nearbyTickets:
    parsedTicket = ticket.split(",")
    for value in parsedTicket:
      errors += int(value) if not FollowsAnyRules(int(value), rules) else 0
  return errors

def solve2(rulesRaw, nearbyTickets, yourTicketRaw):
  out = {}
  yourTicket = yourTicketRaw[0].split(",")
  rules = ParseRules(rulesRaw)
  numberOfRules = len(rules)
  validTickets = GetValidTickets(rules, nearbyTickets)
  alreadyUsed=[]

  while len(alreadyUsed) != numberOfRules:
    for i in range(len(yourTicket)):
      name = GetNameForIndex(rules, validTickets, i, alreadyUsed)
      if(name != None):
        out[name] = int(yourTicket[i])

  count = 1
  for key in out.keys():
    if(key[0:9] == "departure"):
      count *= out[key]

  return count

  
print(solve2(rulesRaw, otherTickets, ticket))

