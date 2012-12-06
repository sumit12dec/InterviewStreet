#Problem Statement link below
#https://www.interviewstreet.com/challenges/dashboard/#problem/4f304a3d84b5e


N = int(raw_input())
tmp1={}
tmp2={}
for i in range(0, N):
    tmp1[i] = raw_input()
    tmp2[i] = raw_input()
    if i<N-1:
      tmp     = raw_input()
for st in range(0,N):
   tom1=tmp1[st]
   tom2=tmp2[st] 
   t1=len(tom1)
   t2=len(tom2)
   m=t1-t2
   for k in xrange(m+1):  
       s=k
       count=0
       for j in xrange(t2):
           if tom1[s]==tom2[j]:
               count=count+1
           s=s+1
       if count==t2-1 or count==t2:
           print k,
   print "\n",