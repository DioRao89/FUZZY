# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:30:01 2018

Defuzzification by center of mass

"""

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
