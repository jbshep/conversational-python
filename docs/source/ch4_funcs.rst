.. include:: <isonum.txt>

.. _ch_funcs:

Functions
=========

.. _sec_func_intro:

Introduction to Functions
-------------------------

Consider Listing :numref:`%s <one_prog>`.

.. _one_prog:
.. code-block:: python
   :linenos:
   :caption: One program consisting of two sub-programs

   print("This is program one.")
   x = input("Enter a string: ")
   if x[0].lower() in "aeiou":
       print("That string starts with a vowel.")
   else:
       print("That string does not start with a vowel.")

   print("This is program two.")
   x = input("Enter a string: ")
   if x.isalnum():
       print("That string only contains only a-z's and 0-9's.")
   else:
       print("That string contains some \"weird\" characters.")

Each of these two sections of code are supposed to be their own separate
programs.  If I type this code into one code file and run it, of course, both
programs will be executed, one after the other.  This is, after all, how
programs work.  Python executes each statement, one after another, and since
"program one" comes before "program two," all of program one's statements will
be executed and then all of program two's statements will be executed.

In program one, we are checking the first character of ``x`` using the expression
``x[0]`` (see line 3 of Listing :numref:`%s <one_prog>`).  We change it to lowercase,
and then we use the ``in`` operator to see if that single character is a vowel.
Without using the ``in`` operator, we would need to write an ``if`` statement
that looks something like this.

.. code-block:: python

   if x[0].lower() == "a" or x[0].lower() == "e" or \
      x[0].lower() == "i" or x[0].lower() == "o" or \
      x[0].lower() == "u":

Yuck.

Let’s try something new.  Let's construct Listing :numref:`%s <two_progs1>` by
modifying Listing :numref:`%s <one_prog>` using a new language construct.

.. _two_progs1:
.. code-block:: python
   :linenos:
   :caption: First functions example, attempt 1

   def one():
       print("This is program one.")
       x = input("Enter a string: ")
       if x[0].lower() in "aeiou":
           print("That string starts with a vowel.")
       else:
           print("That string does not start with a vowel.")
   
   def two():
       print("This is program two.")
       x = input("Enter a string: ")
       if x.isalnum():
           print("That string only contains only a-z’s and 0-9’s.")
       else:
           print("That string contains some \"weird\" characters.")


Now run this code.  What happens?  Yes, nothing!  There is absolutely no output,
which suggests that none of our statements ran.  Oh dear.  Well, let’s add a bit
more code (see the highlighted lines in Listing :numref:`%s <two_progs2>`).  

.. _two_progs2:
.. code-block:: python
   :linenos:
   :emphasize-lines: 17,18
   :caption: First functions example, attempt 2

   def one():
       print("This is program one.")
       x = input("Enter a string: ")
       if x[0].lower() in "aeiou":
           print("That string starts with a vowel.")
       else:
           print("That string does not start with a vowel.")

   def two():
       print("This is program two.")
       x = input("Enter a string: ")
       if x.isalnum():
           print("That string only contains only a-z’s and 0-9’s.")
       else:
           print("That string contains some \"weird\" characters.")
   
   # Add the following line.
   one()

Try again.  Aha!  Only the statements of code listed underneath ``def one():`` are
executed.  Now, try changing ``one()`` to ``two()`` on line 18 in
Listing :numref:`%s <two_progs2>`.  Run it.  Now only the statements under ``def
two():`` are executed.

What’s happening here?  Any code that is not indented at all is considered part
of the *main* program.  Code that is indented beneath a line that starts with
``def`` is like a little mini-program.  ``def`` stands for "define."  In this case,
we are defining a mini-program and giving it a name.  Mini-programs are better
known as... (\*drum roll please\*)... *functions*!

So, in Listing :numref:`%s <two_progs2>`, the main program is simply on lines 17 and
18 (though line 17 is just a comment).  Let's change the main program to see
what happens.  See Listing :numref:`%s <two_progs3>` (specifically lines 17 - 19).

.. _two_progs3:
.. code-block:: python
   :linenos:
   :emphasize-lines: 17,18,19
   :caption: First functions example, attempt 3

   def one():
       print("This is program one.")
       x = input("Enter a string: ")
       if x[0].lower() in "aeiou":
           print("That string starts with a vowel.")
       else:
           print("That string does not start with a vowel.")
   
   def two():
       print("This is program two.")
       x = input("Enter a string: ")
       if x.isalnum():
           print("That string only contains only a-z’s and 0-9’s.")
       else:
           print("That string contains some \"weird\" characters.")

   print("Main: calling a function.")
   two()
   print("Main: end of program.")

Run this, and notice what happens.  The code starts in the main non-indented
section by printing ``"Main: calling a function."`` Then, the expression ``two()``
calls the function, which makes the program "jump" up to the definition of the
function, which starts with ``def two():``.  Each of the statements indented under
``def two():`` are executed, one by one, and then once those statements are
finished, we jump back down to where ``two()`` was called in the first place.
Finally, the main program resumes and we print ``"Main: end of program."``

In a sense, functions are like "tangents" (not the math kind of tangent -- the
tangent where we deviate from a conversation to another topic briefly)  With
functions, we can momentarily leave the main program to execute some
pre-prepared code.  We have been *calling* functions throughout the entire book
already.  We have used functions like ``print``, ``input``, and ``int``.  Now we have
a sense of how to *define* our own new functions.

When we define a new function, we give the function a name and we give the
function an indented section known as the function's *body*.  There can be more
pieces to a function as well, and we will learn about those in the next
few sections.

.. _sec_params:

Parameters
----------

Let’s look at another example of how we can define our own functions that we can
call later.  Suppose, at a certain fictitious university named Higher Ed
University, students are given email addresses that follow a naming convention.
To form the email address, we take the first four characters of a student’s last
name, then the first three characters of a student’s first name, and then append
"@heu.edu" to it.  We could write a function to determine and print out such an
email address.

.. _print_email:
.. code-block:: python
   :linenos:
   :caption: Defining `print_email`

   def print_email(first, last):
       username = last.lower()[0:4]
       username = username + first.lower()[0:3]
       print("%s@heu.edu" % username)

Notice that the ``print_email`` function is defined differently than ``one`` or
``two`` in Listing :numref:`%s <two_progs3>` in Section :numref:`%s <sec_func_intro>`.  In our previous example when we defined those functions, their definitions
had empty parentheses after the function name.  Now, we have two things that
look a lot like variables inside the parentheses.  In fact, they are variables,
and their values are used inside the function’s body.  Variables that are given
inside the parentheses in a function definition are called the function’s
*parameters*.

Let us call this function.  We might type this.

.. code-block:: python

   print_email("Jack", "Jackson")

This would print:

.. code-block:: none

   jackjac@heu.edu

Or, if we typed this:

.. code-block:: python

   print_email("Shania", "Carrington")

It would print:

.. code-block:: none

   carrsha@heu.edu

How does this work?  When we call a function, we must provide the correct number
of values to the function, in the right order.  The correct number of values is
based on how many parameters the function has.  In this case, the function
``print_email`` has two parameters, ``first`` and ``last``.  The *values* we pass to
the definition of a function are called the *arguments*.  When a function is
called, the arguments' values become the parameters' values.  Thus, ``first`` gets
the value ``"Shania"`` and ``last`` gets the value ``"Carrington"``.

Clever readers might suspect that this function has a bug.  It looks like if the
last name is fewer than four characters long or the first name is fewer than
three characters long, the program would crash.  Surprisingly, in Python the
string range operator is very forgiving.  If you were to type the expression
``"abc"[0:20]``, the substring returned will still be ``"abc"``.  We can read this
substring operation aloud as “Start at index 0 and return any characters up to
index 20, if it exists.”  Therefore, there is no bug, but skeptical thinking
like this will help us as we program in the future.

What happens when you switch the order of the arguments?

.. code-block:: python

   print_email("Carrington", "Shania")

What happens if you do not have the correct number of arguments?

.. code-block:: python

   print_email("Shania")

Try these things on your own to see what happens.  Try to guess what they do
before you actually run the code.  If they produce errors, make a mental note of
what the error looks like.  That way, if you encounter that error again in the
future, you'll know what caused it and how to fix it.

Let's move on to a different example.  Let us write code that defines a new function, and then let's write some code to call that new function (see Listing :numref:`%s <print_money>`).

.. _print_money:
.. code-block:: python
   :linenos:
   :caption: Defining and calling `print_money`

   def print_money(amount):
       print("$%.2f" % amount)
   
   my_money = 50.25
   print_money(my_money)

This code will print:

.. code-block:: none

   $50.25

It does not matter when we give an argument to a function call if we provide a
value or an expression that returns a value (in this case, the name of a
variable).

Now, let’s make one more change to the code (see Listing
:numref:`%s <print_money_change_var>`).

.. _print_money_change_var:
.. code-block:: python
   :linenos:
   :emphasize-lines: 3,7
   :caption: Defining and calling `print_money`, attempt 2

   def print_money(amount):
       print("$%.2f" % amount)
       amount = amount + 10.00
   
   my_money = 50.25
   print_money(my_money)
   print_money(my_money)

In this example, we are doing something new.  We are taking the parameter
``amount`` and actually changing its value in the last statement of the function’s
body.  Where does ``amount``’s value come from?  It is passed the value of
``my_money`` down in the main program.  One thing we should look out for is “side
effects.”  Does changing the value of ``amount`` have any effect on the value of
``my_money``?  In other words, does changing ``amount`` also change ``my_money``?  If
it did, we would expect the second call to ``print_money`` to print a different
value than the first.

As it turns out, when we run the code, we see this:

.. code-block:: none

   $50.25
   $50.25

Changing ``amount`` does not change ``my_money``.  This is because arguments are
passed to parameters in Python using their value alone.  This is called *pass by
value*.  If changing the parameter had actually changed the argument, then we
would have said Python practices *pass by reference*, where a reference to the
original variable would have been given to the function rather than just the
value.  Remember that Python uses pass by value when you are writing function
definitions.

It is generally bad programming practice to change the values of parameter
variables in the body of a function -- again, generally speaking -- but there are
exceptions.  For the most part, a programmer should be able to consult the
parameters at any point in the function’s body to see what the “input” to the
function was.  There is one situation, however, where it is desirable to modify
the parameter values passed to a function.  We will discuss this situation in
Chapter :numref:`%s <ch_lists>`.

Terminology time!  The first line of a function definition is called the
function's *signature*.  The signature tells us the name of the function and how
many parameters it has.  For example, suppose we have the following function
signature.

.. code-block:: python

   def print_uppercase(words):
       # function body omitted

We can see from this signature that if we want to call this function, we must
use the name ``print_uppercase`` and we must pass one argument to the function.
The argument will be assigned to the parameter ``words``.

We will use the term signature again in this book, so you should learn to use
it, too!

.. _sec_ret_vals:

Return values
-------------

If we think of functions in terms of them being like mini-programs, we might
observe that programs tend to ask for input, they doing something with the
input, and then finally they produce output.  In a sense, parameters give
programmers the ability to pass “input” to a function.  What then might we do to
allow functions to provide “output” back to the main program?

As you might recall, we have already seen functions that do this -- functions that
Python already has defined for us.  For example:

.. code-block:: python

   ssn = input("Enter your social security number: ")

``input`` is a function.  It allows the programmer to provide an argument, which
is the string to use for prompting the user.  We can imagine that somewhere,
some programmer has written a function definition for ``input`` that looks
something like this:

.. code-block:: python

   def input(prompt):
       # Code that makes input work goes here.

Notice that the ``input`` function returns a value, which we then assign to a
variable.  In a function’s body, we can tell Python what value to return using
the ``return`` statement.  Let's start with an overly simple example so that we
understand the mechanics of the ``return`` keyword.  Suppose we define the
function shown in Listing :numref:`%s <forty_two>`.

.. _forty_two:
.. code-block:: python
   :linenos:
   :caption: A function that always returns 42 no matter what

   def favorite_number():
       return 42
   
   number = favorite_number()
   print(number)

Whenever a ``return`` statement is encountered in a function’s body, the function
stops immediately and returns to where the function was called.  The value that
is returned from the function is whatever value was listed in the ``return``
statement.  In Listing :numref:`%s <forty_two>`, there is only one statement in the
body of the ``favorite_number`` function: the return statement itself.

To interpret the code in Listing :numref:`%s <forty_two>`, we start at line 4, which
is the first line of the main program.  The ``favorite_number`` function is
called, so the program "jumps" up to ``favorite_number``'s definition.  The
program enters the function's body and encounters the ``return`` statement.  The
``42`` listed in the ``return`` statement causes the function to end, and the value
``42`` is sent back to line 4.  Finally, line 4 can finish as the ``42`` is assigned
to the variable ``number``.

Now, let's see how a function might take a parameter value and then return
something based on the parameter value.  To experiment with this, we will define
a function named ``next_int`` that takes an integer as a parameter.  Whatever
integer is given, the function will return the "next" integer.  If we give
``next_int`` the value ``3``, it will return ``4``.  Said another way, ``next_int(3) ==
4``.  If we give ``next_int`` the value ``-2``, it will return ``-1``.  Said another
way, ``next_int(-2) == -1``.  We define ``next_int`` in Listing :numref:`%s <next_int>`.

.. _next_int:
.. code-block:: python
   :linenos:
   :caption: Function definition for `next_int`

   def next_int(int_value):
       next_value = int_value + 1
       return next_value

Now, let's call our function and print its resulting value:

.. code-block:: python

   print(next_int(3))
   print(next_int(-2))

which produces the following output:

.. code-block:: none

   4
   -1

Notice in ``next_int``'s function body how we create a new variable named
``next_value``.  ``next_value`` holds the value we will return from our function.
There is no rule that says we must return the value of a variable.  Any
expression that produces a value can follow the ``return`` keyword.  In other
words, we could have simply returned ``int_value + 1``, as shown in
Listing :numref:`%s <next_int2>`.

.. _next_int2:
.. code-block:: python
   :linenos:
   :caption: Function definition for `next_int`

   def next_int(int_value):
       return int_value + 1

Time to move on and look at a different example function.  Consider
Listing :numref:`%s <pig_latin_word>`.

.. _pig_latin_word:
.. code-block:: python
   :linenos:
   :caption: Function definition for `piglatin`

   def piglatin(english):
       if english[0] in "aeiou":
           return english + "-way"
       else:
           return english[1:] + "-" + english[0] + "ay"

Whenever a ``return`` statement is encountered in a function’s body, the function
stops immediately and returns to where the function was called.  The value that
is returned from the function is whatever value is given to the return
statement.  Maybe you already understand this, but it bears repeating because it
is very important to understand this concept if you are going to be able to
understand functions.

In Listing :numref:`%s <pig_latin_word>`, we have a function named ``piglatin``.  This
example comes from the exercises in Section :numref:`%s <sec_loops_exercises>` from
Chapter :numref:`%s <ch_loops>`.  We can pass to ``piglatin`` an English word, and for
simplicity’s sake, suppose the word always consists solely of lowercase letters.
We are only handling two cases for now: 1.) the word starts with a vowel, or 2.)
the word starts with a single consonant letter.

A function may have zero, one, or many return statements, but as soon as the
program encounters a return statement, the function ends and the value is
returned immediately.

How might we call this function?  There are several ways we could do it.

.. code-block:: python

   engword = "apple"
   pigword = piglatin(engword)
   print("The pig latin of apple is %s." % pigword)
   
   print("The pig latin of catalog is %s." % piglatin("catalog"))

Since ``piglatin`` returns a string, we can call ``piglatin`` anywhere we would
normally put a string.

It's hard for new programmers to learn to write their own functions.  It takes
practice.  It's helpful to see how to define a lot of example functions, and
it's also helpful to try writing your own functions and seeing what problems you
run into.  Let's take a look at a bunch of example functions, and at some point,
you should go back and try to define these functions on your own without looking
at the code.

Listing :numref:`%s <get_area>` is a function definition that, given the radius of a
circle, will return the area of the circle.

.. _get_area:
.. code-block:: python
   :linenos:
   :caption: Function definition for `get_area`

   import math
   
   def get_area(radius):
       return math.pi * radius * radius

Listing :numref:`%s <roll>` is a function definition that simulates rolling a
6-sided die.

.. _roll:
.. code-block:: python
   :linenos:
   :caption: Function definition for `roll`

   import random
   
   def roll():
       return random.randint(1, 6)

Listing :numref:`%s <posintsum>` defines a function named ``posintsum`` that prints
the sum of the first ``n`` positive integers.  The listing also shows how you
might call this function.  For example, ``posintsum(4)`` would calculate the
result of ``1+2+3+4`` as ``10``.  As another example, ``posintsum(10)`` would
calculate the result of ``1+2+3+4+5+6+7+8+9+10`` as ``55``.  Note how we use a ``for``
loop and a variable named ``total`` to accomplish this before returning the result
in ``total``.

.. _posintsum:
.. code-block:: python
   :linenos:
   :caption: Function definition and sample function calls for `posintsum`

   def posintsum(n):
       total = 0
       for i in range(1, n+1):
           total += i
       return total
   
   print("1+2+3+4 = %d" % posintsum(4))
   print("1+2+3+4+5+6+7+8+9+10 = %d" % posintsum(10))

What if we had forgotten the return statement at the end of the function?  In
other words, what if our function definition looked like
Listing :numref:`%s <posintsum_missing_return>`?

.. _posintsum_missing_return:
.. code-block:: python
   :linenos:
   :emphasize-lines: 5
   :caption: Forgotten `return` statement in `posintsum`

   def posintsum(n):
       total = 0
       for i in range(1, n+1):
           total += i
       # Oh no! I need to remember to actually return total.

As it turns out, all functions in Python return something no matter what.  If a
function does not have a ``return`` statement, the function will return a special
value known as ``None``.  The type of the value ``None`` is ``NoneType``.  You may
have already seen ``None`` if you got confused on the difference between ``print``
and ``input``, as many new programmers do.  Suppose we did the following.

.. code-block:: python

   x = print("Enter a number: ")
   # Oops.  x == None

Clearly, we meant to use ``input`` rather than ``print``.  ``print`` returns ``None``.

.. _sec_func_mod:

Modularizing Code with Functions
--------------------------------

Now that we can make “mini-programs” using functions, we can begin composing
full programs made out of mini-programs.  We will use functions to help organize
our code so that our code is easier to read and easier to maintain.  This will
also make it easier to cope with errors, particularly user error, as we will see
in the following example.  Let’s take an idea from the previous section and
suppose that we want to write a simple program that asks the user for a positive
integer ``n``.  Our program should print out the sum of all positive integers up
through that ``n``.  We will also want to only accept valid input, so we will need
to re-ask for input if what the user types is incorrect.  Examples of bad input
might be ``23r5`` (since there is a ``r`` in the number) or ``-2`` (since ``-2`` is
negative).

It is often difficult for novice programmers to know where to begin in writing a
program.  One very effective approach is to start by writing comments in English
that describe, step-by-step, what our program needs to do.  So, we might do
this.

.. code-block:: python

   # Ask for a positive whole number 'n' (i.e., a positive integer).

   # Compute the sum of 1 + 2 + ... + n and print it.

That’s a good start.  Now, let’s become "lazy" programmers.  Laziness is a good
thing in some situations, and this is one of those situations.  In fact, a
famous programmer named Larry Wall once stated that laziness is one of three
“virtues” that programmers should seek (look it up on the Web).

In order to be "lazy," we should pretend that someone has already defined
functions for us, and by calling these functions, our program will be done!

.. code-block:: python

   # Ask for a positive whole number 'n' (i.e., a positive integer).
   n = getposint()

   # Compute the sum of 1 + 2 + ... + n and print it.
   total = getsum(n)

   print("The sum of the first %d positive whole numbers is %d."
          % (n, total))

Hooray!  We’ve written our program in three lines of actual code!  Well, we
haven’t really, but now we can focus on the “pieces” of the program by defining

Now, let’s try to define ``getsum`` in Listing :numref:`%s <getsum>`.  Keep in mind
that ``getsum`` has a single argument, so it needs a single parameter, too.

.. _getsum:
.. code-block:: python
   :linenos:
   :caption: Function definition for `getsum`

   def getsum(n):
       total = 0
       for i in range(1, n+1):
           total += i
       return total

Note that in line 3 of Listing :numref:`%s <getsum>` the second expression in
``range`` is ``n+1``.  Since we want to add up all the values from ``1`` to ``n``, the
value that will make us leave the look is one more than ``n``, that is, ``n+1``.
the functions that will actually make this program work.  Let’s define
``getposint`` first (see Listing :numref:`%s <getposint>`).

.. _getposint:
.. code-block:: python
   :linenos:
   :caption: Function definition for `getposint`

   def getposint():
       s = input("Enter a positive whole number: ")
       while not s.isdigit() and s != "0":
           print("Sorry, that does not look like a positive whole
                  number.  Please try again.")
           s = input("Enter a positive whole number: ")
       return int(s)

Writing functions takes practice.  The more you try, the better you will get at
it.  A program with everything defined is shown in
Listing :numref:`%s <compute_posintsum>`.

.. _compute_posintsum:
.. code-block:: python
   :linenos:
   :caption: Code composed with functions

   def getposint():
       s = input("Enter a positive whole number: ")
       while not s.isdigit() and s != "0":
           print("Sorry, that does not look like a positive whole
                  number.  Please try again.")
           s = input("Enter a positive whole number: ")
       return int(s)
   
   def getsum(n):
       total = 0
       for i in range(1, n+1):
           total += i
       return total


   # Ask for a positive whole number 'n' (i.e., a positive integer).
   n = getposint()

   # Compute the sum of 1 + 2 + ... + n and print it.
   total = getsum(n)

   print("The sum of the first %d positive whole numbers is %d."
          % (n, total))

Sometimes, programmers even like to put their main program code into its own
function.  That way, all of the code exists in some function.
Listing :numref:`%s <compute_posintsum_final>` shows how we would do this.

.. _compute_posintsum_final:
.. code-block:: python
   :linenos:
   :caption: Code composed with functions, using \kode{main}

   def getposint():
       s = input("Enter a positive whole number: ")
       while not s.isdigit() and s != "0":
           print("Sorry, that does not look like a positive whole
                  number.  Please try again.")
           s = input("Enter a positive whole number: ")
       return int(s)
   
   def getsum(n):
       total = 0
       for i in range(1, n+1):
           total += i
       return total
   
   def main():
       # Ask for a positive whole number 'n' (i.e., a positive integer).
       n = getposint()
   
       # Compute the sum of 1 + 2 + ... + n and print it.
       total = getsum(n)
   
       print("The sum of the first %d positive whole numbers is %d."
              % (n, total))
   
   # Run the program by calling main().
   main()

Some other programming languages like C++ and Java actually require programs to
start by calling a function named ``main``.  If we always put our main program
code into a function named ``main``, it will ease our transition from Python to
other languages.

.. _sec_var_scope:

Variable Scope
--------------

You may have noticed in the previous section that our programs are starting to
get longer in terms of number of lines of code (LOC).  As our programs get
longer, we will start to define more variables to help our programs do their
work.  Eventually, we will find that sometimes we can't access a variable in one
part of the program that is defined in another part of the program.  This is due
to *variable scope*.  The *scope* of a variable is the part of the code where
the variable can be accessed.  In terms of accessing a variable, we need to make
the distinction between *reading* a variable's value and *writing* to a
variable's value.  Reading a variable means using--but not modifying--its
current value.  Writing to a variable means modifying its value.  Consider the
following code.

.. code-block:: python

   y = x + 1

In this code, we are *reading* from ``x``.  We are *writing* to ``y``.  When we say
*access* a variable's value, we mean the same thing as *reading* the variable.

Now, let's explore the notion of variable scope.  Consider the (non-working)
code in Listing :numref:`%s <sumsq_no_init>`.

.. _sumsq_no_init:
.. code-block:: python
   :linenos:
   :caption: Sum of squares, with `NameError`

   for k in range(1, 11):
       square = k * k
       total = total + square
   
   print(total)

The code in Listing :numref:`%s <sumsq_no_init>` is supposed to compute the sum of
squares, that is, 1\ :sup:`2` + 2\ :sup:`2` + 3\ :sup:`2` + ... + 10\ :sup:`2`.  It computes each square's
value and adds it to a variable named ``total``.  However, when we run the code,
we get the following error.

.. code-block:: none

   Traceback (most recent call last):
     File "<stdin>", line 3, in <module>
   NameError: name 'total' is not defined

Let's take a closer look at line 3.

.. code-block:: python

   total = total + square

On the right-hand side (RHS) of the ``=`` in line 3, we are *reading* from both
``total`` and ``square``, and then adding their values together.  Since we did not
previously define ``total``, it is not yet *in scope*.  The error produced in
Python is called a ``NameError`` because Python doesn't have information about a
variable named ``total``.  To correct this problem, we must *initialize* ``total``
with a starting value.  Initializing a variable means to create the variable by
giving it a starting value. Listing :numref:`%s <sumsq>` shows the corrected code.
Note that ``total`` is created prior to the start of the loop.

.. _sumsq:
.. code-block:: python
   :linenos:
   :emphasize-lines: 1
   :caption: Sum of squares, corrected

   total = 0
   for k in range(1, 11):
       square = k * k
       total = total + square

   print(total)

Always remember to initialize your variables.

Say it again: a variable's scope is the part of the program where the variable
may be accessed (i.e., "read").

We are bringing up the topic of variable scope in this chapter because variable
scope has particular relevance in functions. Suppose we were to write the code
in Listing :numref:`%s <local_variable_bogus>`.

.. _local_variable_bogus:
.. code-block:: python
   :linenos:
   :caption: Local variable example

   import math
   
   def main():
       people = 10
       slices_per_pizza = 12
       slices_per_person = 3
       pizzas = number_of_pizzas()
       print("You need to order %d pizzas." % pizzas)
   
   def number_of_pizzas():
       return math.ceil(people * slices_per_person / slices_per_pizza)
   
   main()

Take a gander at Listing :numref:`%s <local_variable_bogus>` and try to guess
what might happen?  Well, what do you think?  Try to come up with a few
possibilities.  On one hand, it might set the variables ``people``,
``slices_per_pizza``, and ``slices_per_person``, and then use them to calculate
the number of pizzas one needs to order.  Another possibility is that the
program crashes hideously...  but why?

Try running this code on your own.  Of course, it ends up crashing.  This code
is a hot mess!  The error reads as follows.

.. code-block:: none

   Traceback (most recent call last):
     File "test.py", line 13, in <module>
       main()
     File "test.py", line 7, in main
       pizzas = number_of_pizzas()
     File "test.py", line 11, in number_of_pizzas
       return math.ceil(people * slices_per_person / slices_per_pizza)
   NameError: name 'people' is not defined

When the code reaches the ``number_of_pizzas`` function, it does not remember that
there is a variable named ``people`` that was defined in the ``main`` function.
That's interesting.  This suggests that when we define a variable within a
function's body, that variable is only visible within that function.

Think about it this way.  Functions are like little houses.  What happens in
your house is your business.  Other people shouldn't be able to see in your
house from within their house.

So, if we define a variable in one function, it only "lives" in that function.
This is a good thing!  It means that if you define a variable somewhere in your
program, a function you call can't mess with the variables you've already
defined.  If a function could mess with your variables without you being aware
of it, then your program could have unintended side effects.  If functions had
surprising side effects, it would be very difficult to reason through programs
and predict their behavior and output.  One of the great things about computers
is that they are logical and predictable.

A variable that is defined inside a function is called a *local variable*.  If
we define a variable in the body of a function, we say that the variable is
*local* to that function.  In this case, the variables ``people``,
``slices_per_pizza``, and ``slices_per_person`` are local variables in ``main``.

All right, let's fix the problem.  The best thing to do is to pass
these values to the ``number_of_pizzas`` function, which means we'll need
``number_of_pizzas`` to have three parameters in its definition, as we can see in
the updated code found in Listing :numref:`%s <local_variable_good>`.

.. _local_variable_good:
.. code-block:: python
   :linenos:
   :emphasize-lines: 4,7
   :caption: Local variable example, fixed

   import math
   
   def main():
       pizzas = number_of_pizzas(10, 12, 3)
       print("You need to order %d pizzas." % pizzas)
   
   def number_of_pizzas(people, slices_per_pizza, slices_per_person):
       return math.ceil(people * slices_per_person / slices_per_pizza)
   
   main()

Hey, this works splendidly!

Let's go back to the "houses" metaphor we presented a few paragraphs ago. Recall
that I asked you to think of functions as being like little houses.  What do you
think happens when you define a variable outside of all the "houses."  In other
words, what if I define a variable in what is normally the main part of the
program that exists outside of any function's body?  Consider
Listing :numref:`%s <global_bogus>`, where you'll notice we've done away with a
``main`` function entirely.

.. _global_bogus:
.. code-block:: python
   :linenos:
   :caption: Global variable example

   balance = 10000
   
   def withdraw(amount):
       if balance >= amount:
           balance =  balance - amount
   
   withdraw(1000)
   print(balance)

If you run Listing :numref:`%s <global_bogus>`, you'll see there is a problem.
We'll resolve the problem shortly, however let's consider the intent of the
code.  The main program consists of three lines of code.  They are (in order):

.. code-block:: python

   balance = 10000
   withdraw(1000)
   print(balance)

After we have defined ``balance``, we define a function named ``withdraw`` that can
be used to subtract an amount of money from ``balance``, but only if there is
sufficient money available in ``balance``.

Since ``balance`` is not defined in the body of any function, it is known as a
*global variable*.  Global variables are accessible anywhere in the program,
including inside functions.  Consider the following code.

.. code-block:: python

   gl = 7
   
   def f(x):
       return x + gl
      
   print(f(3))

As we would expect, this code prints ``10``.

Although global variables are accessible (i.e., they may be "read") from within
functions, they cannot be modified from within a function unless we explicitly
tell Python that's what we intend to do.  Do you remember a little bit ago when
I said that if function could mess with your variables without you being aware
of it, then your program could have unintended side effects, and that side
effects are bad?  Well, here we are again.  If you ran the code in
Listing :numref:`%s <global_bogus>`, you would see this:

.. code-block:: none

   Traceback (most recent call last):
     File "variable_scope.py", line 38, in <module>
       withdraw(1000)
     File "variable_scope.py", line 35, in withdraw
       if balance >= amount:
   UnboundLocalError: local variable 'balance' referenced before assignment

Python assumes that any variable you wish to *write* to inside a function is a
local variable, even if there is a global variable of the same name.  Python
does allow us to write to global variables, but we have to tell Python that we
intend to do so and that we know the potential consequences!  We can use the
*global* statement to allow a function to write to a global variable; see
Listing :numref:`%s <global_good>`.

.. _global_good:
.. code-block:: python
   :linenos:
   :emphasize-lines: 4
   :caption: Global variable example, fixed

   balance = 10000
   
   def withdraw(amount):
       global balance
       if balance >= amount:
           balance =  balance - amount
   
   withdraw(1000)
   print(balance)

The output of Listing :numref:`%s <global_good>` is now ``9000``, as we would expect.

``global`` should be used sparingly.  It is generally better to pass values to
functions rather than storing those values in global variables, though in some
cases we will manage common information in global variables, especially when we
program video games.  Stay tuned!


.. _sec_funcs_recursion:

(Optional) Recursion
--------------------

This is the first "optional" section you get to encounter in this book.  The optional sections are intended for readers who have maybe programmed before and want to learn more and seek out an additional challenge.  You can skip over this section if you'd like.  This section deals with a concept called *recursion*.  Recursion happens when a function calls *itself* within its own body.  It is a powerful and awesome idea that shows up a lot in advanced computer science courses.

How and why would a function call itself?  That sounds weird, doesn't it?  And why would it be a powerful and awesome thing to use?  Let's tackle the first question.

Consider Listing :numref:`%s <infty_recur>`.

.. _infty_recur:
.. code-block:: python
   :linenos:
   :caption: Simple yet infinite recursion

   def call_me(n):
       print(n)
       call_me(n - 1)

   # Try it out.
   call_me(10)

The function ``call_me`` looks simple enough. It takes an integer as its parameter, it prints that integer to the screen, and then it calls the very same function again but this time with one less.  Thus, if a program called ``call_me(10)``, that function would print ``10`` and then would execute ``call_me(9)``.

Well, if ``call_me(10)`` prints ``10`` and then executes, ``call_me(9)``, what does ``call_me(9)`` do?  It would print ``9`` and call ``call_me(8)``.  Uh oh.  Do you see a pattern here?  Actually try to run the code in Listing :numref:`%s <infty_recur>`.  What happens?

You might think "infinite loop" (even though there's no real loop here), and you'd be generally correct!  However, the "loop" does actually end.  Check this out:

.. code-block:: none

   10
   9
   8
   7
   6
   5
   4
   3
   2
   1
   0
   -1
   -2
   # ... I omitted a lot of lines from the output -- otherwise this
   # ... section would be ridiculously long.
   -977
   -978
   -979
   -980
   -981
   -982
   -983
   -984
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "<stdin>", line 3, in call_me
     File "<stdin>", line 3, in call_me
     File "<stdin>", line 3, in call_me
     [Previous line repeated 992 more times]
     File "<stdin>", line 2, in call_me
   RecursionError: maximum recursion depth exceeded while calling
   a Python object

This output and error tells us that there is a limit to how many times a function can call itself.  Actually, it is more correct to say there is a limit to how many functions we can "stack" on top of functions before the program runs out of "stack space."  A more detailed explanation is unfortunately beyond the scope of this book.  In a book on computer architecture or operating systems, you can learn about something called an *activation record* or *stack frame* that manages the execution of a function, but again, that's way farther than we need to go now.

So, what do we do?  Well, any recursive function needs to have a way to know when to stop calling itself.  We can use an ``if`` statement to stop things.  Consider Listing :numref:`%s <basic_recur>`.

.. _basic_recur:
.. code-block:: python
   :linenos:
   :emphasize-lines: 3
   :caption: Simple recursion

   def call_me(n):
       print(n)
       if n > 1:
           call_me(n - 1)

   # Try it out.
   call_me(10)

Thus, when ``n`` is 1, the program will have printed ``1`` but will not execute ``call_me(0)``.  If we executed ``call_me(4)``, for example, the following traces how the function would call itself to print each number.

.. code-block::

   call_me(4)
   print(4), call_me(3)
   print(4), print(3), call_me(2)
   print(4), print(3), print(2), call_me(1)
   print(4), print(3), print(2), print(1)

What is the point of all this?  As it turns out, recursion is a powerful technique for solving certain types of problems.  How do we know when to use it?  If we can describe a problem in terms of smaller versions of the problem itself, that problem is a good candidate for using recursion.

Let's look at a simple example.  Perhaps you remember what a *factorial* is.  If not, rather than give a rigorous mathematical definition, let's learn by example.  The factorial of 3 is written :math:`3!` (note the exclamation mark) and it means :math:`3\times2\times1`.  Since :math:`3\times2\times1 = 6`, that means :math:`3! = 6`.

With that example in mind, what do you think the factorial of 4 would be (that is, what is :math:`4!`)?  If you guessed :math:`4\times3\times2\times1 = 24`, you would be correct.  Thus, :math:`4! = 24`.

Why do we care about factorials?  There are many applications of factorials, especially in the field of probability when we want to count things quickly.  Here's an example.  Suppose we have four different books that we want to arrange on a shelf.  How many ways could we do it?  Let's call the books A, B, C, and D.  There are four choices for the first book we place.  Once we place the first book, there are three books left to select from for the second book.  Once we've placed two books, there are two books left to choose from for the third book.  Once we've placed three books, there is only book left.  Thus, there are :math:`4\times3\times2\times1 = 4!` different ways to arrange the books.

This is just a basic example.  There are far more interesting examples of problems that involve factorials, but they take longer to set up and investigating them would be quite a tangential diversion.  Hopefully you will encounter problems like this in a course or book on discrete mathematics or probability.  It's all very interesting.

So, let's use recursion to program a factorial function.  Where to begin?  Remember what we said earlier: "If we can describe a problem in terms of smaller versions of the problem itself, that problem is a good candidate for using recursion."  So, let's make an observation.  We know, for example, that

.. math::

   4! = 4\times3\times2\times1

and

.. math::

   3! = 3\times2\times1

therefore

.. math::

   4! &= 4\times(3\times2\times1) \\
      &= 4\times3!

If we play around, we'll see this pattern with any factorial.  The factorial of a number is just that number times the factorial of one less than that number.  So, for any arbitrary integer :math:`n`,

.. math::

   n! = n\times(n-1)!

and also

.. math::

   1! = 1

We can combine the two definitions above to define our function below.

.. _recur_fact:
.. code-block:: python
   :linenos:
   :caption: A recursive factorial function

   def factorial(n):
       if n == 1:
           return 1
       else:
           return n * factorial(n - 1)

This is a typical setup for the definition of a recursive function.  They often look something like this:

.. _recur_general:
.. code-block:: python
   :linenos:
   :caption: Generalized form of a recursive function

   def recur(n):
       if n is the stopping condition
           return initial value
       else:
           return the result of a smaller recursive piece of the problem
                 ( like recur(n-1) )

We can see a call to ``factorial(4)`` playing out as follows.

.. code-block::

   factorial(4)
   return 4 * factorial(3)
   return 4 * 3 * factorial(2)
   return 4 * 3 * 2 * factorial(1)
   return 4 * 3 * 2 * 1
   return 24

We will experience recursive functions again in an optional section found in Chapter :numref:`%s <ch_searchsort>`.  That's it for now, however!


.. _sec_funcs_exercises:

Exercises
---------

#. Determine the output of the following code.

   .. code-block:: python

      def f1():
          print("f1 called")
      
      def f2():
          print("f2 called")
      
      print("Main 1")
      f2()
      print("Main 2")
      f1()

#. Determine the output of the following code.

   .. code-block:: python

      def f1():
          print("f1 called")
          f2()
      
      def f2():
          print("f2 called")
      
      
      print("Main 1")
      f2()
      print("Main 2")
      f1()

#. Determine the output of the following code.

   .. code-block:: python

      def f1(x, y):
          z = x + y
          return z

      print("Answer: %d" % f1(3, 2))
      print("Answer: %d" % f1(2, 3))

#. Determine the output of the following code.

   .. code-block:: python

      def f1(x, y):
          z = 2 * x + y
          return z
      
      print("Answer: %d" % f1(3, 2))
      print("Answer: %d" % f1(2, 3))
      
#. Determine the output of the following code.

   .. code-block:: python

      def umkay(message):
          return message + ", umkay?"
      
      print(umkay("Do your homework"))
      

#. Define a function named ``circum`` that takes the radius of a circle as a parameter and returns the circumference of that circle.

#. Define a function named ``smallest`` that takes three float parameters and returns the smallest value of the three.

#. Define a function named ``find_vowel`` that takes a string as a parameter and returns the index of the first vowel in the string.

#. Define a function named ``count_words`` that takes a string as a parameter and returns the number of words in the string (where words are separated by a single space).
