<div align="center">
	<h1>Termp</h1>

Drawing in the terminal

![pypi](https://badge.fury.io/py/termp.svg)

</div>

## Install
`pip install --upgrade termp`

## Usage
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

![image](https://github.com/dmitrijkotov634/Termp/blob/master/images/result.jpg)

</div>

## Convert Pictures
* with color
```python
t = termp(140, 140)
t.image("file.jpg", 140, color=True)
```

<div align="center">

![image](https://github.com/dmitrijkotov634/Termp/blob/master/images/result1.jpg)

</div>

* without color
```python
t = termp(140, 140)
t.image("file.jpg", 140)
```

<div align="center">

![image](https://github.com/dmitrijkotov634/Termp/blob/master/images/result2.jpg)

</div>

* color filter picture
```python
t = termp(140, 140)
t.image("file.jpg", 140)
t.givecolor("green")
```

<div align="center">

![image](https://github.com/dmitrijkotov634/Termp/blob/master/images/result3.jpg)

</div>