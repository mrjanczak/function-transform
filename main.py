import matplotlib.pyplot as plt
import numpy as np
import re

def f(x_):
    global x, X
    # Mask elements out of domain
    mask = np.where(x_ < 0., 1, 0)
    X.append(np.ma.array(x, mask = mask))
    x_ = np.ma.array(x_, mask = mask)

    return x_**0.5

Y_ = [
    'f(x)',
    'f(x-1)-2',       
    'f(|x|-1)-2',     
    '|f(|x|-1)-2|',    
    '-|f(|x|-1)-2|',    
    '-1-|f(|x+2|-1)-2|',
]

x = np.arange(-9.999, 10., .1)
X = []
Y = []

for y_ in Y_:
    match = re.search('\|.*\|', y_) 
    while match:
        abs = match.group()
        y_ = y_.replace(abs, 'np.abs('+abs[1:-1]+')' )
        match = re.search(pattern, y_) 
    exec('Y.append('+ y_ + ')')

fig, axs = plt.subplots(len(Y)-1, 1, figsize=(5, 10), constrained_layout=True)
for i in range(len(Y)-1):
    axs[i].plot(X[i],  Y[i],   'r', label=Y_[i])
    axs[i].plot(X[i+1],Y[i+1], 'g--',   label=Y_[i+1])
    axs[i].legend()
    axs[i].grid(True)
plt.show()

