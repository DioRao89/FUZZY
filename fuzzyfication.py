import matplotlib.pyplot as plt

#fuzzy triangle
# receiving from keyboard
a,b,c = 140,240,300

while True:
    x = eval(input(" x value = "))
    tri = max(min((x-a)/(b-a),(c-x)/(c-b)),0)
    print (tri)


#two triangle functions
x_axis = list(range(0,500))
y_tri1 = [ ]
y_tri2 = [ ]
y_and = [ ]
a1,b1,c1= 140,240,340
a2,b2,c2= 240,340,440

for x in range(len(x_axis)):
    tri1 = max(min((x-a1)/(b1-a1),(c1-x)/(c1-b1)),0)
    tri2 = max(min((x-a2)/(b2-a2),(c2-x)/(c2-b2)),0)
    f_and = min(tri1,tri2)
    y_tri1.append(tri1)
    y_tri2.append(tri2)
    y_and.append(f_and)


plt.plot(x_axis,y_tri1,x_axis,y_tri2,x_axis,y_and)
plt.show()

#fuzzy trap trem
# receiving from keyboard
a,b,c,d = 140,240,300,400

while True:
    x = eval(input(" x value = "))
    trap = max(min((x-a)/(b-a),1,(d-x)/(d-c)),0)
    print (trap)

#ploting the graph


x_axis = list(range(0,500))
y_trap = []
a,b,c,d = 140,240,300,400
for x in range(len(x_axis)):
    trap = max(min((x-a)/(b-a),1,(d-x)/(d-c)),0)
    y_trap.append(trap)

print (y_trap)
plt.plot(x_axis,y_trap)
plt.show()


#fuzzy bell trem
c,a,b = 270,130,4
slope = -1*b/(2*a)
# receiving from keyboard
while True:
    x = eval(input(" x value = "))
    bell = 1/(1+((x - c)/a)**(2*b))
    print (bell)
###########################

#ploting the graph
import matplotlib.pyplot as plt

x_axis = list(range(0,500))
y_bell = []
c,a,b = 270,130,4
slope = -1*b/(2*a)

for x in range(len(x_axis)):
    bell = 1/(1+((x - c)/a)**(2*b))
    y_bell.append(bell)

plt.plot(x_axis,y_bell)
plt.show()
###########################
#GAUSSIAN MEMBERSHIP FUNCTION

import matplotlib.pyplot as plt
from math import exp
import numpy as np
c = 10
delta = 2
x_axis = list(np.arange(0,20,0.2))
y_gauss = []

for x in x_axis:
    gauss = exp(-0.5*((x-c)/delta)**2)
    y_gauss.append(gauss)
#rodar separado
plt.plot(x_axis,y_gauss,'gs')
plt.show()

#aula - lab sistemas
# salvar como fuzzy.py
#soluçao parcial recebendo do teclado
a,b,c = 10,11,12
while True:
    x = eval(input("digite o valor de x "))
    tri = max(min((x-a)/(b-a),(c-x)/(c-b)),0)
    tri

# plotagem do grafico
import matplotlib.pyplot as plt
# lista de valores de x
x_axis = list(range(0,15)) # lista com valores de 0 a 15
y_axis = []                # lista vazia para valores da funcao fuzzy
a,b,c = 10,11,12
for x in x_axis:
    tri = max(min((x-a)/(b-a),(c-x)/(c-b)),0)
    y_axis.append(tri)

plt.plot(x_axis,y_axis,'--r')
plt.show()
###############################################################
#resolucao analise de risco

import matplotlib.pyplot as plt
x_axis = list(range(0,101))
din_inadequado = []
din_medio = []
din_adequado = []
pessoal_baixo = []
pessoal_alto = []
b1,c1= 30,50 #din_inadequado
a2,b2,c2= 30,50,70 #din_medio
a3,b3 = 50,70 #din_adequado
b4,c4 = 30,70 #pessoal_baixo
a5,b5 = 30,70 #pessoal_alto
for x in range(len(x_axis)):
    #funcao de pertinencia triangular
    valor_inadequado = max(min((c1-x)/(c1-b1),1),0)
    valor_medio = max(min((x-a2)/(b2-a2),(c2-x)/(c2-b2)),0)
    valor_adequado = max(min((x-a3)/(b3-a3),1),0)
    valor_baixo = max(min((c4-x)/(c4-b4),1),0)
    valor_alto = max(min((x-a5)/(b5-a5),1),0)
    din_medio.append(valor_medio)
    din_inadequado.append(valor_inadequado)
    din_adequado.append(valor_adequado)
    pessoal_baixo.append(valor_baixo)
    pessoal_alto.append(valor_alto)
plt.plot(x_axis,din_medio)
plt.plot(x_axis,din_inadequado)
plt.plot(x_axis,din_adequado)

plt.show()

import matplotlib.pyplot as plt
x_axis = list(range(0,101))
risco_pequeno = []
risco_medio = []
risco_alto = []
b1,c1 = 35,60
a2,b2,c2 = 35,60,85
a3,b3 = 60,85
for x in range(len(x_axis)):
    #funcao de pertinencia triangular
    valor_pequeno = max(min((c1-x)/(c1-b1),1),0)
    valor_medio = max(min((x-a2)/(b2-a2),(c2-x)/(c2-b2)),0)
    valor_alto = max(min((x-a3)/(b3-a3),1),0)
    risco_pequeno.append(valor_pequeno)
    risco_medio.append(valor_medio)
    risco_alto.append(valor_alto)
plt.plot(x_axis,risco_medio)
plt.plot(x_axis,risco_alto)
plt.plot(x_axis,risco_pequeno)
plt.show()
# base de regras
""""
1. Se dinheiro é adequado ou
pessoal é baixo então risco
é pequeno
2.  Se dinheiro é médio e pessoal
é alto, então risco é normal
3.  Se dinheiro é inadequado,
então risco é alto"""
#recebe valor de x = dinhheiro,y = pessoal
x = 35
y = 60
#regra 1
a3,b3 = 50,70 #din_adequado
b4,c4 = 33.3,66.7 #pessoal_baixo
valor_adequado = max(min((x-a3)/(b3-a3),1),0)
valor_baixo = max(min((c4-y)/(c4-b4),1),0)
# conectivo ou
risco_pequeno = max(valor_adequado,valor_baixo)
risco_pequeno
#regra 2
a2,b2,c2= 30,50,70 #din_medio
a5,b5 = 33.3,66.7    #pessoal_alto
valor_medio = max(min((x-a2)/(b2-a2),(c2-x)/(c2-b2)),0)
valor_alto  = max(min((y-a5)/(b5-a5),1),0)
# conectivo e
risco_medio = min(valor_medio,valor_alto)
#regra 3
b1,c1= 30,50 #din_inadequado
valor_inadequado = max(min((c1-x)/(c1-b1),1),0)
# conectivo condicional
risco_alto = valor_inadequado

risco_pequeno
risco_medio
risco_alto

#centro de massa

cm = (10+20+30+40)*risco_pequeno+(50+60+70)*risco_medio+(80+90+100)*risco_alto
cm = cm/(4*risco_pequeno+3*risco_medio+3*risco_alto)
cm 
