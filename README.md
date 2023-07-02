# Habit-Tracker
## OBJECT ORIENTED AND FUNCTIONAL PROGRAMMING WITH PYTHON -  Habit Tracker

This application is a backend for a habit tracking application that includes a custom command line interface to use the basic functionalities.

It was written for the IU University's course "DLBDSOOFPP01" - Object-Oriented and Functional programming with Python.

This application was built with Python 3.10 and is automatically tested against the versions 3.7, 3.8, 3.9, 3.10 and 3.11 on a git push.

## Table of Contents

- [Test](#test)
- [What is it?](#what-is-it)
- [A habit's properties](#a-habits-properties)
- [Core Functionalities](#core-functionalities)
- [Data Storage](#data-storage)
- [Installation](#installation)


## Test

### What is it?

A habit tracker application is in general like a todo list whose tasks are coupled to specific dates and repeat in a set periodicity.
This application can be used to keep track of those and provide you with analytics about how you kept up with those for the set periodicity.
If a habit is successful completed at-least 2 times in a row, a so-called streak begins, which lasts until a habit is marked as failed.

### A habit's properties

A habit consists of:

- A name (maximal length: 20 Letters)
- A description (maximal length: 30 Letters)
- A periodicity/the time range of a task (daily or weekly)
- An optional default time value (a number from 0 to 1440)

## Core Functionalities

### Creating a habit

A habit can be created by giving it a name and assigning a short description, a periodicity that can currently be daily or weekly, and a default time value that can be used to skip entering a time value on each update.

### Updating a habit

A habit can be updated for the current periodicity via the update function either on the day/week it was created or the day/week after, which is called the due date. Once the due date is over, the habit will be automatically marked as failed for the missed date/s.

### Analysing habits

For analyses of the stored habits, there are currently 5 options available:

- Show all habits and their data
- Show all habits and their data which share the same periodicity (daily or weekly)
- Show which of all habits currently has the longest running streak
- Show the highest streak for a specific habit
- Show how much time you already invested into a habit

### Removing a habit

A function to remove habits is also available and can be used by choosing the corresponding menu-point and inserting the habit name.

### Altering a habit's details

Used to change the details of a habit such as the name, description, default time value or to change the details of an existing task record such as the completion status or time value.

## Data Storage

This application stores the habits and its events locally in a sqlite database as a file.
A sample database is provided and can be used to get an overview of the application and test out all functionalities.

## Installation

1. Ensure that you have Python installed - Check the version within your 
2. Download all the code files (`main.py`, `habit.py`, `analytics.py`, `data_storage.py`) and save them in a folder on your computer
3. Create a Virtual Environment
   Go to the folder where you have save the python files and initiate Command prompt by typing "cmd" at the end of the file path name
   In the Command Prompt type python -m venv nameyouwanttocallenvironment, eg python -m venv venv
   After that has run, type venv\Scripts\activate
   The code files do not have external dependencies, so you don't need to install any additional packages.

4. Run the `main.py` script by executing the following command in the terminal or command prompt: python main.py

The Habit Tracker Application will launch, and you can interact with it through the command-line interface (CLI).

To exit the Habit tracker App, choose option 0 on the menu
5. To run the test file python -m tests.py
