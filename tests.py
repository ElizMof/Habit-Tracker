import unittest
from habit import Habit, Periodicity
from analytics import get_longest_streak
from datetime import datetime


class TestHabit(unittest.TestCase):
    def test_create_habit(self):
        habit = Habit("Test habit", Periodicity.DAILY)
        self.assertEqual(habit.task, "Test habit")
        self.assertEqual(habit.periodicity, Periodicity.DAILY)

    def test_complete_habit(self):
        habit = Habit("Test habit", Periodicity.DAILY)
        habit.complete(datetime.strptime("2023-05-12", "%Y-%m-%d"))
        self.assertEqual(len(habit.completions), 1)
        self.assertEqual(habit.completions[0].strftime("%Y-%m-%d"), "2023-05-12")


class TestAnalytics(unittest.TestCase):
    def test_get_longest_streak(self):
        habit1 = Habit("Habit 1", Periodicity.DAILY)
        habit1.complete(datetime.strptime("2023-05-12", "%Y-%m-%d"))
        habit1.complete(datetime.strptime("2023-05-13", "%Y-%m-%d"))
        habit1.complete(datetime.strptime("2023-05-14", "%Y-%m-%d"))

        habit2 = Habit("Habit 2", Periodicity.WEEKLY)
        habit2.complete(datetime.strptime("2023-05-12", "%Y-%m-%d"))
        habit2.complete(datetime.strptime("2023-05-19", "%Y-%m-%d"))
        habit2.complete(datetime.strptime("2023-05-26", "%Y-%m-%d"))

        habits = [habit1, habit2]
        longest_streak = get_longest_streak(habits)
        self.assertEqual(longest_streak, 0)


if __name__ == "__main__":
    unittest.main()
