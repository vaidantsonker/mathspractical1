#program to transpose a matrix using a nested loop
x=[[5,6],
   [5,7],
   [3,4]]

result=[[0,0,0],
        [0,0,0]]

#iterate through rows
for i in range(len(x)):
    # iterate through columns
    for j in range (len(x[0])):
        result[j][i]= x[i][j]

for r in result:
     print(r)

