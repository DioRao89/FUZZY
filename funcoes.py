from numpy import exp
import numpy as np
def tri(x,a1,b2,c3):
    return max(min((x-a1)/(b2-a1),(c3-x)/(c3-b2)),0)
def bell(x,b,c):
   return 1/(1+((x-c)/b)**(2*b))
def gauss(x, delta, c):
    return exp(-0.5*((x-c)/delta)**2)
def trap(x,d1,d2,d3,d4):
    return max(min((x-d1)/(d2-d1),1,(d4-x)/(d4-d3)),0)

def fdinheiro_inadequado(x):
    return trap(x,-1,0,0.3,0.5)
def fdinheiro_medio(x):
    return tri(x,0.3,0.5,0.8)
def fdinheiro_adequado(x):
    return trap(x,0.5,0.8,1,1.5)

def frisco_peq(x):
    return trap(x,-1,0,0.3,0.6)
def frisco_norm(x):
    return tri(x,0.4,0.6,0.85)
def frisco_alto(x):
    return trap(x,0.6,0.85,1,1.5)

def fpessoa_baixo(x):
    return trap(x,-1,0,0.2,0.7)
def fpessoa_alto(x):
    return trap(x,0.2,0.7,1,1.5)

def altura(x,d,p):
    #se dinheiro adequado ou pessoal baixo entao risco pequeno
    risco_peq = max(fdinheiro_adequado(d),fpessoa_baixo(p))
    #se dinheiro medio E pessoa alto entao risco med
    risco_med =min(fdinheiro_medio(d),fpessoa_alto(p))
    #se din inadequado entao risco maximo
    risco_max = fdinheiro_inadequado(d)
    risco_peq = min(risco_peq,frisco_peq(x))
    risco_med = min(risco_med,frisco_norm(x))
    risco_max = min(risco_max,frisco_alto(x))
    
    return max(risco_max,risco_peq,risco_med)

def centroide(d,p):
    area = 0
    altura = 0
    for i in np.arange(0,1.01,0.01):
            area += i*100*altura(i,d,p)
            altura +=altura(i,d,p)
        #print('dinheiro',d, 'pessoa ',p,'risco ',area/altura)    
    return area/altura