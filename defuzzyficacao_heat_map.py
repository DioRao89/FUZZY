import matplotlib.pyplot as plt
import numpy as np
import funcoes as f
##d = 0.35
##p = 0.6
 #vetor risco
#vr = np.zeros(100,100)
 
        ##base(i)*altura(i)
#implementar integral... 
# vd vetores de inteiros e modificar atributos a serem passados para altura... 
'''
############################################################################
## esse aqui ta funcionando
vd = list(np.arange(0,1.01,0.01)) #vetor dineiro
vp = list(np.arange(0,1.01,0.01)) #vetor pessoa
u = -1
uvet = []
vvet = []
for d in vd:
    u+=1
    v = -1
    for p in vp:
        v+=1
        area = 0
        alt = 0       
        for i in np.arange(0,1.01,0.01):
            area += i*100*f.altura(i,d,p)
            alt +=f.altura(i,d,p)
        vvet.append( area/alt)
        #print('dinheiro',u, 'pessoa ',v,'risco ',area/alt)    
    uvet.append(vvet)
    vvet=[]
vr = uvet
############################################################################
''' 
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
