InterviewStreet
===============

Python Codes of Problem Solved on InterviewStreet
#Problem Statement link below
#https://www.interviewstreet.com/challenges/dashboard/#problem/4fcf919f11817

def func():
       r.sort()
       if len(r)%2==0:
                 tera=(r[(len(r)/2)]+r[(len(r)/2)-1])/2.0
                 if tera.is_integer():
                    print int(tera)
                 else:
               tera=str(tera)
          	     print tera
       else:
           print r[len(r)/2]

N = int(raw_input())

s = []
x = []
r = []
for i in range(0, N):

	tmp = raw_input()
	a, b = [xx for xx in tmp.split(' ')]
	s.append(a)
	x.append(int(b))

for each,each1 in zip(s,x):
  if each=='r': 
        if each1 not in r: 
           print"Wrong!"
        else:
          r.remove(each1)
          if len(r)==0:
            print "Wrong!"
          else:
           func()
   
  else:
       r.append(each1)
       func()