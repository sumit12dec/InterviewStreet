
#Problem Statement link below
#https://www.interviewstreet.com/challenges/dashboard/#problem/4edb8abd7cacd

no_of_testcases = int(raw_input())
testcases=[]
count=[0,0,0,0,0,0,0,0,0,0]
for m in range(0,no_of_testcases):
    testcases.append(raw_input())
for i in range(0,no_of_testcases):
  leng=len(testcases[i])
  for k in range(0,leng):
    c=0
    suffix=testcases[i][k:]
    if testcases[i][0]==suffix[0]:
      for z in range(0,len(suffix)):
         if testcases[i][z]==suffix[z]:
          c=c+1
         else:
           break;
      count[i]=count[i]+c

for i in range(0,no_of_testcases):
 print count[i]