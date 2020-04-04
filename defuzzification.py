import matplotlib.pyplot as plt
import numpy as np
import funcoes as f
#modifique os valores de entrada d e p
d =0.1
p =0.6
y = []
x = [] 
altura,area =  0,0

for i in np.arange(0,1,0.01):
    y.append(f.altura(i,d,p))
    x.append(i)
    area += i*100*f.altura(i,d,p)
    altura +=f.altura(i,d,p)
                  
risco = area/altura
print('risco ', risco,' para dinheiro ',d,' e pessoal ',p)
plt.plot(x,y)
plt.show()





