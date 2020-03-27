import numpy as np
import matplotlib.pyplot as plt 

x = [1,2,3,4,5,6,7,8,9,10]
conf = [0.2,0.5,0.8,1,0.7,0.3,0,0,0,0]
gran = [0,0,0.2,0.4,0.6,0.8,1,1,1,1]
#complementar - nao grande = pequeno
peq = []
des = []
conf_e_gran= []
# muito
muito_conf = np.power(conf,4)
for i,_ in enumerate(x):
    peq.append(abs(gran[i]-1))
    des.append(abs(conf[i]-1))
    conf_e_gran.append(min(conf[i],gran[i]))
    
plt.plot(x,conf, x,muito_conf)
plt.show()

#solteirao
filhos = [0,1,2,3,4,5,6]
galeto = [1,0.8,0.6,0,0,0,0]
creche = [0,0.2,0.5,0.9,1,1,1]
#complementar - nao grande = pequeno

plt.plot(filhos,galeto, filhos,creche)
plt.show()


