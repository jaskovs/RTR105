user@epk428-4:~$ idle &
[1] 2715
user@epk428-4:~$ ipython
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: fruit = 'banana'

In [2]: pint(len(fruit))
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-2-e8065a0b2bb0> in <module>()
----> 1 pint(len(fruit))

NameError: name 'pint' is not defined

In [3]: print(len(fruit))
6

In [4]: while
   ...: index
   ...: < 
   ...: len
   ...: (
   ...: fruit
   ...: ): 
   ...: letter
   ...: = 
   ...: fruit
   ...: [
   ...: index
   ...: ]
   ...: print
   ...: (
   ...: index
   ...: , 
   ...: letter
   ...: )
   ...: index
   ...: = 
   ...: index
   ...: +
   ...: 1
  File "<ipython-input-4-ed48b9f1e73b>", line 3
    =
    ^
SyntaxError: invalid syntax


In [5]: fruit = 'banana'

In [6]: for letter in fruit:
   ...:     print(letter)
   ...:             
b
a
n
a
n
a

In [7]: 

In [7]: word = 'banana'

In [8]: count = 0

In [9]: for letter in word:
   ...:     if letter == 'ā':
   ...:         count = count + 1
   ...: print(count)
   ...: 
0

In [10]: for letter in 'banana:
  File "<ipython-input-10-4cfbb7935d47>", line 1
    for letter in 'banana:
                          ^
SyntaxError: EOL while scanning string literal


In [11]: for letter in 'banana':
    ...:     print(letter)
    ...:     
b
a
n
a
n
a

In [12]: history > history_20181105.py

