#!/usr/bin/env python
# coding: utf-8

# ## Solución lineal de prmer orden 
# 
# una ecuación diferenacial homogenea de primer orden es de la forma 
# 
# $$a(t)y'+b(t)y=c(t)$$
# si $a(t)\ne 0$ enonces podemos transformar la ecuación de la forma 
# 
# $$y'(t)+P(t)y(t)=Q(t)$$
# donde $P(t)=\frac{b(t)}{a(t)}$ y $Q(t)=\frac{c(t)}{a(t)}$.
# 
# Note que si $Q(t)=0$, la ecuación anterior se torna de la forma 
# $$y'(t)+P(t)y(t)=0$$
# 
# podemos buscar un factor de integración de la forma 
# 
# $$\rho(t)=e^{\int P(t)d\ t},$$
# note que 
# 
# $$\frac{d}{dt}\Big(y(t)e^{\int P(t)d\ t}\Big)=y'e^{\int P(t)d\ t}+y(t)P(t)e^{\int P(t)d\ t}$$
# 
# al multiplica a $\rho(t)$ por la ecuación original tenemos 
# 
# 
# $$y'(t)\rho(t)+\rho(t)P(t)y(t)=0$$
# $$y'(t)e^{\int P(t)d\ t}+e^{\int P(t)d\ t}P(t)y(t)=0$$
# $$\frac{d}{dt}\Big(y(t)e^{\int P(t)d\ t}\Big)=0$$
# $$\int\frac{d}{dt}\Big(y(t)e^{\int P(\tau)d\tau}\Big)d t=C$$
# de esta forma tenemos que 
# $$y(t)=C
# 

# In[ ]:




