#!/usr/bin/python

n=int(raw_input('Introduzca un numero n>0: '))
suma=0.0
for i in range(1,n+1):
  x_i=(i-1.0/2)/float(n)
  print'El valor de xi es: %f' % x_i
  print'Subintervalo: ', [(i-1.0)/float(n),i/float(n)]
  fx_i=4.0/(1+x_i**2)
  print'El valor de fx_i es: %f' % fx_i
  suma=suma + fx_i
pi=(1.0/n)*suma
print'El valor de pi es: pi=%.35f' % pi

Pi=3.1415926535897931159979634685441852
print'El valor de Pi es: Pi=%.35f' % Pi
