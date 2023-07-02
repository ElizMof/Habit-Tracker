from habit import Habit, Periodicity

#List of all Habits
def get_all_habits(habits):
    return habits

#Get Habits by period
def get_habits_by_periodicity(habits, periodicity):
    return list(filter(lambda habit: habit.periodicity == periodicity, habits))

#See the Streak
def get_longest_streak(habits):
    longest_streak = 0
    for habit in habits:
        streak = habit.get_streak()
        if streak > longest_streak:
            longest_streak = streak
    return longest_streak


def get_longest_streak_for_habit(habit):
    return habit.get_streak()
