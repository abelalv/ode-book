#!/usr/bin/env python
# coding: utf-8

# # Unidad 1
# 
# Cuando tenemos una ecuación como $x+2=3$ buscamos un valor de $x$ tal que satisfaga la ecuación en algún sentido, en el caso de ecuación diferencial ordinaria (EDO), ya no buscamos un número sino una función en una ecuación, la cual esta relacionada con sus derivadas. por ejemplo
# $$\label{eq1}
# \frac{dy}{dx}=5y(x),
# $$
# aquí estamos buscando una función $y(x)$ cuya derivada sea $5y(x)$. Nosotros podemos probar por simple inspección que esta  función seria
# 
# $$y(x)=Ce^{5x},$$
# donde $c$ es una constante. Notemos que de esta forma no tenemos una sola función sino una familia de funciones. Lo que nos hace preguntarnos ¿Cómo debemos modificar la ecuación \eqref{eq1} para obtengamos una única solución? Para solucionar esta pregunta tenemos que agregar un termino llamado condición inicial el cual determina el valor de la función en un punto especifico, de esta forma la \eqref{eq1}$ se puede reescribir de la forma 
# 
# 
# $$\label{eq2}
# \frac{dy}{dx}=5y(x), \ \ \ y(0)=1. 
# $$

# ## Definiciones 
# + Llamaremos ecuación diferencial ordinaria (abreviado EDO) a una ecuación que involucra a una variable independiente $x$, una función $y(x)$ y una o varias derivadas de $y(x)$
#  
#  Ejemplos 
#  
#  $$
#  xy'(x)=y+5x-y^2,\ \ \ \ \  \ \ 3\frac{d^2y}{dx^2}=yx,\ \ \ \ \  \ \ \dot{y}=5xy+5y
#  $$
#  
# + Llamaremos orden de una EDO al orden de la mayor derivada en la ecuación.
# + Llamaremos una ecuación diferencial lineal de orden $n$ se la podemos escribir de la siguiente forma 
# 
# $$a_n(x)\frac{d^ny}{dx^n}+a_{n-1}(x)\frac{d^{n-1}y}{dx^{n-1}}+\cdots+a_1(x)\frac{dy}{dx}+a_0(x)y=b(x).$$
# + Dada una EDO de orden $n$, llamaremos solución de esta EDO a una función $y = f (x)$ definida en un intervalo $I$ y que tiene al menos $n$ derivadas continuas en el intervalo $I$, de forma que cuando sustituimos $y = f (x)$ y sus derivadas en la EDO se cumple la ecuación en todo el intervalo
# 
# + Dada una EDO de orden $n$, un intervalo $I$ y un punto $x_0\in I$, llamaremos problema de valores iniciales (abreviado PVI) al problema de encontrar las funciones que cumplen la EDO de orden $n$ anterior en el intervalo $I$. Además satisfacen las condiciones iniciales $$y(x_0) = c_0, y'(x_0) = c_1, . . . , y^{(n-1)}(x_0) = c_{n-1},$$ donde los $c_i$ son $n$ números prefijados 

# ### Ejercicios 
#  
#  
#  1. En los siguientes problemas establezca el orden de la ecuación diferencial dada. Determine si la ecuación es lineal 
#  * $(1-x)y''=\cos x+y'''-y'\sin x$
#  * $\frac{d^3y}{dx^3}+\cos y=x^2$
#  * $x^6y^{(4)}+x^3y^{(3)}+\ln (x)y^{(1)}-y=\cos(x)$
#  * $\frac{d^2x}{dt^2}+\frac{dx}{dt}+x =\ln (x+t)$
#  

# ## Cuando una función es solución de una ecuación diferencial
# 
# Para comprobar si una ecuación diferencial tiene una cierta solución lo único que debemos hacer es sustituir la función en la ecuación para comprobar si es la solución como mostraremos en el siguiente ejemplo
# 
# 
# Comprobemos que la función  $y(x)=4e^{-3x}+2$  es solución de la ecuación $2y''(x)+3y'(x)-9y(x)=-18$
# 
# para ello lo primero que hacemos es calcular las derivadas, 
# 
# $\begin{split}
# y'(x)&=-12e^{-3x},\\
# y''(x)&=36e^{-3x},
# \end{split}$
# 
# posteriormente sustituimos en la ecuación y comprobamos que la igualdad se satisfaga
# 
# 
# $\begin{split}
# 2y''(x)+3y'(x)-9y(x)&=-18,\\
# 2(36e^{-3x})+3(-12e^{-3x})-9(4e^{-3x}+2)&=-18,\\
# (72-36-36)e^{-3x}-18&=-18,\\
# -18&=-18.
# \end{split}$

# ### Ejercicios 
# 
# Compruebe que las familias de las funciones son soluciones de las  ecuaciones 
# * $\frac{dP}{dt}=P(t)(1-P(t))$ con la familia $P=\frac{c_1e^t}{1+c_1e^t}$
# * $\frac{dy}{dx}+2xy=1$ con la familia $y=e^{-x^2}\int_0^xe^{t^2}dt+c_1e^{-x^2}$
# * $\frac{d^2y}{dx^2}-4\frac{dy}{dx}+4y=0$ con la familia $y=c_1e^{2x}+c_2xe^{2x}$
# * $xy'-2y=0$ con la familia $\begin{cases}-x^2,&\ \  x<0\\x^2,&\ \  x\geq0\end{cases}$, en $(-\infty,\infty)$.

# 
# ## Primer método para encontrar las soluciones de una EDO de primer orden 
# ### Ecuaciones Variables separables 
# La EDO de variable separable tiene la forma 
# 
# $$
# \label{equasol}
# N(y)y'+M(x)=0.
# $$
# 
# Para resolver \eqref{equasol} el siguiente procedimiento
# 
# 1. Separa las variables para escribir la EDO de la forma $N(y)y'+M(x)=0$, e identificar los coeficientes $N(y)$ y $M(x)$ 
# 2. Determine la antiderivada $G(y)$ para $N(y)$ y otra  $F(x)$ para $N(x)$.
# 3. Todas las soluciones $y=y(x)$ satisfacen la ecuación $G(y)+F(x)=C$, donde $C$ es una constante 
# 
# ### Integrales y curvas integrales 
# 
# Definiremos algunos términos nuevos
# 
# *Integrales y curvas integrales* Una función no constante $H(x,y)$ en un rectángulo Res una integral de la EDO $Ny'+M=0$ si para cualquier solución $y(x)$ cuya gráfica este dentro de R, $H(x,y(x))=C$ para alguna constante $C$. El conjunto de puntos en R que satisfacen $H(x,y)=C$ es una curva integral de la EDO. Si C es una constante no especificada, entonces $H(x,y)=C$ es la solución general implicita de la EDO
# 
# ### Considere el ejemplo 
# 
#  $$\begin{split}
# yy'-x&=0,\\
# y\frac{dy}{dx}&=x,\\
# ydy&=xdx,\\
# \int ydy&=\int xdx,\\
# \frac{y^2}{2}&=\frac{x^2}{2}+c,\\
# y^2-x^2&=c.
# \end{split}
# $$
# 
# La ecuación $y^2-x^2=c$ es considerada una solución general o familia de soluciones, para determinar una solución que pase por la condición inicial $y(0)=1$, sustituimos en la ecuación 
# 
#  $$\begin{split}
# y^2(x)-x^2&=c,\\
# y^2(0)-0^2&=c,\\
# 1^2-0&=c\\
# 1&=c
# \end{split}
# $$
# 
# de esta forma obtenemos que la solución del problema inicial es 
# 
# $$y^2-x^2=1$$
# 

# ### Ejercicios
# Encuentre 
# 1. La curva integral de $yy'+x=0$ pasando por el punto $(2,-1) $
# 2. $(1-y^2)y'+x^2=0$ Encuentre la solución general 
# 3. $(1-y^2)y'+x^2=0$, encuentre la curva integral que pasando por el punto $(-1,1/2)$

# ## Ecuación Lógistica  (Verhulst)
# 
# La solución de la ecuación logística es conocida como la [función](https://es.wikipedia.org/wiki/Funci%C3%B3n_log%C3%ADstica), la cual se usa para modelar diferentes fenómenos como propagación de enfermedades, crecimiento poblacional difusión en redes sociales, entre otros. 
# 
# Supongamos que tenemos una población de peces en un estanque, y queremos modelar la población en un determinado tiempo. Para ello vamos a crear un modelo basado en ecuaciones diferenciales ordinarias, usando el siguiente principio 
# 
# La  tasa de cambio neta de  la población de peces en toneladas $y'(t)$ es equivalente a la tasa de nacimiento menos la tasa de muerte.
# 
# <font color='blue'>    
# ¿Podemos escribir esto como una ecuación diferencial?
# ¿Qué supuestos debemos incluir?
# </font>    
# 
# Notemos que debemos incluir nuevos supuestos, por ejemplo,
# * El modelo es continuo.
# * La tasa de nacimiento de la población es proporcional a la población existente.
# * Existe una "penalización" por el hecho de sobrepoblación.
# * la tasa de reproducción es proporcional a la cantidad de recursos disponibles.
# 
# $$\frac{dy}{dt}=ry\Big(1-\frac{y}{k}\Big),$$
# 
# La familia de soluciones de este modelo es
# 
# $$y(t)=\frac{ky_0e^{rt}}{k+y_0e^{rt}},$$
# donde $y_0$ es la condición inicial del problema.
#     

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np


# Ecuacion Diferencial: dy/dx=f(x,y)
        


def f( y,x): 
    #return 2*y/x
    r=2.0
    K=3.0
    return r*y*(1-y/K)
    



# Campo de pendientes
def campo(N,xf,yf):
    
    #N  numero de pendientes a graficar
    #K=3.0
    xi = -1.3
    #xf = 5  # dominio
    yi= -0.1
    #yf= K+0.5*K
    x = np.linspace(xi, xf, N)
    y = np.linspace(yi, yf, N)
    X, Y = np.meshgrid(x, y)
    U = 1
    V = f(Y,X)
    U2, V2 = U/np.sqrt(U**2+V**2), V/np.sqrt(U**2+V**2)
    plt.quiver(X, Y, U2, V2, color='k')
    plt.grid(True)
    return 
xf=5
yf=4.5
campo(30,xf,yf)

plt.title(r'Campo de pendientes: $\frac{dy}{dx}=ry(1-\frac{y}{K})$')
#plt.title(r'Campo de pendientes: $\frac{dy}{dx}=2\frac{y}{x}$')
#plt.title(r'Campo de pendientes: $\frac{dy}{dx}= -y+sin(4*x) $ ')


# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
# initial condition
y0 = [ 0.0, 0.1, 0.3, 0.4, 0.5, 4, 3.6]

# time points
xf=5.0
yf=4.5
t = np.linspace(0, xf)

# solve ODE
for yi in y0:
    y = odeint(f, yi, t, rtol=1.0E-8)
    plt.plot(t, y)

# plot results
campo(30,xf,yf)
plt.xlabel('time')
plt.ylabel(r'y(t)')
plt.title(r'Campo de pendientesny solución de la ecuación: $\frac{dy}{dx}=ry(1-\frac{y}{K})$')
plt.show()


#  <font color='blue'>
# En este momento nos podemos realizar muchas preguntas
#     
#   - ¿Cómo es el comportamiento de la solución para tiempos largos?
#   - En este caso, ¿por que "casi" con cualquier condición inicial tenemos el mismo comportamiento para tiempos grandes?
#   - ¿Exíste alguna relación entre el comportamiento y la función $f(y)=ry\Big(1-\frac{y}{k}\Big)$
#     
#  </font>

# ### Problema, un modelo de ahorro
# Suponga que depositamos $\$ 5000 $ en una cuenta de ahorros con intereses devengados a una tasa de capitalización continua del $ 2\% $. Si dejamos que $A (t)$ denote la cantidad de dinero en la cuenta en el tiempo t, entonces la ecuación diferencial para $A$ es
# 
# $\frac{dA}{dt}=0.02A$
# 
# * ¿Encuentre la solución analítica 
# * Suponiendo que el interés nunca cambia, cual sería el dinero que tendría después de 10 años
# 
# Si vemos que al cabo de 10 años, tenemos una buena cantidad de dinero, por ende decidimos retirar cada año la cantidad de $ \$ 500$, la ecuación diferencial cambia de la siguiente forma, cuando $t>10$$ 
# 
# $\frac{dA}{dt}=0.02A-500$
# 
# De esta forma podemos expresar la ecuación para todo tiempo
# 
# $ \frac{dA}{dt}=\begin{cases}0.02A & \text{si } t<10,\\
# 0.02A-500& \text{si } t>10.\end{cases} $
# 
# 
#  * ¿Al cabo de 12 años cuanto dinero tendremos?
#  * ¿Al cabo de cuanto tiempo me voy a quedar sin dinero años cuanto dinero tendremos?
#  * Suponiendo que podría vivir con 500 al año, ¿Cual debería ser el  monto inicial para poder vivir de por vida? 

# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')
def f( y,x):
    dy=w=np.where(x < 10, 0.02*y, 0.02*y-500)
    return dy
# plot results
xf=20
yf=30000
campo(30,xf,yf)

# initial condition
y0 = [ 5000, 6000, 4000,20000,20800]

# time points
xf=20
yf=4.5
t = np.linspace(0, xf)

# solve ODE
for yi in y0:
    y = odeint(f, yi, t, rtol=1.0E-8)
    plt.plot(t, y)


#  <font color='red'>    
#  Por grupos exponer los siguientes fenómenos:
#     
#  -  Modelos aplicados a la ecuaciones diferenciales 
#  -  Dinámica poblacional 
#  -  Decaimiento radioactivo
#  -  Ley de enfriamiento de Newton 
#  -  Reacciones químicas 
#  -  Mezclas 
#  -  Cuerpos de caídas y resistencia del aire
#     
# </font> 

# In[48]:





# In[ ]:




