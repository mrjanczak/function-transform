import matplotlib.pyplot as plt
import numpy as np
import re
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning) 

# Step 1 - define basic function, e.g. root square x**(1/2)
def _f(x):
    try:
        return x**0.5
    except:
        return None

# Step 2 - define sequence of equations to graphically determine plot of desired equation 
# Use basic function as f(x) - can be used only once per line!
# Allowable operators: +, -, *, /, ** (power), |...| (absolute value e.g. |x+2|)
Y_ = '''f(x)
f(x+1)
f(-x+1)
f(-|x|+1)
f(-|x+2|+1)
-f(-|x+2|+1)
-f(-|x+2|+1)+1
|-f(-|x+2|+1)+1|
|-f(-|x+2|+1)+1|-1
'''

# Step 3 - define symmetric range of plot, e.g. for xlim = 5 x ∈ <-5,5>
xlim, ylim = 5.,5.
dx = .1

############################## Don't modify below this line ########################

# Call basic function _f(x) for each x from <-xlim,+xlim> range 
# and exclude arguments x out of domain (mask = 1) from X
def f(x_):
    global x, X
    m_ = []
    y_ = []

    for _x in x_:

        _y = _f(_x)
        if _y:
            _m = 0
        else:
            _m = 1

        y_.append(_y)
        m_.append(_m)

    x_ = np.ma.array(x, mask = m_)
    X.append(x_)

    y_ = np.array(y_)
    return y_

_xlim = [-xlim, xlim]
_ylim = [-ylim, ylim]
x = np.arange(_xlim[0],_xlim[1], dx)

X = [] # List of x values for all transformation steps
Y = [] # List of y values for all transformation steps

Y_ = Y_.splitlines()

# Calculate each step of transformation
for y_ in Y_:

    if len(y_) == 0:
        continue

    print('line: ' + y_)

    # Check equation
    if (y_.count('(') + y_.count(')')) % 2 > 0:
        print('ERROR - line ' + y_ + ' has not balanced brackets' )
        break

    if y_.count('|') % 2 != 0:
        print('ERROR - line ' + y_ + ' has not balanced modulus')
        break
    
    match = re.search('[^0-9\.\(\)\|\+\-\*\/fx]*\n', y_)
    if match:
        print('ERROR - line ' + y_ + ' includes not allowed chars' + match.group())
        break

    if y_.count('f') > 1:
        print('ERROR - line ' + y_ + ' includes more then 1 call of f(x)')
        break

    # Replace |...| by np.abs(...)
    match = re.search('\|.*\|', y_) 
    while match:
        abs = match.group()
        y_ = y_.replace(abs, 'np.abs('+abs[1:-1]+')' )
        match = re.search('\|.*\|', y_) 

    # Find solutions of current equation and append to Y
    try:
        exec('Y.append('+ y_ + ')')
    except:
        print('ERROR - line ' + y_ + 'cannot be executed')
        break

# Plot transformation steps in pairs
Ylen = len(Y)
if Ylen < 2:
    print('Provide more equations')

elif Ylen == 2:
    fig, axs = plt.subplots(len(Y)-1, 1, figsize=(5, 10), layout="constrained")
    for i in range(len(Y)-1):
        axs.plot(X[i],  Y[i],   'r', label=Y_[i])
        axs.plot(X[i+1],Y[i+1], 'g--',   label=Y_[i+1])
        axs.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        axs.grid(True)
        axs.set_xlim(_xlim[0],_xlim[1])
        axs.set_ylim(_ylim[0],_ylim[1])
    plt.show()

elif Ylen > 2:
    fig, axs = plt.subplots(len(Y)-1, 1, figsize=(5, 10), layout="constrained")
    for i in range(len(Y)-1):
        axs[i].plot(X[i],  Y[i],   'r', label=Y_[i])
        axs[i].plot(X[i+1],Y[i+1], 'g--',   label=Y_[i+1])
        axs[i].legend(loc='center left', bbox_to_anchor=(1, 0.5))
        axs[i].grid(True)
        axs[i].set_xlim(_xlim[0],_xlim[1])
        axs[i].set_ylim(_ylim[0],_ylim[1])
    plt.show()


