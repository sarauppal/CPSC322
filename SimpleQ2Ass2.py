#!/usr/bin/env python
# coding: utf-8

# In[92]:


import numpy as np


# In[127]:



A=[1,2,3,4]
B=[1,2,3,4]
C=[1,2,3,4]
D=[1,2,3,4]
E=[1,2,3,4]
F=[1,2,3,4]
G=[1,2,3,4]
H=[1,2,3,4]

Constraints={'a':[],
             'b':[],
             'c':[],
             'd':['d!=c'],
             'e':['e!=c','e<(d-1)'],
             'f':['abs(f-b)==1','c!=f','d!=f','abs(e-f)%2!=0'],
             'g':['a>=g','abs(g-c)==1','d>=g','g!=f'],
             'h':['a<h','g<h','abs(h-c)%2==0','h!=d','e!=(h-2)','h!=f']}
    
#def consistent(V,constraint):
    
    
    


# In[146]:


models=np.array([])
for a in A:
    print('\n a={0}'.format(a),end="")
    for b in B:
        print(' \t b={0}'.format(b),end="")
        for c in C:
            print(' \t c={0}'.format(c) ,end="")
            for d in D:
                print(' \t d={0}'.format(d), end="")
                for constraint in Constraints['d']:
                    if not eval(constraint):
                        print(' \t  -> failure '.format(d))
                        flag=1
                        break
                if flag:
                    flag=0
                    continue
                
                for e in E:
                    print('\t e={0}'.format(e),end="")
                    for constraint in Constraints['e']:
                        if not eval(constraint):
                            print('\t  -> failure'.format(e))
                            flag=1
                            break
                    if flag:
                        flag=0
                        continue        
                            
                    for f in F:
                        print('\t f={0}'.format(f),end="")
                        for constraint in Constraints['f']:
                            if not eval(constraint):
                                print('\t  -> failure'.format(f))
                                flag=1
                                break
                        if flag:
                            flag=0
                            continue  
                            
                        for g in G:
                                print('\t g={0}'.format(g),end="")
                                for constraint in Constraints['g']:
                                    if not eval(constraint):
                                        print('\t -> failure'.format(g))
                                        flag=1
                                        break  
                                        
                                if flag:
                                    flag=0
                                    continue
                                    
                                    
                                for h in H:
                                    print('\t h={0}'.format(h),end="")
                                    for constraint in Constraints['h']:
                                        if not eval(constraint):
                                            print('\t  -> failure'.format(h))
                                            flag=1
                                            break
                                            
                                    if flag:
                                        flag=0
                                        continue
                                                                            
                                    print("Yay! we have a model")
                                    model=np.array([a,b,c,d,e,f,g,h])
                                    if not models.size:
                                        models=model
                                    else:
                                        models=np.vstack((models,model))
                                                                        
                                                                
                                                            
                                                
                                            
                                            
                                            
                                            
                                            


# In[140]:


models

