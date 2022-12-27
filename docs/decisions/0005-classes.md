# Classes

## Context and Problem Statement

Which classes should I use?

## Considered Options

I mainly need to track two things:

1. Exercises
2. Workout sessions

A workout session consists of several preformed exercises. There should be an workout session
ID and a time stamp ofure some sort.
An exercise can have the following form exercise name (for instance deadlift), sets (for instance, 3)
repetitions (for instance, 5) and weight (for instance, 120 kgs).
Sets can varry in reps and weight, so it perhaps best to skip sets and rather add reps and weight for each set of the exercise.
That means, rather than entering "Deadlift, 3, 5, 120", enter "Deadlift 5 120" 3 times.

 In the future I could perhaps add a comment such as "easy" or "difficult" or "make sure that the technique is good", which could give an indication on whether the weight is too high or too low.

## Decision Outcome

Exercise, workout sessions
