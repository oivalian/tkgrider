# **tkgrider**
A library that simplifies tkinter grids by feeding in lists into simple functions

___

### Dependancies

tkgrider is dependent on python's built-in ```tkinter``` library
 
___

### Documentation

Get started by importing the module:

```
from tkgrider import *
```

Place your widgets into a list. This will be used to feed into our methods

```
# widgets
item1 = tk.Label(root, text="Example 1")
item2 = tk.Label(root, text="Example 2")
item3 = tk.Label(root, text="Example 3")
item4 = tk.Label(root, text="Example 4")
item5 = tk.Label(root, text="Example 5")
item6 = tk.Label(root, text="Example 6")

# add widgets to a list
wigdets = [item1, item2, item3, item4, item5, item6]
```

**-- Packing Functions --**

Place widgets into a list and feed as an attribute.

To utilise, call the 'Pack' class before the method (where method is replaced by methods below)
```
Pack.method()
```

**Pack by column width**

Packing by column width will populate the grid from left to right by max column amount.

e.g. if input is _3_, the maximum grid width will be 3. Rows are then automatically added per amount of widgets.

```
Pack.packcol(widgets, 3)
```
Output:

![img_2.png](img_2.png)

**Pack by row height**

Packing by row width will populate the grid from top to bottom, left to right by max row amount.

e.g. if input is _3_, the maximum grid height will be 3. columns are then automatically added per amount of widgets.

```
Pack.packrow(widgets, 3)
```
Output:

![img_3.png](img_3.png)

**Pack by row height and col width**

You can also define both height and width and populate the grid from left to right by both maxes.

e.g. if row input is _2_, and width input is _4_ the maximum grid height will be 2 and the max width will be 4.

```
Pack.pack(widgets, 2, 4)
```
Output:

![img_4.png](img_4.png)

**Keyword args**

There are five optional keyword arguments available for each method:

```x=``` adds outer x-axis padding to grid

```y=``` adds outer y-axis padding to grid

```ix``` adds inner x-axis padding to grid

```iy``` adds inner y-axis padding to grid

```s=``` defines 'sticky' values for all cells

example:
```Pack.pack(widgets, 3, 3, x=20, y=20, s='nw')```

Output:

![img_5.png](img_5.png)

> More features will be added soon. I plan to add more grid customisation such as styling, colspan, rowspan options
> access and change particular widgets etc.