matrix = []
n=int(input())
ith=[]
jth=[]
count=0
cont=[]
for i in range(n):
   row = list(map(str, input().split()))
   matrix.append(row)

for i in range(n):
  for j in range(n):
    if(matrix[i][j]=="R"):
      ith.append(i)
      jth.append(j)
      count+=1
  cont.append(count)
  count=0
print(matrix)
print(ith,jth)
print(cont)
new_list = []
arrcnt=0
while cont:
    min = cont[0]  
    for x in cont: 
        if x < min:
            min = x
            arrcnt+=1
    new_list.append(min)
    cont.remove(min) 
print(arrcnt)
