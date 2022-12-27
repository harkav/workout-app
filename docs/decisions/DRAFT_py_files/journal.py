from workout import Workout_session 

class Journal: 

    def __init__(self): 
        self._workout_sessions = [] 
        self._ID = 1 

    def add_workout_session(self, timestamp): 
        workout_session = Workout_session(self._ID, timestamp)
        name = "deadlift"
        reps = 5
        weight_in_kgs = 120
        workout_session.create_exercise(name, reps, weight_in_kgs)
        self._workout_sessions.append(workout_session)
        self._ID += 1 

    # Not sure if this is a good start. Will get a coffee and think about it 