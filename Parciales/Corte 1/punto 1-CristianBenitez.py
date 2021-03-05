#Cristian Camilo Benitez
from math import*

# Defining Function
def f(x): 
    return sin(x)+1 

# Implementing Secant Method

def secant(x0,x1,e,N):
    print('\n\n*** Metodo de la secante ***')
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break
        
        x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
        print('Iteracion-%d, x2 = %0.6f y f(x2) = %0.6f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step > N:
            print('No Convergente!')
            break
        
        condition = abs(f(x2)) > e
    print('\n Raiz aprox.: %0.8f' % x2)


x0 = input('Primer valor: ')
x1 = input('Segundo valor: ')
N = input('Max iteraciones: ')

x0 = float(x0)
x1 = float(x1)
e = 10**-16

N = int(N)


# Starting Secant Method
secant(x0,x1,e,N)