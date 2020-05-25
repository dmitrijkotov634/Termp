# Termp
Drawing in the terminal

*Installation*:

`pip install --upgrade termp`

*Import*:
```python
from Termp import *
```

*Create a text picture*:
```python
t = termp(50,50)
# Create a 50 × 50 text image
```
*Draw*:
```python
t.line(0,0,49,49)
t.circle(25,25,10)
t.rect(0,0,49,49)
t.fill(30,5, "#")
t.fill(20,30, "#")
```
*Result*:
```python
t.print()
```
 
<div align="center">

![image](https://github.com/dmitrijkotov634/Termp/blob/master/result.jpg)

</div>

*Convert pictures*:
* with color
```python
t = termp(140, 140)
t.image("file.jpg", 139, color=True)
```

<div align="center">

![image](https://github.com/dmitrijkotov634/Termp/blob/master/result1.jpg)

</div>

* without color
```python
t = termp(140, 140)
t.image("file.jpg", 139)
```

<div align="center">

![image](https://github.com/dmitrijkotov634/Termp/blob/master/result2.jpg)

</div>