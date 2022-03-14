Bio-3027 / Bio-8027: Python Course
==================================

This repository contains all the material that will be shared during the course, including lectures and sample code.  
The files are organised per day, and will be updated as the course goes on.

(rough) schedule
================
_week 1_  
**Day 1**: Introduction, Simple Python, strings, numbers  
**Day 2**: Data types (dictionaries, booleans, lists), Program logic, Loops & Control flow (for, while, if/else)  
**Day 3**: Functions, Sets, Tuples, Code structure, Practice with loops and data types learned so far  
**Day 4**: File handling, file parsing, practice day with functions   
**Day 5**: Advanced functions, modules, more practice  

_week 2_  
**Day 1**: Object-oriented programming, basics of data science: Jupyter, Pandas, Scipy  
**Day 2**: Plotting: Matplotlib, Seaborn  
**Day 3**: Biology: BLAST, Biopython  
**Day 4**: Coding Practice, pathlib and argparse, start to work on assignments 
**Day 5**: Best practices, Good code, Work on assignments 

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
         
  * [day3](day3)
      * [list of exercises](week1/day3/exercise_outline_wk1_day3.pdf)
      * [control flow, functions, coding practices lecture](week1/day3/day_3.pdf): only covered functions and scope in this lecture
         * recap of day 2, practice lists, dictionaries, and list comprehension [-->](week1/day3/recap.py)
         * introduction to defining and structuring a function with a [mean calculator](week1/day3/mean_calculator.py)
         * more practice with functions and loops, [calculate factorial script](week1/day3/calculate_factorial.py), [string inversion script](week1/day3/invert_string.py)
         * introduction to tuples, which are ordered immutable collections of things [-->](week1/day3/tuple_operations.py)
         * introduction to sets, unordered (unindexed) mutable collections of things [-->](week1/day3/set_operations.py)

  * [day4](day4): only new material was intro to file IO, main focus of day 4 is on [Rosalind exercises](https://rosalind.info/problems/locations/)
      * [list of exercises](week1/day4/exercise_outline_wk1_day4.pdf)
      * introduction to file input / output [-->](week1/day4/basic_file_io.py)
      * recap of common problems encountered with formulating conditional statements in if/else [-->](week1/day4/conditional_issues.py)
      * Rosalind exercises [count nucleotides](week1/day4/count_nucleotides.py), [gc content](week1/day4/gc_content_rosalind_exercise.py)
      * Main focus of the day is on the GC content exercise, if you can do this independently (fasta parser and gc functions) you are set for the rest of the course

  * [day5](day5)
      * [list of exercises](week1/day5/exercise_outline_wk1_day5.pdf)
      * [lecture on advanced functions and modules](week1/day5/day_5_classes_modules.odp): we didn't cover classes today
      * iteration over lists via enumerate function [enumerate example](week1/day5/enumerate_example.py)
      * practice with advanced functions and anonymous functions [-->](week1/day5/more_functions.py)
      * practice with lambda functions [-->](week1/day5/play_with_lambda.py)
      * making your own module [-->](week1/day5/testmodule.py)
      * using the module you made [-->](week1/day5/explore_modules.py)
      * Rosalind exercise to translate rna to protein, parse your file!! don't cheat [-->](week1/day5/translate_rna_to_protein.py)

4. [week2](week2)
  * [day1](day1)
     * [classes lecture](week1/day5/day_5_classes_modules.odp)
         * practice with making a [student class](week2/day1/Student.py), and a [sequence class](week2/day1/Sequence.py)
     * [jupyter lecture](week2/day1/1_Jupyter.odp)
         * practice using pandas on jupyter [-->](week2/day1/intro_jupy_pandas.ipynb)
     * [pandas lecture](week2/day1/2_Pandas.odp)
     * [numpy / scipy lecture](week2/day1/3_NumPy_SciPy.odp): not yet covered in class
   
  * [day2](day2)
     * [sequence analysis lecture](week2/day2/Sequence_analysis.pdf): background of sequence alignment, scoring matrices, and what BLAST does
     * [numpy / scipy lecture](week2/day2/3_NumPy_SciPy.odp): go through and practice numpy / scipy on your own
     * more practice with pandas in jupyter notebook [-->](week2/day2/plottting_practice.ipynb)
     * [plotting lecture](week2/day2/3_Plotting.odp): main packages for plotting are matplotlib, seaborn in python
     * use the [python graph gallery](https://python-graph-gallery.com/) whenever you want to make your own plots, because there are plenty of examples there already and they are well documented
     * practice plotting skills with a jupyter notebook [-->](week2/day2/presentation_plotting.ipynb)
 
  * [day3](day3)
     * [biopython mini lecture](week2/day2/0_BioPython.odp)
     * practice with Seq and SeqIO from biopython module [-->](week2/day3/sequence_practice_biopython.py)
     * practice with blasting using NCBIWWW [-->](week2/day3/blast_on_jupy.ipynb)
     
  * [day4](day4)
     * practice with paths and the pathlib module [-->](week2/day4/useful_modules.py)
     * how to write a command-line runable program, practice with argparse [-->](week2/day4/simple_cmdline_program.py)
 
  * [day5](day5)
     * practice with code verification of input type [-->](week2/day5/verify_input.py)
