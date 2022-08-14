.. include:: <isonum.txt>

.. _ch_dict:

Dictionaries
============

.. _sec_crud_dict:

Creating and using dictionaries
-------------------------------

We can do a lot of things in code using what we know so far.  Some of the things
we can do in code is kind of, well, "clunky."  Consider the following example.
Suppose we want to keep track of a group of students and their major field of
study.  The only way we know how to do that currently is with lists.

.. code-block:: python

   names = ["Shayla Succotash", "Amy Avocado", "Larry Linguini", "Kevin Kumquat"]
   majors = ["Comp Sci", "Accounting", "Math", "Comp Sci"]

We are using lists to store corresponding attributes of each student.  Each
student has a unique index for their attributes.  Suppose we ran the code that
follows.

.. code-block:: python

   print(names[1])
   print(majors[1])
   print()
   print(names[3])
   print(majors[3])

The resulting output of this code is:

.. code-block:: none

   Amy Avocado
   Accounting
   
   Kevin Kumquat
   Comp Sci

This is all fine, but it's also a bit awkward.  If we want to know a student's
major, we have to find their location in the first list, and then use their
index to look up their major in the second list, like this:

.. code-block:: python

   x = "Kevin Kumquat"
   found = False
   
   for i in range(0, len(names)):
       if names[i] == x:
           print(majors[i])
   
   if not found:
       print("Couldn't find a major for %s." % x)

Yuck.  What we really want to do is something more simple, like this:

.. code-block:: python

   x = "Kevin Kumquat"
   m = get_major(x)
   # m is now "Comp Sci"

We could easily define a function like ``get_major``, but fortunately we don't
have to.

To make this easier, we will forgo lists (for now) and use something called
a *dictionary*.  At first glance, a dictionary is just like an English
dictionary.  With an English dictionary, we look up a word (which is a
string) and next to the word is its definition (also a string).  Python
dictionaries can be used on more than just strings, but we'll focus on
strings for now.  We can apply this concept of an English dictionary to,
say, look up ``"Amy Avocado"`` and receive ``Accounting``.

Let's create a dictionary to *associate* names with majors.  Here is how we do
it (see Listing :numref:`%s <majors_dict_def>`).

.. _majors_dict_def:
.. code-block:: python
   :caption: Defining a dictionary (``dict``)

   majors = {    
       "Shayla Succotash" : "Comp Sci",
       "Amy Avocado" : "Accounting",
       "Larry Linguini" : "Math",
       "Kevin Kumquat" : "Comp Sci",
   }

Now, we can *look up* majors by typing this:

.. code-block:: python

   print(majors["Shayla Succotash"])
   print(majors["Larry Linguini"])

This produces:

.. code-block:: none

   Comp Sci
   Math

Notice how we *create* (i.e., *define*) a dictionary.  We use curly braces
to denote the dictionary type (which is called ``dict`` kind of like other
types such as ``str`` and ``int``).  We use colons (``:``) to separate the
name from the major.  Also, notice how we use dictionaries to *look up*
values.  We use square brackets, which looks a lot like how we used lists.

Terminology time!  The values on the left side of the ``:`` in our dictionary
definition (e.g., ``"Shayla Succotash"``, etc.) are called *keys*.  The values on
the right (e.g., ``"Comp Sci"``, etc.) are simply called *values*.  Each entry in
the dictionary that associates a name with a major is called a *key-value pair*.
``"Larry Linguini"`` and  ``"Math"`` is an example of a key-value pair.

Okay, so now what?  Well, in this book we often ask questions that start with
"What happens if..." or "What happens when...?" to enhance our understanding of
a topic.  Here's one: What happens if we try to look up something that doesn't
exist in the dictionary?  Can we create an example of this in code?  You try it
without looking at the next paragraph.

Were you able to come up with an example?  If so, did it look like
Listing :numref:`%s <dict_no_key>`?

.. _dict_no_key:
.. code-block:: python
   :caption: Attempting to access a key that does not exist

   print(majors["Brooklyn Broccolini"])

Clearly, there is no key for `"Brooklyn Broccolini"` defined in `majors` in
Listing :numref:`%s <majors_dict_def>`.  What happens when we run the
Listing :numref:`%s <dict_no_key>` code?

Did you try it?  What did you find out?

If we try to specify a key that does not exist in the dictionary, the code
produces a ``KeyError``.  We could handle ``KeyError`` if we so chose, like the code
example found in Listing :numref:`%s <dict_no_key_except>`.

.. _dict_no_key_except:
.. code-block:: python
   :caption: Handling ``KeyError``

   try:
       student = "Brooklyn Broccolini"
       print(majors[student])
   except KeyError:
       print("There is no major listed for %s." % student)

If we didn't want to rely on handling a ``KeyError``, we could check first to see
if a certain key exists in a dictionary (see
Listing :numref:`%s <dict_no_key_check>`).

.. _dict_no_key_check:
.. code-block:: python
   :linenos:
   :caption: Checking for the existence of a key first

   if "Brooklyn Broccolini" in majors:
       print(majors["Brooklyn Broccolini"])
   else:
       print("No major listed for that student.")

Even though line 2 could technically raise a ``KeyError``, the ``if`` statement in
line 1 checks first to make sure line 2 won't raise a ``KeyError``.

To see a different example, let's return to the idea of a Python dictionary as
being similar to an English dictionary.  In an English dictionary, we can look
up a word and find its definition.  The word is a key.  The definition is the
word's value.

We will now write a program that creates a very small English dictionary that
allows the user to look up definitions of words (see
Listing :numref:`%s <eng_dict_str>`).

.. _eng_dict_str:
.. code-block:: python
   :linenos:
   :caption: Using a ``dict`` to create an English dictionary

   d = {
       "alpaca" : "A domesticated camelid",
       "bow" : "A weapon that shoots arrows",
       "rose" : "A prickly bush that produces fragrant flowers",
   }
   
   word = input("Enter a word to lookup (enter nothing to quit): ")
   while word != "":
       if word in d:
           print("Definition:", d[word])
       else:
           print("There is no definition for '%s'" % word)
   
       word = input("Enter a word to lookup (enter nothing to quit): ")

This is lovely, but English dictionaries often have more than one definition for
a word.  In Listing :numref:`%s <eng_dict_str>`, the key ``"rose"`` is a homophone.
The word "rose" could also mean "the past tense of rise."

It appears that we want a key to have multiple values, potentially.  If we
wanted to store multiple values in the past, we have relied on using a ``list``.
So, we shall use a ``list`` once again.  Let us modify the definition of ``d`` in
Listing :numref:`%s <eng_dict_str>` so that the values are no longer strings, but
rather lists of strings (that is, a ``list`` of ``str``).

.. code-block:: python

   d = {
       "alpaca" : ["A domesticated camelid"],
       "bow" : ["A weapon that shoots arrows",
                "To bend at the waist",
                ],
       "rose" : ["A prickly bush that produces fragrant flowers",
                 "The past tense of rise",
                 ],
   }

The expression ``d["rose"]`` now yields a ``list`` of two items: ``"A prickly bush ..."``
and ``"The past ..."``.  Because the expression ``d["rose"]`` produces a ``list``, I
can do ``list``-things to it.  For example, the expression ``len(d["rose"])``
produces the ``int`` value ``2``, and the expression ``d["rose"][1]`` produces the
``str`` value ``"The past tense of rise"``.

When we look up a word the user enters, we can use a ``for`` loop to show each of
the definitions.  See how we have modified Listing :numref:`%s <eng_dict_str>` to
create Listing :numref:`%s <eng_dict_list>`.

.. _eng_dict_list:
.. code-block:: python
   :linenos:
   :caption: Using a ``dict`` to print word meanings

   d = {
       "alpaca" : ["A domesticated camelid"],
       "bow" : ["A weapon that shoots arrows",
                "To bend at the waist",
                ],
       "rose" : ["A prickly bush that produces fragrant flowers",
                 "The past tense of rise",
                 ],
   }
   
   word = input("Enter a word to lookup (enter nothing to quit): ")
   while word != "":
       if word in d:
           for defn in d[word]:
               print("Definition:", defn)
       else:
           print("There is no definition for '%s'" % word)
   
       word = input("Enter a word to lookup (enter nothing to quit): ")
   
There's an interesting tidbit in Listing :numref:`%s <eng_dict_list>` you may have
missed.  Note lines 14 and 15.  My initial choice for a variable name was ``def``.
However, ``def`` is a reserved keyword in Python, which we know is used to define
functions.  So, I had to chose another variable name.  Instead, I chose ``defn``
to stand for "definition."

What if we want to remove a key-value pair from a dictionary?  We can use the
``del`` keyword to accomplish this.  Consider Listing :numref:`%s <del_dict_pair>`,
specifically line 13.

.. _del_dict_pair:
.. code-block:: python
   :linenos:
   :emphasize-lines: 13
   :caption: Deleting a key-value pair from a ``dict``

   d = {
       "alpaca" : ["A domesticated camelid"],
       "bow" : ["A weapon that shoots arrows",
                "To bend at the waist",
                ],
       "rose" : ["A prickly bush that produces fragrant flowers",
                 "The past tense of rise",
                 ],
   }

   word = input("Enter a word to remove from the dictionary: ")
   if word in d:
       del d[word]
   else:
       print("Sorry, %s doesn't seem to be defined in our dictionary." % word)

If the user were to type ``alpaca``, the pair for the key ``"alpaca"`` would be
removed.  Only the pairs for the keys ``"bow"`` and ``"rose"`` would remain.
(Readers will note that removing alpacas from the dictionary would be a terrible
calamity because they are adorable and charming.  Llamas, on the other hand, are
jerks.)

.. _sec_iter_dict:

Iterating through dictionaries
------------------------------

There may be instances where we wish to iterate through a ``dict`` similar to how
we might traverse a ``list``.  Suppose have the following dictionary definition.

.. code-block:: python

   calories = {
       "egg" : 80.0,
       "milk" : 80.0,
       "cheerios" : 100.0,
       "blueberry" : 0.78,
       "strawberry" : 4.0,
   }

``calories`` is a ``dict`` that acts as a food database.  It allows programmers to
look up the calories for a given food.  Thus, ``calories["strawberry"]`` gives us
``4.0``.  Suppose we want to see all the foods in our database.  We might write
the following code.

.. code-block:: python

   for food in calories:
       print(food)

When a ``for`` loop operates on a dictionary, the value assigned to the variable
``food`` is actually the *key*.  The output of this code is each of the keys (the
food names), one on each line.

Now, run this code.  Run it several times.  What do you notice?  In all
likelihood, the ordering changes for the food names.  We cannot rely on the keys
to be kept in order when we use a dictionary.  If we want the keys to be sorted
alphabetically, we would need to do something like what we see in
Listing :numref:`%s <sorted_dict_iter>`.

.. _sorted_dict_iter:
.. code-block:: python
   :linenos:
   :caption: Iterating through keys of a ``dict``

   for food in sorted(calories.keys()):
       print(food)

``keys()`` creates a ``list`` of the keys in ``calories``.  ``sorted`` then returns a
new ``list`` with the keys in alphabetical order.

If you're curious why the keys are ordered differently when you iterate through
them using a loop, you'll learn more when you take a class on data structures
and learn about *hash tables*. Hash tables are used to make dictionaries.  (Very
curious readers should look on YouTube for a video from PyCon 2010 titled
"Mighty Dictionary." This will give you an idea how hash tables work and how
they organize the internals of a dictionary.)

.. _sec_dict_exercises:

Exercises
---------

#. Given the following ``dict`` definition

   .. code-block:: python

      d = {"a" : 1, "b" : 2, "c" : 3}

   write the type and value of each of the following expressions.  If there is an error, state the error instead.

   a. ``d``

   b. ``d["b"]``

   c. ``d[2]``

   d. ``d["x"]``

   e. ``"c" in d``

   f. ``3 in d``

#. Given the following ``dict`` definition

   .. code-block:: python

      d = {"a" : 1, "b" : 2, "c" : 3}

   write code that adds a new key ``"d"`` and gives it the value ``4``, and then modifies the key ``"c"`` and gives it the value ``"radish"``.

#. Write a function that stores a ``dict`` to a file.  The function's name should be ``dict_to_file`` and it should have two parameters.  The first parameter should be the ``dict``.  The second parameter should be the new file's name.  Assume that each key is a ``str`` and each value is also a ``str``.  The format of the file should be each key on a line followed by its value on the next line.

#. Write a function that creates a ``dict`` and fills its contents using lines from a file.  The function's name should be ``file_to_dict`` and it should have one parameter: the name of the file.  The function should return the ``dict`` it creates.  Assume the file's format consists of a key on a single line followed by the key's value on the line after it.  Also assume both the key and the value are strings.

#. Write a function that stores a ``dict`` that maps strings to lists into a file.  The function's name should be ``str2list_to_file`` and it should have two parameters.  The first parameter should be the ``dict``.  The second parameter should be the new file's name.  Assume that each key is a ``str`` and each value is a ``list``.  The format of the file should be each key on a line followed by a series of lines, where each line is an item in the ``list``.  The lines that are keys should be prefixed with the string ``"K:"``.  This will tell us which lines are keys and which are values.

   For example, suppose we define

   .. code-block:: python

      names = { "Anderson" : ["Steve", "Tyler"], "Smith" : [Susie, Aaron] }

   calling ``str2list_to_file(names, "names.txt")`` should create a file named ``names.txt`` that has the contents

   .. code-block:: none

      K:Anderson
      Steve
      Tyler
      K:Smith
      Susie
      Aaron
