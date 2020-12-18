problems = []




inputFile = open('input.txt', 'r') 


for line in inputFile:
  stripped = line.rstrip()
  problems.append(list(stripped.replace(" ", "")))

inputFile.close()

def GetStartEnd(problem):
  l=1
  r=0

  leftIndex = problem.index("(")
  rightIndex = None

  
  #(())
  for i in range(leftIndex+1, len(problem)):
    c = problem[i]
    r += 1 if c == ")" else 0
    l += 1 if c == "(" else 0
    if(l == r):
      rightIndex = i
      break
    
    #print(c + " l count: " + str(l) + " r count: " + str(r) + " at index: " + str(i))
   
    
  out = (leftIndex, rightIndex)
  #print("".join(problem))
  #print(out)
  return out
    
    

def RemovePar(problem):
  if("(" in problem or ")" in problem):
    startEnd = GetStartEnd(problem)
    left = startEnd[0]
    right = startEnd[1]
    sub = problem[left+1:right]
    sub = Evaluate(sub)
    problem[left] = sub
    del problem[left+1:right+1]
    return RemovePar(problem)
    
  else:
    return problem

def RemovePar2(problem):
  #print("".join(problem))
  if("(" in problem or ")" in problem):
    startEnd = GetStartEnd(problem)
    left = startEnd[0]
    right = startEnd[1]
    sub = problem[left+1:right]
    sub = Evaluate2(sub)
    problem[left] = sub
    del problem[left+1:right+1]
    return RemovePar2(problem)
    
  else:
    return problem

def Evaluate(problem):
  #print("".join(problem))
  problem = RemovePar(problem)
  
  #solve plain problem
  while len(problem) > 1:
    x = "".join(problem[0:3])
    x = str(eval(x))
    problem.pop(0)
    problem.pop(0)
    problem.pop(0)
    problem.insert(0, x)
  
  return problem[0]

def Evaluate2(problem):
  
  #print("".join(problem))
  problem = RemovePar2(problem)
  
  #solve plain problem
  while len(problem) > 1:
    
    if("+" not in problem):
      return str(eval("".join(problem)))
    else:
      for i in range(0, len(problem)):
        print(problem)
        if("+" not in problem):
          return str(eval("".join(problem)))
        chunk = problem[i:i+3]
        if(len(chunk)==3):
          if(chunk[1] == "+"):
            x = eval("".join(chunk))
            problem.insert(i, str(x))
            del problem[i+1:i+4]
        
  
  return problem[0]



def solve(problems):
  sum=0
  for problem in problems:
    sum += int(Evaluate(problem))
  return sum

def solve2(problems):
  sum=0
  for problem in problems:
    print("PROBLEM IS " + "".join(problem))
    sum += int(Evaluate2(problem))
  return sum


#print(GetStartEnd(problems[0]))
print(solve2(problems))