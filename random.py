#formula used:  Xn+1=(a.Xn + c)%m  here m=2^b , a = 5+8*k , k=1,2,3,4----

#random number generate and plot

import matplotlib.pyplot as plt # library to plot data

#random number generator function parameter
#intial value of x is seed value(determine sequence of random number generated)
#k,c and b parameter determine characteristics of generated random number
#n is number of generated random number
#k,c and b is a positive integer ,for good randomness b should be greater than 10
#put n less than or equal to 2^b-2 if n>2^b-2 then pattern of generated number is repeated(pseudo random number)

def RndGen(x,k,c,b,n):
      m=2**b
      a=5+8*k
      l=[x]
      t=[0]
      for i in range(1,n):
          x=(a*x+c)%m
          l.append(x)
          t.append(i)
      return [l,t]

#test case        

p=RndGen(3,1,0,15,8192)
print(p[0]) #print the random number list
plt.plot(p[1],p[0],'.')
plt.show()


