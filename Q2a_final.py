#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
from itertools import islice


# ## Initialize Domains

# In[13]:



A=[1,2,3,4]
B=[1,2,3,4]
C=[1,2,3,4]
D=[1,2,3,4]
E=[1,2,3,4]
F=[1,2,3,4]
G=[1,2,3,4]
H=[1,2,3,4]

    
def consistent(V,Constraints):
    V=V
    for constraint in Constraints:
        if not eval(constraint):
            return False
        
    return True    
        
            
        
            

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

    


# ## Define Constraints as dict

# In[14]:


Constraints={'a':[],
             'b':[],
             'c':[],
             'd':["V['d']!=V['c']"],
             'e':["V['e']!=V['c']","V['e']<(V['d']-1)"],
             'f':["abs(V['f']-V['b'])==1","V['c']!=V['f']","V['d']!=V['f']","abs(V['e']-V['f'])%2!=0"],
             'g':["V['a']>=V['g']","abs(V['g']-V['c'])==1","V['d']>=V['g']","V['g']!=V['f']"],
             'h':["V['a']<V['h']","V['g']<V['h']","abs(V['h']-V['c'])%2==0","V['h']!=V['d']","V['e']!=(V['h']-2)","V['h']!=V['f']"]}


# In[15]:


Constraints['e']
V={'c': 4, 'd': 3,'e':2}
if not eval(Constraints['e'][1]):
    print("True")
else: 
    print("False")


# In[16]:


d=3
c=4
e=2
V={'c': 2, 'd': 6,'e':2}
if consistent(V,Constraints['e']):
    print("satisfied")
else:
    print("Insatiable")


# I couldn't print it the way it shows in the assignment. See if it works for you.

# In[29]:


assignment={}
models=np.array([])
count=0
space='\t'
for a in A:
    assignment['a']=a
    n_items = take(1, assignment.items())
    print(n_items) 
    time=1
    for b in B:
        assignment['b']=b
        n_items = take(2, assignment.items())
        print(n_items)   
        time+=1
        for c in C:
            assignment['c']=c
            n_items = take(3, assignment.items())
            print(n_items)   
            time+=1
            for d in D:
                assignment['d']=d
                n_items = take(4, assignment.items())
                print(n_items)
                if not consistent(assignment,Constraints['d']):
                    count+=1
                    print("********************************************* - > Failure")
                    continue
                
                for e in E:
                    assignment['e']=e
                    n_items = take(5, assignment.items())
                    print(n_items)
                    if not consistent(assignment,Constraints['e']):
                        count+=1
                        print("********************************************* - > Failure")
                        continue
                   
                        
                            
                    for f in F:
                        assignment['f']=f
                        n_items = take(6, assignment.items())
                        print(n_items)
                        if not consistent(assignment,Constraints['f']):
                            count+=1
                            print("********************************************* - > Failure")
                            continue  
                            
                        for g in G:
                            assignment['g']=g
                            n_items = take(7, assignment.items())
                            print(n_items)
                            if not consistent(assignment,Constraints['g']):
                                count+=1
                                print("********************************************* - > Failure")
                                continue 
     
                                    
                                    
                            for h in H:
                                assignment['h']=h
                                n_items = take(8, assignment.items())
                                print(n_items)
                                if not consistent(assignment,Constraints['h']):
                                    count+=1
                                    print("********************************************* - > Failure")
                                    continue
                                                                            
                                print("Yay! we have a model")
                                model=np.array([a,b,c,d,e,f,g,h])
                                if not models.size:
                                    models=model
                                else:
                                    models=np.vstack((models,model))
                                                                        
                                                                
                                                            
                                                
                                            
                                            
                                            
                                            
                                            


# ## Show models found 

# In[39]:


print("The search algorthm found {0} models with {1} failures" .format(models.shape[0],count))
print(models)

