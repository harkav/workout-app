from exercise import Exercise 


class Workout_session: 

    def __init__(self, ID, timestamp):
        self._id = ID 
        self._timestamp = timestamp
        self._exercises = []

    def create_exercise(self, name, reps, weight_in_kgs): 
        exercise = Exercise(name, reps, weight_in_kgs)
        self._exercises.append(exercise)

    def print_exercises(self): 
        for exercise in self._exercises: 
            print(exercise)