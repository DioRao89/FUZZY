'''
AUTHOR: DIONISIO RIBEIRO
13/04/2019
RISK ANALYSIS WITH COLORMAP
'''

import matplotlib.pyplot as plt
import numpy as np
import funcoes as f

paced = 0.01
pacep = 0.01
vd = list(np.arange(0,1.01,paced)) #vetor dinheiro
vp = list(np.arange(0,1.01,pacep)) #vetor pessoa
vet = []
vr = [] #vetor risco
'''
#inicializacao dos vetores
for d in vd:
    for p in vp:
        vet.append((d,p))
    vr.append(vet)
    vet = []
'''    
for d in vd:
    for p in vp:
        area = 0
        alt = 0       
        for k in np.arange(0,1.01,0.01):
            area += k*100*f.altura(k,d,p)
            alt +=f.altura(k,d,p)
        vet.append(area/alt)
    vr.append(vet)
    vet = []           
#plt.imshow(vr)
plt.matshow(vr,cmap='jet')
plt.xlabel('PESSOAS')
plt.ylabel('DINHEIRO')
#plt.title('HEAT_MAP_FUZZY') 
plt.colorbar(label='RISCO')
plt.show()
