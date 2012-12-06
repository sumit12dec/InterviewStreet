#Problem statement link below
#https://www.interviewstreet.com/challenges/dashboard/#problem/4efa210eb70ac


no_of_testcases = int(raw_input())
testcases=[]
s=[[],[],[]]
final=[]
a=[]
for m in range(0,no_of_testcases):
    testcases.append(raw_input())
for i in range(0,no_of_testcases):
  leng=len(testcases[i])
  for y in range(0,leng):
    for k in range(1,leng+1):
      suffix1=testcases[i][y:k]
      if suffix1 not in s[i] and len(suffix1)>0:
        s[i].append(suffix1)
for p in range(0,no_of_testcases-1):
  for q in range(0,len(s[p])):
    if (s[p][q] == s[p+1][q]):
     if s[p][q] not in final:
      final.append(s[p][q])
    else:
     if s[p][q] not in final:
      final.append(s[p][q])
     if s[p+1][q] not in final:
      final.append(s[p+1][q])

no_of_queries = int(raw_input())
for m in range(0,no_of_queries):
    a.append(int(raw_input()))
for each in a:
  if each>len(final):
   print "INVALID"
  else:
    print final[each-1]