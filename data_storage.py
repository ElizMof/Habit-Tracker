import json
from habit import Habit, Periodicity
from datetime import datetime
import uuid

# Take Habit as input and convert it into dictionary
def habit_to_dict(habit):
    return {
        "id": str(habit.id), #Convert ID into a string
        "task": habit.task,
        "periodicity": habit.periodicity.value,
        "start_date": habit.start_date.isoformat(),
        "completions": [completion.isoformat() for completion in habit.completions],
    }

#Take Dictionary of habit and convert into a Habit object
def dict_to_habit(habit_dict):
    habit = Habit(
        habit_dict["task"],
        Periodicity(habit_dict["periodicity"]),
        datetime.fromisoformat(habit_dict["start_date"]),
    )
    habit.id = uuid.UUID(habit_dict["id"])
    habit.completions = [
        datetime.fromisoformat(completion) for completion in habit_dict["completions"]
    ]
    return habit

#Save File in JSON format
def save_habits_to_file(habits, file_path="habits.json"):
    habit_dicts = [habit_to_dict(habit) for habit in habits]
    with open(file_path, "w") as f:
        json.dump(habit_dicts, f, indent=4)

#Read Habit data from file
def load_habits_from_file(file_path="habits.json"):
    with open(file_path, "r") as f:
        habit_dicts = json.load(f)
    habits = [dict_to_habit(habit_dict) for habit_dict in habit_dicts]
    return habits
