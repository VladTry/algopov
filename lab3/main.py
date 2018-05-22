f = open("data.txt")

def isAll(a, x):
  for i in range(x):
    if a[i] == 0:
      return False
  return True

i = 0
A=[]

for line in f:
  if i == 0:
    num = line.split("X=")
    x= int(num[1])
  else:
    A.append(int(line))
  i+=1

alls =[]

for i in range(x):
  alls.append(0)

s=0

for i in A:
  alls[i-1] = 1
  if isAll(alls, x) == True:
    break
  else:
    s+=1

print ("Second = " + str(s))

