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
- [Unit Tests](#unit-tests)
- [General Usage](#general-usage)
- [Interactive mode](#interactive-mode)
- [Detailed usage with Examples](#detailed-usage-with-examples)
- [Contributing](#contributing)

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

The only requirement is pytest for unittests, if you want to run tests, a requirements file is attached, so you can install the needed dependency by opening a shell and
