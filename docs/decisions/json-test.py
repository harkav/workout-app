
import json

class Loeft: 

    def __init__(self,id, exercise_type, repetions, weight_in_kgs): 
        self._id = id
        self._exercise = exercise_type 
        self._repetitions = repetions 
        self._weight_in_kgs = weight_in_kgs 

    
    def __str__(self): 
        return self._exercise + " " + str(self._repetitions) + " " + str(self._weight_in_kgs)

    def get_id(self): 
        return self._id

    def get_exercise(self): 
        return self._exercise

    def get_repetitions(self): 
        return self._repetitions

    def get_weight_in_kgs(self): 
        return self._weight_in_kgs



loeft = Loeft(1, "markloeft", 3, 120)

print(loeft)

ordbok = {}
ordbok["oevelse"] = loeft.get_exercise()
ordbok["repetisjoner"] = loeft.get_repetitions()
ordbok["vekt"] = loeft.get_weight_in_kgs()



json_loeft = json.dumps(ordbok)
print(json_loeft)
print(type(json_loeft))

with open("data.json", "w") as f:
    json.dump(json_loeft, f, indent=2)