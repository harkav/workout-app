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

    def menu(self): 
        pass 
    #should display the menu and prompt the user and run methods depending on the choice 
    # add workout... 
    # edit workout... 
    # and so on... 

journal = Journal() 

journal.add_workout_session("2022.12.24")
journal.print_workout_sessions()


#problem, does not write time stamp, does not write id 
# need to create a loop in the add_workout_session-function. 