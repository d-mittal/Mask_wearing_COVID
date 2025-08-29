# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:26:32 2024

@author: dmittal
"""

import numpy as np
from numba import njit


@njit(fastmath=True)
def simulation(I,S,country_params,mu,beta):
    
    #I=np.log(I)
    a,w=country_params
    #a=0
    k=1
    #mu=0.3
    #beta=1
    x=0
    time_steps=len(I)
    x_time_series=np.zeros(time_steps, dtype=np.float64)
    for i in range(time_steps):
        
        U= -k + a*I[i]+ w*(x-0.5)
        #U= -k + a*I[i] + w*((x-0.5) + c*S[i])
        p_m= 1.0/(1.0 + np.exp(-U * beta))
        
        delta_x= mu*(p_m-x)
        x=x+delta_x
        x_time_series[i]=x
     
    return x_time_series
        
    
                                                                           
    
                                                                                                                        