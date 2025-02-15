# Sets

We will start by reviewing some high-school math:

* Read [this](https://discrete.openmathbooks.org/dmoi3/sec_intro-sets.html) chapter about sets.
* Solve the exercises in the chapter.

## Sets in Python

Python has a built-in `set` data type, but the problem is that it is not
recursive. _Think about what this means and why it is a problem._ We will not
use the built-in `set` data type in this assingment, but if you nevertheless
want to have a look, check
[the docs](https://docs.python.org/3/library/stdtypes.html#set) or
[this Real Python article](https://realpython.com/python-sets/).

In this assingment we will represent sets with the help of Python dictionaries. Our implementation will not be recursive either.
So refresh your memory by 
[the docs](https://docs.python.org/3/library/stdtypes.html#dict), or Think
Python, Chapter 11. 

The idea is simple, we will use the keys of the dictionary to represent the
items in the set. The values of the dictionary will be `None`. _Think about why
this is a good idea._

## The task

Your task is to implment the following constructors:

* `set_from_list` -- takes a list and returns a set.
* `list_from_set` -- do the reverse of above. 
* `add` -- takes a set and an element and returns a new set with the element added.
* `remove` -- takes a set and an element and returns a new set with the element removed.

and the following set operations as two place functions taking two sets (=a
special kind of dict in our case) and returning a set:

* `union`
* `intersection`
* `difference`
* `symmetric_difference` -- the elements that are in exactly one of the sets.
* `is_subset_of`
* `is_superset_of`


You are required to implement these functions In the functional style as `lambda` functions. 

If you feel lost at this task check the following:

* Dictionary comprehensions --  see Python Cookbook 1.17 for an example. 
* The merge operator `|`-- see the relevant section in [this article](https://www.digitalocean.com/community/tutorials/python-add-to-dictionary#adding-to-a-dictionary-using-the-merge-operator) 

Code your definitions in the file `editme.py` in the repo and commit your
changes to the repo. You can work in increments, but make sure that you commit
when you have something that works.

Included in `eidtme.py` is a test suite that you can use to test your functions.
You can run your tests any time during your work by running `test()`, it will
simply report `[Error]` for those functions you have not implemented yet and for
those who actually raise an error.
