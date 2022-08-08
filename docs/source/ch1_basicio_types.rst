.. include:: <isonum.txt>

.. _ch_intro:

Basic I/O, Statements, Expressions, Variables, and Types
========================================================

Getting set up to program
-------------------------

Computers consist of hardware and software.  Hardware is the physical stuff you
can hold in your hands, like memory, disks, keyboards, etc.  Software tells the
hardware what to do.  The hardware stores the software and "runs" it.  In this
book, we're going to learn how to create software. Creating software is called
*programming* or *coding*.  When coding, we give the computer instructions for
it to do, and then we tell the computer to "run" or "execute" our code.

Typically, hardware consists of a bunch of electrical circuits.  Instructions
for controlling the circuits are called *machine code* (which is basically a
bunch of 1's and 0's that tell the computer which electrical circuits to turn on
and off... beep beep boop boop).  However, we will not need to learn machine
code or worry about electrical circuits.  We will write code that looks
something more like normal human language, and then we will use another software
program called a *compiler* or an *interpreter* to translate our nice, readable
code into machine code that will control the hardware.  Nice, eh?

The code we write will be written in a high-level programming language named
*Python*.  Although programming languages might look technical, they are more
human reader-friendly than the hardware's machine code language.
Figure :numref:`%s <interp>` shows the relationship between Python language code, the
interpreter, and the hardware.

.. _interp:
.. figure:: images/ch1/interp.jpg
   :scale: 50 %
   :alt: Code translated by an interpreter to hardware

   Code translated by an interpreter to hardware

To get started programming in Python, we will need to install two software
programs on our computer.  One program will help us write code for the computer
to execute.  The second program will run our code so that we can see what it
does.  The first program is named *Thonny*.  The second program is simply known
as the *Python interpreter*.  Fortunately, we don't need to download these two
programs separately.  When we download and install Thonny, Thonny contains the
Python interpreter as well for free!

Let's install Thonny, and by extension, the Python interpreter.

- Open your favorite Web browser, again (mine is Google Chrome).
- In your Web browser, go to the Web address http://thonny.org/.
- The Thonny Web page will appear.  In the upper-right hand you will see options
  to download Thonny for your computer.  If you have a Windows computer, choose
  Windows.  If you have Mac, choose Mac.  If you have Linux, choose Linux.
- Find the file that you've downloaded and double-click on it to run it.
- An installer program will be displayed.  Follow the steps in the installer to
  finish installing Thonny.  If you are unsure of what to do at a particular
  step, accept the default information in that step.

Now, find the Thonny program on your computer and run it.  The main Thonny
window is shown in Figure :numref:`%s <thonny_basic>`.

.. _thonny_basic:
.. figure:: images/ch1/thonny_basic.png
   :scale: 50 %
   :alt: The Thonny window, consisting of the Shell and the output

   The Thonny window, consisting of the Shell and the output


Notice that there are two "parts" to the Thonny window.  The top part is where
you type Python code.  The bottom part is called the Python *Shell* window.  The
shell is where you will see the result of your code, which we call the *output*.

Normally, you'll be able to write code in code window, save it to a file, and
then run it to see the output in the Python Shell window.  Additionally, you can
type single lines of code into the Python Shell window if you want to experiment
a little bit before writing your finished program code.  We'll encourage you to
do both types of activities throughout this book.

Notice that the code window in Thonny displays something like "untitled."  Let's
go ahead and start saving any code we type into a file.  That way, after we
close Thonny we can always come back and work on our code some more later.  In
Thonny, choose **File --> Save As...** from the top menu.  A dialog window will
appear.  Choose an appropriate folder location for your new file (and all other
Python code files you'll create in this book), and then let's name this first
file `hello.py`.  Python files always end with the suffix `.py`.  This helps us
remember what type of file it is.  We call these files Python source code files,
or simply Python source files.  Click the **Save** button and return to the
Thonny code window.

Okay, let's learn some Python!


The `print` statement
---------------------

You are now ready to start typing *statements* into the file `hello.py`.  These
statements will make up a program.  Each statement gives the computer an
instruction.  A statement might tell the computer to put something on the screen
(which is called "printing"), it might prompt the user to type something, or it
might tell the computer to remember some information so that we can recall it
and use it later in the program, etc.

Any time from here forward that you click the play button in Thonny, Thonny will
hand over your statements to the Python interpreter.  The Python interpreter will
take each statement, one at a time, and change the statement into machine code
that the computer can understand (again, 1's and 0's... beep beep boop boop).
If any of your statements put words or numbers on the screen, those will show
up in the Python Shell window.

Let's try to write a program that makes some text show up in the Shell
window.  Again, this is called "printing" text to the screen.

So, let's type the following into your new **hello.py** file::

   print("Hello")

Run your program by pressing the play button.

What do you see?  You should see in your Python Shell window the word ``Hello``
on a separate line.  If you don't, ask your friendly neighborhood programmer for
help.

Cool.  Why does this work, and can we break it and learn something in the
process?

(A word of warning: in this book we will frequently learn concepts more
deeply by trying to mess up the code, that is, "break" the code and then
learn how to fix it.  If we don't make mistakes and learn
how to fix them, we won't know how to respond when we encounter different
types of errors.  It's been said that if you're afraid of failure, you'll
never succeed.  This is especially true in computer programming.)

The ``print`` statement allows us to put words and numbers on the
screen in the Python Shell window.  You type ``print`` and then in
parentheses, you put what you want to appear on-screen.  What are those double
quotes doing there?  Let's get rid of them and then run the program to see what
happens.  Replace your code with this::

   print(Hello)

Notice the double quotes are gone.  Run your program using play button again.

Oh no!  We've broken our computer!  Well, not really.  The word ``print`` means
something to Python--it's part of the language--but ``Hello`` doesn't mean
anything to Python.  The double quotes tell Python to actually print the text
characters "Hello" onto the screen.

Let's delete the one line we have in our file, and replace it with the following
three lines.

.. code-block:: python

   print("Hello")
   print("How are you?")
   print("Goodbye.")

Run your code again and you will see these three lines appear on-screen in
order.

What if you change the order of the statements?

.. code-block:: python

   print("Hello")
   print("Goodbye.")
   print("How are you?")

Notice we switched the order of the last two statements.  Python will only
execute your statements in the order you give them.  Consider the following
analogy: programs are to computers as recipes are to cooking.  The order of the
statements matter just like the order of steps in a recipe matter.  Imagine what
would happen if you jumbled up the steps in a recipe for making a cake.  You
might end up with a very strange-looking cake! 

The `input` statement
---------------------

Okay, let's change our code again.  Delete the three lines you have so far and then add one new one::

   print("Hello, Steve.")

This code attempts to make our program more personalized, but it makes the bold
(and unfortunate) assumption that the user's name will always be Steve.  What if
we wanted to ask users what their names are, and then greet the user by name?
How many statements would we need?  We would need two: 1.) to ask for the name,
and 2.) to greet the person using that name.  Here's a good first attempt.

.. code-block:: python

   print("What is your name? ")
   print("Hello, name.")

What do you see?  The code does ask for the user's name (that's good), but it
does not give the user the ability to type anything in (that's bad).

Let's introduce a new type of statement called ``input``.  All programs take
*input* from the user (possibly from the keyboard, a mouse, or something else)
and produce *output* (usually information is *printed* to the screen, but the
information could be placed elsewhere, too, like placed in a file or sent over
the Internet to a Web site or something).  The ``input`` statement will allow the
user to type something in.

Let's try this.  Change the first ``print`` statement to an ``input`` statement.

.. code-block:: python

   input("What is your name? ")
   print("Hello, name.")

Run this code.  What happens?

Cool!  The user (you) can now type in your name, and then the program waits until
you're done typing and you've hit the Enter or Return key on your keyboard.
But, then the program fails to address the person (you, again) using that name.
Bummer.

We need to make the program *remember* the person's name in the first statement so
that it can be used later in the second statement.

Let's change the first statement from this

.. code-block:: python

   input("What is your name? ")

to this

.. code-block:: python

   firstname = input("What is your name? ")

See the difference?  We've put ``firstname =`` in front of the input command.

Here's how it works. The ``input`` command retrieves the text the user types in
from the keyboard.  Then, we must *store* it somewhere so that we can use it
later in the program.  The word ``firstname`` is a **variable**.  Variables are kind
of like Post-It notes for the computer to help it remember different numbers and
text that become important to us.  *Variables* store **values**.

We can choose to name the variable almost whatever we want.  There are some
rules for what you can and can't name a variable.  Variables must start with a
letter or an underscore (_).  After that, they can include any letters,
numbers, or underscores, but no other symbols.  Variables cannot have spaces in
their name.  Let me repeat that again.  *Variables cannot have spaces in their
name*.  Thus, you can name a variable ``cool_memes`` but not ``cool memes``.
You also cannot name a variable one of the **reserved words** in
Python.  Reserved words are like  "commands" that mean something to Python,
like ``if`` or ``while``.  Always name the variable so that you'll remember
its name.  Instead of

.. code-block:: python

   firstname = input("What is your name? ")

We could have typed

.. code-block:: python

   dudename = input("What is your name? ")

or

.. code-block:: python

   awesomename = input("What is your name? ")

or even

.. code-block:: python

   awesome_name = input("What is your name? ")

but for now we'll stick with

.. code-block:: python

   firstname = input("What is your name? ")

Now, what about the second line?  It's still

.. code-block:: python

   print("Hello, name.")

We need to use the variable ``firstname`` to retrieve the value we stored.  Change
the print line to this

.. code-block:: python

   print("Hello,", firstname)

Run it.  Voila!  It works!

Now, instead of putting one thing inside the parentheses after the word ``print``,
we're listing two things, separated by a comma.  The first is a text value
``"Hello,"``.  The second is the variable that stores the name.  Print will print
both of those things, separated by a space.

What if we don't want spaces between the things we print?  We'll get to that
later, too.

Awesome.  Try some stuff.  Try to break your code.  Don't worry, you can always
change your code back.  Our code so far should look like the code in
Listing :numref:`%s <input1>`.

.. _input1:
.. code-block:: python
   :linenos:
   :caption: Reading and printing a name

   firstname = input("What is your name? ")
   print("Hello,", firstname)

Sometimes in this book we will show code snippets like we had been previously.
Other times, if we want to show a series of statements in context, we will use a
listing like we did above.  The listings will typically have line numbers before
each code statement so that we can draw attention to individual statements if we
wish.

Let's learn by breaking things.  In Listing :numref:`%s <input1>`, change the second
line by removing ``first`` from the variable name.  The code should now read

.. code-block:: python

   firstname = input("What is your name? ")
   print("Hello,", name)

Run this code.  What happens?  Why do you think this happens?

Once you create a variable named ``firstname``, it's called ``firstname`` for the
duration of the program.  In the first line, we're creating ``firstname``.  Then,
in the second line, we try to use a variable called ``name``, but there is no such
variable called ``name``.  Python rightly vomits red text all over the screen.

It would be like if your name was Jorge and I tried to get your attention by
yelling "Hey, Betty!"  You wouldn't know I was trying to get your attention.

Let's try one more thing.  Let's go back to our original code in
Listing :numref:`%s <input1>`.

Change the variable ``firstname`` in the second line by capitalizing the first letter.  In other words, change ``firstname`` to ``Firstname``, like this.


.. code-block:: python

   firstname = input("What is your name? ")
   print("Hello,", Firstname)

Now run it and see what happens.  You get an error, don't you?  ``Firstname`` and
``firstname`` are different variables.  Python is a *case-sensitive* language.  So
we don't make mistakes with mixing uppercase and lowercase in Python, we
typically stick to lowercase.

Remember how I said variable names can't have spaces in them?  Let's try it
anyway.  What if we changed ``firstname`` to ``first_name``?

.. code-block:: python

   first_name = input("What is your name? ")
   print("Hello,", first_name)

Run it and watch our program crash and burn.  It's a good things computers don't
have feelings because ours would probably be feeling rather abused right now.

Notice that each time we tried to "break" our code, we ended up with different
program errors. Pay attention to what the errors say.  At first, the errors look
like "tech-ese" but eventually you'll learn to make sense of them, and it will
help you in correcting your programs.

One cool thing about programming is it will give you a keener eye, and you'll
notice details and mistakes a lot better in other avenues of your life.  Well,
we'll hope so anyway.

.. _asgn_stmts:

Assignment statements
---------------------

As it turns out, we now know a lot about Python even though we likely don't
realize it.  We know three kinds of statements.

1.	``print`` statements
2.	``input`` statements
3.	*assignment* statements

An assignment statement is a statement that creates or updates the value of a
variable.  Our input statement in the previous example was also an assignment
statement because it created the variable named ``firstname``.

Let's look at more examples of assignment statements.  Consider the following.
I live on an acreage, and we have a barn where cats tend to gather.  We didn't
have to buy any cats; they just show up.  It's good they are around because they
eat mice and we don't like mice.

Suppose we want to remember the number of cats we have in our barn at any given
time, and suppose we currently have six cats.  To store this information in a
Python variable, we would type the following.

.. code-block:: python

   cats = 6

To experiment with what's happening here, let's add two more lines so that your
code now looks like Listing :numref:`%s <cats>`.

.. _cats:
.. code-block:: python
   :linenos:
   :caption: Cats example

   cats = 6
   print(cats)
   print("cats")

Can you guess what will happen when you run this code?  It is very important to
be able to read code line by line to figure out in your mind what will happen.
Later on, when you're programming and something doesn't work right, you'll need
to look at your code line by line to make sure that it makes logical sense.
This code will print

.. code-block:: none

   6
   cats

There are two print statements in Listing :numref:`%s <cats>`.  Since there are two
print statements, we can reasonably assume there will be two lines that appear
on the screen.  The first statement makes a new variable named ``cats`` and
assigns it the value ``6``.  The second statement prints the value stored in cats.
The third statement prints the text string "cats" since there are double quotes
around it.

If we hadn't created the variable ``cats`` before printing the value of ``cats``,
Python would have puked red text again saying that it doesn't know what ``cats``
is.

It's worth noting that the first statement line ``cats = 6`` does not print
anything to the screen.  It's just an assignment statement.  It's only job is to
*define* a new variable.  It does not print anything.  Only ``print`` statements
actually print anything on the Python Shell window.

Okay, let's try to break things again!  What happens if we switch the order of
``cats`` and the number ``6`` in the first line of Listing :numref:`%s <cats>`, like
this::

   6 = cats

Run it.  Kablooey!  Now we've learned a rule about assignment statements.  Think
of the = sign as being more like a left arrow (|larr|).  When we write
``cats = 6``, we can think of it like ``cats`` |larr| ``6`` in that the
value ``6`` is being assigned to the new variable ``cats``.  You cannot change the
order of ``cats`` and ``6``.

See?  Computers are picky.

So, on the left-hand side of the equals sign in an assignment statement, we can
give the name of a variable.  If the variable doesn't exist, it is created brand
new.  If the variable does already exist, the value of the variable is updated
(or, overwritten – update and overwrite are synonymous).  So what can we put on
the right-hand side of the equals?

On the right-hand side, we can put any *expression* that produces a value.  Here
are some examples of expressions.

* ``6``
* ``2 + 4``
* ``6 * 1``
* ``8 - 2``
* ``12 / 2``
* ``12 – (3 * 2)``

The asterisk (``*``) or star does multiplication.  The forward slash (``/``)
performs division.  The double forward slash (``//``) performs whole number
division by dropping the remainder.  For example, ``5 // 2`` produces the value
``2``.  The percent (``%``) gives us the remainder.  This operation is also known as
the modulus, or simply mod.  For example, ``5 % 2`` produces the value ``1``.

The  ``+``, ``-``, ``*``, ``/``, ``//``, and ``%`` are known as *operators*.  Operators take
two expressions (which produce values) and produces a new value.  Parentheses
can be used to group expressions much like we do in mathematics.  Also as in
mathematics, operators have precedence.  Expressions produce a value by
evaluating the expression left-to-right while performing parenthetical
expressions first, then multiplication and division, and finally addition and
subtraction.

Just for the heck of it, we could re-write the assignment statement ``cats = 6``
as::

   cats = 12 - (3 * 2)

To recap, the left-hand side (abbreviated *LHS*) of an assignment statement is
the name of a variable.  The variable will either be created (that is, defined)
if it doesn't already exist or updated (that is, overwritten) depending on
whether the variable existed previously.  The right-hand side (abbreviated
*RHS*) is an expression that, when evaluated by Python, produces a value.

With all this in mind, let's try something.  What happens when you change our
code so that it looks like Listing :numref:`%s <cats_plus1>`.

.. _cats_plus1:
.. code-block:: python
   :linenos:
   :caption: Incrementing a value

   cats = 6
   cats = cats + 1
   print("You have", cats, "cats.")

Remember how assignment statements work.  They work in two steps.

1. We determine the value produced on the RHS.
2. That value is assigned to the variable on the LHS.

What is the value on the RHS of ``cats = cats + 1``?  When we reach this
statement, ``cats`` is ``6``.  Thus, ``cats + 1`` is the same as ``6 + 1``, which is
``7``.  Therefore, the assignment statement ``cats = cats + 1`` is essentially the
same as saying ``cats = 7``.

We can visualize how this assignment statement is *evaluated* in
Figure :numref:`%s <cats_eval>`.

.. _cats_eval:
.. figure:: images/ch1/cats_eval.png
   :scale: 100 %
   :alt: Evaluating an assignment statement

   Evaluating an assignment statement

Remember, the equals sign performs assignment of the value produced by the RHS
to the variable on the LHS.  Therefore, the equals sign is more like a left
arrow that the mathematical equals sign that normally says "the thing on the LHS
and the thing on the RHS have the same value."  The fact that you can type
``x = x + 1`` in Python looks yucky to mathematicians.  Poor, poor mathematicians.
We will try to avoid making fun of mathematicians in this book, but I make
no promises.

We will say more about the relationship between values, expressions, and
statements in the next section.

Values, types, expressions, and statements
------------------------------------------

Let's modify the code example from the previous section.  It is, after all,
silly because you start with a fixed number of cats when, in fact, we could
start with any number of cats.  Let's ask users for how many cats they have in
their barn.  Then, our program should calculate the number of cats they'll have
in the barn in a month's time.  For the sake of argument, let's arbitrarilysuppose
the number of cats will increase by 4.

A running program that solves this problem would look like this on the Python
Shell window.

.. code-block:: none

   How many cats do you have? 10
   In a month's time, you will have 14 cats!

The 10 at the end of the first line is typed in by the user, as an example. Can
you write this program?  Give it a try.  You know how to write code to get input
from the user.  You know how to produce output.  You know how to create
variables and perform calculations using expressions.  Try to write this
program.

(One attempt at a solution follows, but try to shield your eyes and don't look
at it right away.  You won't learn very well if you don't try and fail every now
and then.)

Listing :numref:`%s <cats_typeerror>` shows an attempt that you might have made.

.. _cats_typeerror:
.. code-block:: python
   :linenos:
   :caption: Type error

   cats = input("How many cats do you have? ")
   cats = cats + 4
   print("In a month's time, you will have", cats, "cats.")

This seems reasonable and logical, but it doesn't work!  Rather, you end up with an
error.  Let's take a very close look at the error.  It's very important to
understand how to read error messages.  If you know how, they often tell you
exactly what's wrong.

.. code-block:: none

   Traceback (most recent call last):
     File "/Users/shep/cs1/code/cats.py", line 2, in <module>
       cats = cats + 4
   TypeError: Can't convert 'int' object to str implicitly


The error states that the problem is on line 2 of your code.  That's helpful,
but keep in mind line 2 is only where the error was *detected*.  It's possible
that what caused the error occurred earlier in the code than line 2.

Note what the error message says: "Can't convert 'int' object to str
implicitly."  What does this mean?  In order to understand what it means, we
need to revisit some of the concepts we touched on in Section
:numref:`%s <asgn_stmts>`.

A *statement* can consist of one or more expressions.  An *expression* is a
piece of code that produces a *value*.  Every value has a *type*.  Consider the
following example::

   carrots = (7 + 3) * 2

This is one assignment statement whose right-hand side (RHS) consists of two
expressions.  The first expression is::

   7 + 3

``7`` and ``3`` are values known as *integers*, which is just a fancy word for
"whole number."  In Python, an integer is called an ``int``, for short.  ``7`` is a
value and its type is ``int``.  ``3`` is value and its type is ``int``.  Since
``7`` is an ``int`` and ``3`` is an ``int``, adding them together gives us the
value ``10``, which is also an ``int``.  Thus, the following table describes
what we know about this expression.

.. list-table:: Expression/value/type
   :widths: 50 25 25
   :header-rows: 1

   * - Expression
     - Value
     - Type
   * - ``7 + 3``
     - ``10``
     - ``int``

Remember, an expression is a piece of code that produces a value.  Every value
has a type.

Say it again: an expression produces a value, and every value has a type.

Say it again with me (yes, *again*, ... ugh): an expression produces a value, and every value has a type.

If you're not sure what the type of an expression is, you can find out by typing
the expression into the Python Shell.  If I entered ``7 + 3``, the Python Shell
would output ``10``.  If I entered ``type(7 + 3)``, the Python Shell would output
``"<class 'int'>"``.  Try out the type command to see what different expressions and
different values have as their type.  Try ``type(7)``, ``type(7.52)``, and
``type("Hello")``.

The next expression for us to consider in our current example is ``(7 + 3) * 2``.
We can see from this expression that expressions can consist of other
expressions.  We already know that ``7 + 3`` is an expression whose value is ``10``
and whose type is ``int``.  Thus, we can determine the following about this
expression.

.. list-table:: Expression/value/type
   :widths: 50 25 25
   :header-rows: 1

   * - Expression
     - Value
     - Type
   * - ``(7 + 3) * 2``
     - ``20``
     - ``int``

From this, we can determine that the variable ``carrots`` will have as its value
``20`` and its type will be ``int``.

There is another number type named ``float``.  Floats are used to represent
numbers that have a fractional part.  The value ``5.2`` is an example of a float.
Float values can be expressed in scientific notation as well.  The value ``3e2``
is equivalent to :math:`3 \times 10^2` which is 300, for example.  The value
after the ``e`` is the power of ten to which we multiply the first number.

Any time we type a specific value like ``5`` or ``5.25`` in a program, we call that
value a *literal*.  That is, ``5.25`` is a float literal because it is "literally"
the value ``5.25``.  It's important to have the word "literal" in your programmer
vocabulary.

Now let us consider a different example, shown in Listing :numref:`%s <firstlast>`.

.. _firstlast:
.. code-block:: python
   :linenos:
   :caption: String concatenation

   firstname = "Kanye"
   lastname = "West"
   fullname = firstname + " " + lastname

These three statements all involve text values.  Text values have a special type
called *string*.  In Python, a string is called a ``str`` for short.  If, in the
Python Shell, I were to enter ``type("Kanye")``, I would see the output ``<class
'str'>``.  If I entered the first statement ``firstname = "Kanye"`` and then
afterwards entered ``type(firstname)``, I would see the output ``<class 'str'>``.

There are four expressions in these three statements.  They are shown in the
following table.

.. list-table:: Expression/value/type for string concatenation
   :widths: 50 25 25
   :header-rows: 1

   * - Expression
     - Value
     - Type
   * - ``"Kanye"``
     - ``"Kanye"``
     - ``str``
   * - ``"West"``
     - ``"West"``
     - ``str``
   * - ``firstname + " "``
     - ``"Kanye "``
     - ``str``
   * - ``firstname + " " + lastname``
     - ``"Kanye West"``
     - ``str``

Some operators can work on strings, too.  When we use the plus (+) on two string
values, it "smashes" the two strings together to form a new string.  Here, we
are taking the first name and putting a space on the end of it.  Then, we are
appending the last name onto that new string that consists of the first name and
trailing space.  There is a geeky name for "smashing" two strings together to
make a new string, and that name is *concatenation*.  We would say that the plus (+)
*concatenates* two strings.

Remember, an expression is a piece of code that produces a value.  Every value
has a type.  Every variable has a value and a type.

When we write a string literal, we always put quotes around it. The quotes are
not part of the string value, however.  In other words, if I write ``"abc"``, I
know ``"abc"`` is a string literal, and I know the quotes are not a part of the
string's value.  Also, we can use either double quotes (``"``) or single quotes
(``'``) as long as they match one another.  That is, we can write ``"cheese"`` or
``'cheese'`` but not ``'cheese"``.

Types and values are tremendously important in Python, and this is illustrated
by our problematic code from earlier in this section.  Recall
Listing :numref:`%s <cats_typeerror>`, which is shown again below:

.. code-block:: python
   :linenos:

   cats = input("How many cats do you have? ")
   cats = cats + 4
   print("In a month's time, you will have", cats, "cats.")

.. role:: red

When we ran this code, we got an error on line 2 that told us
":red:`Can't convert 'int' object to str implicitly.`"  When line 2
tries to do the plus operation, it gets confused because ``4`` is an ``int`` and it
thinks that ``cats`` is a ``str`` rather than an ``int``. Think about it.  Can you
guess why?  Look back at line 2.  Look back at line 1.

The ``input`` command in line 1 retrieves characters entered from the keyboard.
These characters could be letters, symbols, and/or numbers.  Since the value
placed into ``cats`` by ``input`` could be any of these things, the type of the
value ``input`` gives us is ``str``.  Suppose the user typed a ``5`` at the prompt
"How many cats do you have?"  The initial value of the variable cats will be the
``str`` value ``"5"`` rather than the ``int`` value ``5``.

It doesn't make sense to Python to add a string and an integer.  After all, what
is reasonable to assume about the type and value of an expression like ``"Hello" +
32``?  In the above example, we need to convert ``cats`` from a string to an
integer so that we can treat ``cats`` as an integer.  Let us add a new line of
code after the ``input`` statement in Listing :numref:`%s <cats_cast>` at line 2.

.. _cats_cast:
.. code-block:: python
   :linenos:
   :emphasize-lines: 2
   :caption: Casting to a str

   cats = input("How many cats do you have? ")
   cats = int(cats)
   cats = cats + 4			
   print("In a month's time, you will have", cats, "cats.")

The ``int`` command converts the string value stored in ``cats`` to an integer, and
then it overwrites the value of ``cats`` to this new ``int`` value.  Converting a
value from one type to another is called *casting*.

When we write code, it is bound to have errors we need to correct.  Sometimes,
those errors make the program crash and we see an actual error message in
red text on the screen.  Other times, however, we don't get a
nice error message.  Instead, the program appears to behave erroneously.
Erroneous code is called a *bug*, and it is up to us to "debug" the program.

At some point in this book's sure-to-be-glorious future, we'll have a nice
detour in this box about the origin of the term "debug."  It's an amusing
historical tale.  For now, read this: http://www.wired.com/2013/12/googles-doodle-honors-grace-hopper-and-entomology/.

Let's practice detecting and fixing bugs.  We'll again use
Listing :numref:`%s <cats_typeerror>` as our starting point, only this time instead
of adding ``4`` to the number of cats, we will double the number of cats by
multiplying by ``2``.  After all, when it comes to feral barn cats, this is a more
accurate representation of what happens to cat populations.  Consider our new
Listing :numref:`%s <cats_mult>`.

.. _cats_mult:
.. code-block:: python
   :caption: Multiplying cats
   :linenos:
   :emphasize-lines: 2

   cats = input("How many cats do you have? ")
   cats = cats * 2		
   print("In a month's time, you will have", cats, "cats.")

Note that we forgot to cast ``cats`` to be an ``int``.  We might expect this
program to have a ``TypeError`` since it doesn't make sense to multiply a string
and an integer.  In fact, this is not what happens.  Type ``3`` for the number of
cats.  What happens?

``33`` cats?!  Good grief!  As it turns out, Python allows string values to be
repeated using the asterisk/star (``*``) operator.  Instead of performing ``3 * 2``,
the expression we've inadvertently performed is ``"3" * 2``, which is the same as
``"3" + "3"``, which is the same as ``"33"``.  If we properly cast ``cats`` to an
``int`` before multiplying, we get the proper result and we have "debugged" the
program.

It is important to understand what operators are available to us.
Tables :numref:`%s <arith_ops>` and :numref:`%s <str_ops>` provide more
comprehensive lists of these operators and their function.

.. _arith_ops:
.. list-table:: Arithmetic operators
   :widths: 15 85
   :header-rows: 1

   * - Operator
     - Usage
   * - ``+``
     - Addition
   * - ``-``
     - Subtraction
   * - ``*``
     - Multiplication
   * - ``/``
     - Division
   * - ``//``
     - Integer-only division; example: ``5 // 2`` gives us ``2`` rather than ``2.5``
   * - ``%``
     - Modulus or "mod", which returns the remainder from division; example: ``5 % 2`` gives us ``1`` since ``5`` divided by ``2`` is ``2`` remainder ``1``
   * - ``**``
     - Exponentiation, which returns the result of raising a number to a power; example: ``2 ** 3`` gives us ``8``


.. _str_ops:
.. list-table:: String operators
   :widths: 15 85
   :header-rows: 1

   * - Operator
     - Usage
   * - ``+``
     - Concatenation; example: ``"ab" + "cd"`` gives us ``"abcd"`` 
   * - ``*``
     - Repetition: example: ``"-" * 5`` gives us ``"-----"``
   * - ``%``
     - Formatting. The string format operator allows us to insert one string value into the middle of another string, which is known as the format string.  The format string can contain any number of format specifiers, which are placeholders for the values to be inserted.  See Table :numref:`%s <str_fmts>` for a list of format specifier examples.

        Example 1:
        Suppose we have a variable ``forks`` that contains the integer value ``5``. 
        ``"There are %d forks on the table." % forks``
        would produce the string ``"There are 5 forks on the table."``

        Example 2:
        Suppose we have two variables ``first`` and ``last`` that contain string
        values ``"Bob"`` and ``"Barker"```.  The expression
        ``"Hi, %s %s." % (first, last)`` would produce the string ``"Hi, Bob Barker."``.
        Note that if we have multiple values to be inserted into the format string,
        we enclose them in parentheses and separate the values with commas.

        Example 3:
        Suppose we have a variable ``ch`` that contains a single character ``'!'``
        ``"OMG\%c\%c\%c" \% (ch, ch, ch)`` would produce the string ``"OMG!!!"``.

.. _str_fmts:
.. list-table:: String format specifiers
   :widths: 20 80
   :header-rows: 1

   * - Specifier 
     - Description
   * - ``%d``
     - the value to be inserted is an integer
   * - ``%5d``
     - the value is aligned to the right across a 5-character column
   * - ``%-5d``
     - the value is aligned to the left across a 5-character column
   * - ``%f``
     - the value to be inserted is a float
   * - ``%10.2f``
     - the value to be inserted is a float aligned to the right across a 10-character column, and we should use two decimal places after the decimal point only
   * - ``%s``
     - the value to be inserted is a string
   * - ``%10s``
     - the value is aligned to the right across a 10-character column
   * - ``%-10s``
     - the value is aligned to the left across a 10-character column
   * - ``%c``
     - the value to be inserted is a single character

Calling functions
-----------------

In the `Assignment statements`_ section, we identified  the three types of statements
that we knew at that point.

1. ``print`` statements
2. ``input`` statements
3. *assignment* statements

We have since learned about other statements.  For example, we can use ``type`` to
determine the type of an expression or ``int`` to cast a ``str`` to an ``int``.  We
have also been using the word *command* to refer to words like ``print``, ``input``,
and ``type`` that seem to have important meaning to Python.  In fact, these
commands are actually called *functions*.  It's important to learn to speak like
a programmer when you are writing code, so we will call them *functions* from here
forward.

You'll note that in this book, we try to steer clear of technical terms until we
reach an appropriate time to introduce them.  This seems to be a better approach
than throwing every possible technical term at you right away and then expect
you to memorize them without any context whatsoever.

So, let's practice speaking like programmers.

.. list-table::
   :widths: 50 50
   :header-rows: 1
   
   * - Instead of...
     - Programmers would say...
   * - *use* a function
     - *call* a function
   * - function *produces* a value
     - function *returns* a value

Consider the following code.

::

   answer = input("Do you wish to continue (y/n)? ")

Programmers would say they are *calling* the input function, and the input
function will *return* a string value.

All functions return a value, even something like ``print``.  Just for fun
(wheee!), type the following into the Python Shell window.

::

   var = print("Hello.")

Now, type ``var`` in the Shell window and press ENTER.  Hmm, normally when we type
the name of a variable or we type an expression into the Python Shell window, it
tells us its value.  We get nothing.  Type the expression ``type(var)`` into the
Shell.  Aha!  The variable ``var`` has a special type called ``NoneType``.  Every
function call is an expression that returns some value, even if at least that
value belongs to ``NoneType``.

Okay, it makes sense to have ``int``, ``float``, and ``str`` because it's easy to
think of whole and fractional numbers and text values, but why does ``NoneType``
exist?  We're really not ready for the answer yet, but rest assured we'll cover
it eventually.  The short answer is that seasoned Python programmers can use
``NoneType`` to make their code really easy to read in some circumstances.  Stay
tuned.

We can now simplify the list of statements we know about to these.

1. function call statements
2. assignment statements

From now on, we will refer to things like ``print``, ``input``, and ``type`` as
functions rather than as commands.  Note that assignment statements can have
function calls in them, like

::

   name = input("What is your name? ")

This statement is an assignment statement, and the RHS is a function call.

The expressions that are placed between the parentheses after the function's
name are called *arguments*.  Some functions take no arguments, some functions
take one argument, and some other functions can take several arguments.
Arguments are separated with commas.  Arguments tell the function how to do its
job.  The code in Listing :numref:`%s <age_inc>` shows different examples of how to
call functions with differing numbers of arguments.

.. _age_inc:
.. code-block:: python
   :linenos:
   :caption: Calling functions with different numbers of arguments

   age = input("What is your age? ")
   age = int(age)
   age = age + 1
   print("In one year, you will be", age, "years old.")

Lines 1 and 2 demonstrate calling a function with one argument.  Line 4 has
three arguments.  The first is a string value, the second is a string variable,
and the third is another string value.

Because functions return values, we can call one function and immediately give
its return value to another function.  Look at lines 1 and 2 in
Listing~\ref{code:age_inc} again.  Since casting can be performed on any
expression, we could do both the ``input`` and the ``int`` cast on one line, like
this.

::

   age = int(input("What is your age? "))

The ``input`` function is called first, and the result returned by ``input`` is then given to ``int``, which casts the result from a string to an integer.  Students are often puzzled by what appears to be "double right parentheses" at the end of the above statement.  Note that the last right parenthesis matches the left parenthesis for ``int``, and the next to last right parenthesis matches the left parenthesis for ``input``.  This is shown visually in Figure :numref:`%s <match_parens>`.

.. _match_parens:
.. figure:: images/ch1/match_parens.png
   :scale: 100 %
   :alt: Use of arrows to showing matching parentheses

   Use of arrows to showing matching parentheses

If the user were to type ``18``, the code above would be executed and "transformed" through the steps shown in Figure :numref:`%s <stmt_exec>`.

.. _stmt_exec:
.. figure:: images/ch1/stmt_exec.png
   :scale: 100 %
   :alt: Statement execution

   Statement execution

Just for fun (again: whee!!), let's change line 4 of Listing :numref:`%s <age_inc>` and try out the string formatting operator (``%``).  Instead of this,

::

   print("In one year, you will be", age, "years old.")

We could do this:

::

   print("In one year, you will be %d years old." % age)

Here, the value of ``age`` gets inserted into the format string in place of the
``%d``.  There is no advantage to one way or the other, per se.  There will be
lots of ways to write code, though you should try to write code so that is
*readable*.  If you write code that is easy to read, it will be easier to
change.  Some programmers like the second way because it is easy to see the
format of what the output will be, and it can be easier to control where the
spaces go in the output.

There is another way to do string formatting in Python that is newer and is now
preferred as of Python 3.5.  We will introduce it later in the book.  However,
we show this method for string formatting since this is an introductory computer
science textbook, and this "style" of string formatting is one you'd encounter
in other programming languages (e.g., C, Java, etc.).

To review, we started with four lines of code.

::

   age = input("What is your age? ")
   age = int(age)
   age = age + 1
   print("In one year, you will be", age, "years old.")

Then, we "tweaked" the code so that, ultimately, it looked like this.

::

   age = int(input("What is your age? "))
   age = age + 1
   print("In one year, you will be %d years old." % age)

As you program, you will develop your own coding style.  You will want to decide
which of the two blocks of code (or a combination of them) looks the most
readable to you.

Handy functions
---------------

The purpose of this book is to teach novice programmers how to program.  The
purpose is not to have you learn every single thing about the Python programming
language.  To that point, this book is not intended to be a desk reference for
all things Python.  If you want to find information about a particular language
feature or a list of available functions, the best way to look is to use a Web
search (like Google) or go straight to the `Python
Documentation <https://docs.python.org/>`_ online.

That said, there are a number of handy functions that come "pre-packaged" with
Python and ready for you to use.  We will list a few of them here in the
subsections that follow, since we're highly confident you'll use them very soon.
We'll introduce more functions throughout the book.  Eventually, you'll learn
how to create your own functions.  That will happen in Chapter :numref:`%s <ch_funcs>`.
Creating your own functions is pretty cool. 

Some functions can be called just by stating their name.  For example, we can
use the ``print`` function just by typing something like ``print("Hello")``.  Other
functions are part of what we call *libraries*.  One example is the ``math``
library.  In order to use functions in the ``math`` library, we must do two
things.  First, we must type the statement ``import math``.  Then, ``math`` library
functions start with the prefix ``math.`` (read aloud as "math-dot"), so when we
call them we must use the ``math.`` prefix.  Here is an example of using a
function from a library (see Listing :numref:`%s <import_math>`).

.. _import_math:
.. code-block:: python
   :linenos:
   :emphasize-lines: 1,4
   :caption: Importing and calling a function from a library

   import math

   number = float(input("Enter a number: "))
   squared = math.pow(number, 2)
   print("Your number squared is %f." % squared)

In Listing :numref:`%s <import_math>` line 4, the function named ``pow`` is contained
in the library ``math``.  Because of this, we must type ``math.pow`` for the
function name in order to call it.  As you may be able to guess, ``pow`` raises a
number to a power.  In this case, we are raising whatever number the user types
to the second power, which is called squaring the number.

Math functions
--------------

Suppose ``i`` is an ``int`` variable and ``f`` and ``g`` are both ``float`` variables.
Said another way, ``type(i)`` is ``int``, ``type(f)`` is ``float``, and ``type(g)`` is ``float``.
Some of the functions in Table :numref:`%s <math_funcs>` belong to the ``math``
library and some do not.  If we want to use these functions, we need to first type the
statement ``import math``.  If we don't write ``import math``, we will get a
``NameError`` that tells us ``math`` is not defined.

Here is how to read Table :numref:`%s <math_funcs>`.  If the function is shown as ``i =
math.ceil(f)``, that means the function expects us to pass it a ``float`` (hence
the ``f`` in parentheses), and the function will return an ``int`` (hence the ``i`` on
the LHS of the equals).

There are many more functions found in ``math``, but these are the ones you're
most likely to use in the near future.  Again, consult the online `Python
Documentation <https://docs.python.org/>`_) if there's something specific you're
looking for that's not mentioned in this subsection.

.. _math_funcs:
.. list-table:: Math functions
   :widths: 30 70
   :header-rows: 1

   * - Function
     - Returns
   * - ``i = round(f)``
     - The integer resulting from rounding ``f``.

       Examples:

       ``round(5.2)`` is ``5``

       ``round(5.78)`` is ``6``

       ``round(6)`` is ``6``

       ``round(-1.2)`` is ``-1``

   * - ``i = math.ceil(f)``
     - The smallest integer :math:`\geq` ``f``.

       Examples:

       ``math.ceil(5.2)`` is ``6``

       ``math.ceil(5.78)`` is ``6``

       ``math.ceil(6)`` is ``6``

       ``math.ceil(-1.2)`` is ``-1``

   * - ``i = math.floor(f)``
     - The largest integer :math:`\leq` ``f``.

       Examples:

       ``math.floor(5.2)`` is ``5``

       ``math.floor(5.78)`` is ``5``

       ``math.floor(6)`` is ``6``

       ``math.floor(-1.2)`` is ``-2``

   * - ``g = abs(f)``
     - The absolute value of ``f``.

       Examples:

       ``abs(23.2)`` is ``23.2``

       ``abs(-23.2)`` is ``23.2``

Let's consider an example of how we might use some of these functions.

Suppose we want to buy a whole bunch of fidget spinners in bulk and then re-sell
them to make a profit.  (Yes, this is a terrible idea. The fidget spinner fad is
long since dead, but stick with me here.  It's just an example.)
If we buy them in bulk, then we can get a good deal
because they'll be cheaper per fidget spinner.  Let's have users enter the
number of fidget spinners they want and the number of spinners that come in a
case.  The program should tell them how many cases they'll need to buy to get at
least that many number of fidget spinners.

To write this program, we'll need to ask for two inputs: the number of spinners
and the number of spinners per case.  Then, we'll need to calculate the number
of cases needed and then output that number.  Listing :numref:`%s <spinner_cases>`
shows how to do this in Python code.

.. _spinner_cases:
.. code-block:: python
   :linenos:
   :caption: Fidget spinner example

   spinners = int(input("How many spinners do you need? "))
   spins_per_case = int(input("How many spinners come in a case? "))

   cases = math.ceil(spinners / spins_per_case)

   print("You need to order %d cases." % cases)

In line 4 of Listing :numref:`%s <spinner_cases>`, we divide ``spinners`` by
``spins_per_case`` to get how many cases we'll need.  But this gives us a
fractional number potentially.  For example, if we wanted ``18`` spinners and ``12``
come in a case, that would be ``1.5`` cases, but we can't order one case and then
another half of a case.  We actually need ``2`` cases.  This is where ``math.ceil``
comes in.  We take the "fractional" number of cases needed and find the
*ceiling* of it.  This makes ``cases`` an integer that is greater than or equal to
the number of fractional cases.

Random functions
----------------

The library ``random`` has functions that help us generate random numbers.  This
is useful for writing programs that involve random chance, for example, rolling
dice, flipping coins, etc.  There are several useful functions in ``random``, but
the two we'll focus on right now are ``random`` and ``randint``.

Suppose ``i``, ``start``, and ``end`` are ``int`` variables and ``f`` is a
``float`` variable.

.. _rand_funcs:
.. list-table:: Random functions
   :widths: 50 50
   :header-rows: 1

   * - Function
     - Returns
   * - ``f = random.random()``
     - A float value between ``0`` and ``1`` inclusive.
   * - ``i = random.randint(start, end)``
     - An integer value between ``start`` and ``end`` inclusive.

Listing :numref:`%s <rand_ex>` shows an example of how one might use a ``random``
library function.

.. _rand_ex:
.. code-block:: python
   :linenos:
   :caption: Random function example

   import random

   print("Rolling a six-sided die......")
   die_roll = random.randint(1, 6)
   print("You rolled a %d." % die_roll)

The code in Listing :numref:`%s <rand_ex>` may produce a different die roll every
time you run the program.

Comments
--------

As we go forward in learning Python, our programs will get longer and more
intricate.  It may be helpful to annotate our code with short comments to remind
us what our code does.  Listing :numref:`%s <age_w_comments>` shows a (somewhat
silly) example.

.. _age_w_comments:
.. code-block:: python
   :linenos:
   :caption: Age code with comments

   # Get the user's age.
   age = input("What is your age? ")
   age = int(age)

   # Tell the user his or her age one year from now.
   age = age + 1
   print("In one year, you will be", age, "years old.")

The lines that start with a ``#`` symbol are called comments.  Any line that
starts with ``#`` will be ignored by the Python interpreter.  Those lines are only
for the programmer to read.  Again, this is a somewhat silly example because our
code is relatively simple and probably does not require comments.

Programmers will also use comments at the beginning of a code file to document
what the program does.  Here is an example (see Listing :numref:`%s <comment_hdr>`).

.. _comment_hdr:
.. code-block:: python
   :caption: A header comment at the top of a code file

   # Program: tictactoe.py
   # Programmer: Susan McConnell
   # Description:
   #   This program allows users to play Tic Tac Toe against
   #   a computer opponent.  Users choose the row and column
   #   to place their ‘X' or ‘O' on the game grid in each turn.

Because placing a ``#`` symbol at the start of a line hides the code from Python,
another use of comments is to hide old code.  Sometimes, we want to save old
code without deleting it.  This can occur when we're not sure if new code we're
trying out is going to work, and so we may not want to lose our old code in case
we need to go back to it later.  Listing~\ref{code:comment_out} demonstrates
this concept.

.. _comment_out:
.. code-block:: python
   :linenos:
   :emphasize-lines: 1,2
   :caption: Commenting out code

   #age = input("What is your age? ")
   #age = int(age)

   age = int(input("What is your age? "))

Python will not execute lines 1 and 2 because they are "commented out."
It will, however, execute line 4.

Another use for comments is to help us program.  As human beings, we do not
naturally think in code.  Even experienced programmers struggle to think purely
in terms of programming language code.  One good way to program is to write
comments first in plain English to help us organize our logic and thoughts, and
then we write Python code beneath the comments.  For example, we might start
with::

   # Get the user's age.

   # Print how old they'll be in a year.

Then, we can fill in the details.

::

   # Get the user's age.
   age = input("What is your age? ")
   age = int(age)

   # Print how old they'll be in a year.
   age = age + 1
   print("In one year, you will be", age, "years old.")

Comments end up being very important later on in the book when we start creating
our own functions (yes, we get to make our own functions eventually).  Practice
writing comments when you write your own code.

Exercises
---------

1. Write a program that creates as its output a face on the screen by arranging different symbols, letters, and/or numbers.  Here is an example.

.. code-block:: none

   \\///
    0 0
     v
    ---

2. What is the output of the following program?

::

   a = 1
   b = a * 2
   c = 2 * b + 1
   print(a)
   print(b)
   print(c)

3. What is the output of the following program?

::

   a = 2
   b = a * 2
   c = b ** a
   a = c % 2
   print(a)
   print(b)
   print(c)

4. What is the output of the following program?

::

   a = 5
   b = a // 2
   c = a / 2
   a = a % 2
   print(a)
   print(b)
   print(c)

5. What is the output of the following program if the user enters a ``2`` at the first prompt and a ``3`` at the second prompt?

::

   x = input("Enter a whole number: ")
   y = input("Enter another whole number: ")
   z = x + y
   print(z)

(Be careful.  Try to type this program into the Python Shell and see what you get.)

6. Write a program that asks users for two whole numbers.  It should then add them and print the result.  Here is an example of what the output should look like.

.. code-block:: none

   Enter a whole number: 2
   Enter another whole number: 3

   2 + 3 = 5

7. What is the output of the following program?

::

   s = "John"
   t = "Smith"
   r = s + t
   print(r)

8. What is the output of the following program?

::

   s = "John"
   t = "Smith"
   print("%s, %s" % (t, s))

9. What is the output of the following program?

::

   s = "John"
   t = "Smith"
   r = "%s, %s" % (t, s)
   print(r)

10. What is the output of the following program?

::

   s = "John"
   t = "Smith"
   r = "%s, %s"
   print(r % (t, s))

11. What is the output of the following program?  Write down the answer exactly how it would appear on-screen.

::

   print("%s %s" % ("Item", "Price"))
   print("%s %f" % ("Soda", 1.75))
   print("%s %f" % ("Pizza", 2.00))
   print("%s %f" % ("Hot Dog", 1.50))
   print("%s %f" % ("Crab Legs", 30.99))

12. What is the output of the following program?  Write down the answer exactly how it would appear on-screen.

::

   print("%-10s %10s" % ("Item", "Price"))
   print("%-10s %10.2f" % ("Soda", 1.75))
   print("%-10s %10.2f" % ("Pizza", 2.00))
   print("%-10s %10.2f" % ("Hot Dog", 1.50))   
   print("%-10s %10.2f" % ("Crab Legs", 30.99))

13. What is the output of the following program?  Write down the answer exactly how it would appear on-screen.

::

   print("%-10s %10s" % ("Item", "Price"))
   fmt = "%-10s %10.2f"
   print(fmt % ("Soda", 1.75))
   print(fmt % ("Pizza", 2.00))
   print(fmt % ("Hot Dog", 1.50))
   print(fmt % ("Crab Legs", 30.99))

14. What is the output of the following program?  Write down the answer exactly how it would appear on-screen.

::

   print("%-10s %10s" % ("Item", "Price"))
   fmt = "%-10s %10.2f"
   print(fmt % ("Soda", 1.75))
   print(fmt % ("Pizza", 2.00))
   #print(fmt % ("Hot Dog", 1.50))
   #print(fmt % ("Crab Legs", 30.99))
   print(fmt % ("Pretzel", 1.50))
   print(fmt % ("Nachos", 2.25))

15. Write a program that asks the user for a single character.  The program should then greet them in block letters "HI" consisting solely of that character.  Here is an example of a running program.

.. code-block:: none

   Enter a character: @

   @@  @@  @@@@@
   @@@@@@    @
   @@  @@  @@@@@
   

Here is another example of a running program if the user were to type a different character.

.. code-block:: none

   Enter a character: +
    
   ++  ++  +++++
   ++++++    +
   ++  ++  +++++

