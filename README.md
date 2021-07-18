# MultiThreadingFirstStudy

 - First study into Python Multithreading world with some examples 


 Multitasking refers to the ability of an operating system to perform different tasks at the same time.
 Advantages of Multithreading:

    -Enhanced performance by decreased development time
    -Simplified and streamlined program coding
    -Simultaneous and parallelized occurrence of tasks
    -Better use of CPU resource  

 
 There are two types of multitasking in an OS:
 
    -Process Based: Multiple threads running on the same OS simultaneously.
    -Thread Based: Single process consisting of separate tasks.

 
 Multithreading is very usefull for saving time and improving perfomance, but it cannot be applied everywhere.
 Multithreading in Python can be used when:
 
    -Multiple tasks need to achieved
    -Tasks do not have interdependency


Multithreading in Python can be achieved by importing the "threading" module.

    -"import threading"
    -"from threading import *"
    -"conda install -c conda-forge tbb"

 
 Threads can be created in three ways:
 
    -Without creating a class
    -By extending Thread class
    -Without extending Thread class

