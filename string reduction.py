

#Problem Statement link below
#https://www.interviewstreet.com/challenges/dashboard/#problem/4eac48496bee2

# Enter your code here. Read input from STDIN. Print output to STDOUT
c1=["ab","ba"]
c2=["ac","ca"]
c3=["bc","cb"]
testcases=[]
no_of_testcases = int(raw_input())
for m in range(0,no_of_testcases):
    testcases.append(raw_input())

for i in range(0,no_of_testcases):
  j=2
  k=0
  mu=len(testcases[i])
  for o in range(0,mu+3):
    if testcases[i][k:j] in c1:
        if j!=2 and k!=0:
          testcases[i]=testcases[i][:k]+'c'+testcases[i][j:]
        else:
          testcases[i]='c'+testcases[i][j:]
        j=2
        k=0
    elif testcases[i][k:j] in c2:
        if j!=2 and k!=0:
          testcases[i]=testcases[i][:k]+'b'+testcases[i][j:]
        else:
          testcases[i]='b'+testcases[i][j:]
        j=2
        k=0
    elif testcases[i][k:j] in c3:
        if j!=2 and k!=0:
          testcases[i]=testcases[i][:k]+'a'+testcases[i][j:]
        else:
          testcases[i]='a'+testcases[i][j:]
        j=2
        k=0
    else:
        j=j+1
        k=k+1

for i in range(0,no_of_testcases):
  print len(testcases[i])