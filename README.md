# OOP in Python
 the objective of this exercise is to train OOP Principles(Abstraction, Inheritance, 
 Polymorphism, Encapsulation) in Python.

In case1.py:
 - we have the first class  WriteFile, which only writes a line to the file and has the abstract method write.
 - the second class and third class inherit the WriteFile class.
 - The second class LogFile redefines the abstract method and writes a log stamp into a file using the inherited
   method write_line
 - The third class DelimFile, we have a definition of the __init__ method using super to pass some arguments to 
   the parent class and the definition of a variable for the DelimFile class. This class writes to a file 
   with a delimiter such as in a csv.

In case2.py:
 - we have the first abstract class Animal, which has some basic characteristics of an animal and a lot of the
   methods are defined for Encapsulation.
 - The other classes Dog and Cat, each one of these classes has their own characteristics but share some with the animal class