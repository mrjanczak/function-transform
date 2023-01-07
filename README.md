# script to plot steps of function transformation

### Step 1 - define basic function _f(x), e.g. root square x**(1/2) as:
```python
def _f(x):
    try:
        return x**0.5
    except:
        return None
```
### Step 2 - define sequence of equations to graphically determine plot of desired equation 
- Use basic function as f(x) - can be used only once per line!
- Allowable operators: +, -, *, /, ** (power), |...| (absolute value e.g. |x+2|)
```python
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
```python
xlim, ylim = 5.,3.
dx = .1
```
### Script generates plots helpful to verify sequence of function transsformation:
![Figure_1](https://user-images.githubusercontent.com/6569984/211146463-956f97af-07de-4db4-9b34-4a0f9b75eb2e.png)
