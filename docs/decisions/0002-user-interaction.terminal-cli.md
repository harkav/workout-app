# userinterface: terminal cli

## Main view/options

`python -m workout-app`

`python -m workout-app --help`

Should display the options for the CLI:

```text
Workout App

Commands:
add - add a workout
edit - edit a workout
remove - remove a workout
list - list workouts
report - generate a report from workout data

Flags:
--file <filepath> - which file to use for storing/reading data. Defaults to ./workout-app.data
```

## Add Workout

### Category subcommand

`python -m workout-app add --exercise-type=<exercise-type> --repetitions=<no repetitions> --weight=<weight in kgs> [--date=<yyyy-MM-dd>]`

Add a strength exercise based on type.

```text
--exercise-type=<exercise-type>
    What kind of exercise that has been done.
    Exercise-types:
    deadlift
    squat
    bench

--repetitions=<no repetitions>
    an integer representing the number of "lifts"

--weight=<weight in kgs>
    Decimal number of kilograms lifted

--date=<yyyy-MM-dd>
    optional - defaults to "today" if not provided
    yyyy is year, MM is the month, dd is the day

Output:
Added workout with id:
2

```

## Edit Workout

`python -m workout-app edit <id> <at least one flag>`

```text
Edit Workout
python -m workout-app edit <id> <at least one flag>

Args
<id>: integer

Flags:
--exercise-type=<exercise-type>
    What kind of exercise that has been done.
    Exercise-types:
    deadlift
    squat
    bench

--repetitions=<no repetitions>
    an integer representing the number of "lifts"

--weight=<weight in kgs>
    Decimal number of kilograms lifted

--date=<yyyy-MM-dd>
    optional - defaults to "today" if not provided
    yyyy is year, MM is the month, dd is the day
```

## List workouts

```text
List workouts
Show all workouts

Usage:
python -m workout-app list

| id | date       | type     | reps | weight |
-----------------------------------------------
|  1 | 2023-01-01 | deadlift |   10 |    120 |


```

## Delete workout

```text
Delete a workout

Usage:
python -m workout-app delete <id>

Args:
<id>: integer
```

## Workout reports

```text
Print reports 

Usage:
python -m workout-app report <report-type>

Args:
<report-type>: Type of report.
    1RM - just outputs the 1RM
```

### Workout reports - 1RM

```text
Print reports - 1RM

Usage:
python -m workout-app report 1RM <exercise-type>

Args:
<exercise-type>:
    deadlift
    squat
