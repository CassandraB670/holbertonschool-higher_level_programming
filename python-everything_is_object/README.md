Task 0 - Who am I ?
    file 0-answer.txt

What function would you use to print the type of an object?

Write the name of the function in the file, without ().

Task 1 - Where are you ?
    file 1-answer.txt

How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

Task 2 - Right count
    file 2-answer.txt

In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 100

Task 3 - Right count =
    file 3-answer.txt

In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 89

Task 4 - Right count =
    file 4-answer.txt

In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a

Task 5 - Right count =+
    file 5-answer.txt

In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a + 1

Task 6 - Is equal
    file 6-answer.txt

What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)

Task 7 - Is the same
    file 7-answer.txt

What do these 3 lines print?

>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

Task 8 - Is really equal
    file 8-answer.txt

What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)

Task 9 - Is really the same
    file 9-answer.txt

What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)

Task 10 - And with a list, is it equal 
    file 10-answer.txt

What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)

Task 11 - And with a list, is it the same
    file 11-answer.txt

What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)

Task 12 - And with a list, is it really equal
    file 12-answer.txt

What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)

Task 13 - And with a list, is it really the same
    file 13-answer.txt

What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)

Task 14 - List append
    file 14-answer.txt

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

Task 15 - List add
    file 15-answer.txt

What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

Task 16 - Integer incrementation
    file 16-answer.txt

What does this script print?

def increment(n):
    n += 1

a = 1
increment(a)
print(a)

Task 17 - List incrementation
    file 17-answer.txt

What does this script print?

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

Task 18 - List assignation
    file 18-answer.txt

What does this script print?

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

Task 19 - Copy a list object
    file 19-copy_list.py

Write a function def copy_list(a_list): that returns a copy of a list.

    The input list can contain any type of objects
    Your file should be maximum 3-line long (no documentation needed)
    You are not allowed to import any module

Task 20 - Tuple or not ?
    file 20-answer.txt

a = ()
Is a a tuple? Answer with Yes or No.

Task 21 - Tuple or not ?
    file 21-answer.txt

a = (1, 2)
Is a a tuple? Answer with Yes or No.

Task 22 - Tuple or not ?
    file 22-answer.txt

a = (1)
Is a a tuple? Answer with Yes or No.

Task 23 - Tuple or not ?
    file 23-answer.txt

a = (1, )
Is a a tuple? Answer with Yes or No.

Task 24 - Who I am ?
    file 24-answer.txt

What does this script print?

a = (1)
b = (1)
a is b

Task 25 - Tuple or not
    file 25-answer.txt

What does this script print?

a = (1, 2)
b = (1, 2)
a is b

Task 26 - Empty is not empty 
    file 26-answer.txt

What does this script print?

a = ()
b = ()
a is b

Task 27 - Still the same ?
    file 27-answer.txt

>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.

Task 28 - Same or not ?
    file 28-answer.txt

>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.

Task 29 - Python3: Mutable, Immutable... everything is object!

Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):

    introduction
    id and type
    mutable objects
    immutable objects
    why does it matter and how differently does Python treat mutable and immutable objects
    how arguments are passed to functions and what does that imply for mutable and immutable objects
    If you worked on advanced tasks, please also include what you did learn in those tasks in the blog post.

Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.

When done, please add all urls below (blog post, LinkedIn post, etc.)

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.