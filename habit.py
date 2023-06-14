from datetime import datetime, timedelta
from enum import Enum


class Habit:
    next_id = 1

    def __init__(self, task, periodicity, start_date=None):
        self.id = Habit.next_id
        Habit.next_id += 1
        self.task = task
        self.periodicity = periodicity
        self.start_date = start_date or datetime.now()
        self.completions = []

    def __str__(self):
        periodicity_str = "DAILY" if self.periodicity == Periodicity.DAILY else "WEEKLY"
        return f"Habit: {self.task} | Periodicity: {periodicity_str}"

    def complete(self, completion_time=None):
        completion_time = completion_time or datetime.now()
        self.completions.append(completion_time)
        return completion_time

    def is_completed_within_period(self, period_start, period_end):
        for completion in self.completions:
            if period_start <= completion <= period_end:
                return True
        return False

    def get_streak(self):
        streak = 0
        current_streak = 0
        period_start = self.start_date
        period_end = self.get_period_end(period_start)
        while period_start < datetime.now():
            if self.is_completed_within_period(period_start, period_end):
                current_streak += 1
                streak = max(streak, current_streak)
            else:
                current_streak = 0
            period_start = period_end + timedelta(days=1)
            period_end = self.get_period_end(period_start)
        return streak

    def get_period_end(self, period_start):
        return period_start + timedelta(days=self.periodicity.value - 1)


class Periodicity(Enum):
    DAILY = 1
    WEEKLY = 7
