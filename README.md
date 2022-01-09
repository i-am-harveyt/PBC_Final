# Family Tree Maker

## Introduction

This is a Python-based application that can help you draw a simple family tree,
and this app's target group is social workers (and, of course, all of you if you want to draw one).

However, the divorce relation has not implemented yet, maybe one day it will, or 
never(LOL), but I sincerely hope in will be implemented in another day.

In some reason, considering there might be kind of (weird, in my culture) relationship,
the marriage between parent and kid is accepted.

BTW, this is also the final project for the Programming for Business Computing class.

Enjoy using it!

Author: Harvey Tung

Date: 12/28 2021. (Happy New Year!)

## Functions

These functions are implemented in this application, and which can be called 
by clicking the button on the Controller window.

### Adding person

Adding a node in the graph, and the name is needed to be written, or the adding will be failed.

### Deleting person

Deleting a node in the graph, before doing this, highly recommend that remove all the edges and isolate the node.

### Adding relationship

Adding a relationship, there are now three kinds of relations:
1. Married Couple: the user manually chose two different node to be a couple, and there locations(left or right).

2. Child: the user manually chose three (or two) different nodes and assign them as Fa/Mather and child, 
and assign location as well.

3. Unmarried Couple: Same as married couple, but the line's style is dashed.

### Deleting Relationship

