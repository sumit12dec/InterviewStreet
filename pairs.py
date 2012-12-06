#Problem Statement link below
#


no_of_testcases,diff = raw_input().split()
no_of_testcases=int(no_of_testcases)
diff=int(diff)
testcase=[]
count=0
testcase= raw_input().split()
for i in range(0,len(testcase)):
  testcase[i]=int(testcase[i])
testcase.sort()
for j in range(0,len(testcase)):
  for k in range(j+1,len(testcase)):
     if testcase[k]-testcase[j]==2:
       count=count+1
       break
print(count)