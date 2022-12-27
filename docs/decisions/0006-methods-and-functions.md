# Methods and functions

## Context and Problem Statement

Which methods and functions should the classes have?

## Considered Options

This depends a bit on how the program should be structured, but as of now, it makes sense
to have different get and set methods for the data that I want to track. It might be a good idea
to make the workout session consist of one or more exercises and to give the workout session a method
for adding an exercise where the required information for the exercise is stored.

The workout class should also probably have a method for reading and writing to a file, prompting for user-input. Displaying the different workout sessions and calculating the 1RM and so on.

I'm beginning to think that it would perhaps make sense to add a third class to keep track on the workout sessions. I think I'll try to get going with an easy implementation of the app without reading/writing to a file and take it from there.

## Decision Outcome

I'm not sure about the class structure now. I'll do an easy version of the app and then revisit this file and the previous one.
