# function_transformation_plots
script to plot steps of function transformation

### Step 1 - define basic function _f(x), e.g. root square x**(1/2) as:
```
def _f(x):
    try:
        return x**0.5
    except:
        return None
```
### Step 2 - define sequence of equations to graphically determine plot of desired equation 
Use basic function as f(x) - can be used only once per line!
Allowable operators: +, -, *, /, ** (power), |...| (absolute value e.g. |x+2|)
```
Y_ = '''
f(x)
f(x+1)
f(-x+1)
f(-|x|+1)
f(-|x+2|+1)
-f(-|x+2|+1)
-f(-|x+2|+1)+1
|-f(-|x+2|+1)+1|
|-f(-|x+2|+1)+1|-1
'''
```
### Step 3 - define symmetric range of plot, e.g. for xlim = 5 x ∈ <-5,5>
```
xlim, ylim = 5.,3.
dx = .1
```
