# Termp
Drawing in the terminal

*Installation*:  
`pip install --upgrade termp`

*Import*:
```python
from Termp import termp
```

Create Create a text picture:
```python
t = termp(50,50)
# Create a 50 × 50 text image
```
Draw
```python
t.line(0,0,49,49)
t.circle(25,25,10)
t.rect(0,0,5,5)
```
Print
```python
t.print()
```
*Result*:


