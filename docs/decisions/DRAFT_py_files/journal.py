from workout import Workout_session 

class Journal: 

    def __init__(self): 
        self._workout_sessions = [] 
        self._ID = 1 

    def add_workout_session(self, timestamp): 
        workout_session = Workout_session(self._ID, timestamp)
        name = input("enter name of exercise: ")
        reps = input("enter number of repetitions")
        weight_in_kgs = input("enter weight in kilograms: ")
        workout_session.create_exercise(name, reps, weight_in_kgs)
        self._workout_sessions.append(workout_session)
        self._ID += 1 

    # Not sure if this is a good start. Will get a coffee and think about it 

    def print_workout_sessions(self): 
        for workout_sessions in self._workout_sessions: 
            workout_sessions.print_exercises()

journal = Journal() 

journal.add_workout_session(22021224)
journal.print_workout_sessions()
