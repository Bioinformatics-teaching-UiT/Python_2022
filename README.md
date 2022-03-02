Bio-3027 / Bio-8027: Python Course
==================================

This repository contains all the material that will be shared during the course, including lectures and sample code.  
The files are organised per day, and will be updated as the course goes on.

(rough) schedule
================
_week 1_  
**Day 1**: Introduction, Simple Python, strings, numbers  
**Day 2**: Data types (dictionaries, booleans, lists), Program logic, Loops & Control flow (for, while, if/else)  
**Day 3**: Functions, Code structure, Good code practice   
**Day 4**: File handling   
**Day 5**: Object-oriented programming, Recap, Practice day   

_week 2_  
**Day 1**: Basics Science: Jupyter, Pandas, Scipy  
**Day 2**: Plotting: Matplotlib, Seaborn  
**Day 3**: Biology: BLAST, Biopython  
**Day 4**: Coding Practice!  
**Day 5**: Best practices, Good code, Wrap-up  

Repo Content
============

1. [general](general) 
    * course descriptions [MSc](general/python_course_msc.pdf) [PhD](general/python_course_phd.pdf)
    * [useful links](online_resource_links.pdf)
2. [week1](week1)
  * [day1](day1)
    * [list of exercises](week1/day1/exercise_outline_wk1_day1.pdf)
    * [introductory lecture 1](week1/day1/0_introduction.pdf): 
      * brief overview of the course & expectations
    * [introductory lecture 2](week1/day1/1_1_basics.pdf):
      * what is inside your computer and how this relates to programming
      * operating systems, intro to the terminal
      * 2 ways of writing Python (interactive shell vs IDE) [-->](week1/day1/script.py)
     * [variables lecture](week1/day1/1_2_variables.pdf):
        * use of variables as placeholders for objects
        * the Python string object and its behaviour [-->](week1/day1/string_operations.py)
        * basic numbers - integers and floats and the difference in between them [-->](week1/day1/number_operations.py)
        * avoid whitespace at beginning of lines [-->](week1/day1/bad_whitespace.py)
        * how to comment in the script with hashtags
        * general functions vs. type specific methods
        * basic script exercises [greeter](week1/day1/greeter.py), [pizza1](week1/day1/pizza_calculation.py), [pizza2](week1/day1/get_pizza_volume.py)
     
   * [day2](day2)
      * [list of exercises](week1/day2/exercise_outline_wk1_day2.pdf)
      * [data structures lecture](week1/day2/2_1_data_structures.pdf):
         * two exercises to recap day 1 [-->](week1/day2/day1_recap.py)
         * booleans don't behave as you would expect in Python, a lot more map to True [-->](week1/day2/boolean_operations.py)
         * if statements structured by indentation, meaning of if, elif, and else [-->](week1/day2/play_with_if_statements.py)
         * test if number is even or odd [exercise 1](week1/day2/test_odd_even.py), [exercise 2](week1/day2/is_number_even_or_odd.py)
         * mutable types 1: lists can contain anything, and are readily changeable, [basic list operations](week1/day2/list_operations.py)
         * mutable types 2: dictionaries are a key to value mapping sequence, even better than lists, [basic dictionary operations](week1/day2/dictionary_operations.py)
         * for loops: use when you know how many times or what you want to loop over [basic for loop usage](week1/day2/mini_for_loop.py), [numeric sequence printer](week1/day2/print_numeric_sequence.py), [turtle exercise 1](week1/day2/Turtle_play.py), [turtle exercise 2](week1/day2/mini_turtle.py), [turtle colored](week1/day2/coloured_turtle.py)
         * while loops: use when you want to stop only if condition is met or don't know how many times you want to loop, [basic while loop](week1/day2/small_while_counter.py)
         * list comprehension: one-liner for loops or other control flow statements, [basic usage](week1/day2/list_comp_practice.py)
4. [week2](week2) 

