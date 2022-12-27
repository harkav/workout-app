from exercise import Exercise 


class Workout_session: 

    def __init__(self, ID, timestamp):
        self._id = ID 
        self._timestamp = timestamp

    def create_exercise(self, name, reps, weight_in_kgs): 
        exercise = Exercise(name, reps, weight_in_kgs)
        return exercise

    