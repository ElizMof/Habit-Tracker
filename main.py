import sys
from datetime import datetime, timedelta
from habit import Habit, Periodicity
from data_storage import save_habits_to_file, load_habits_from_file
from analytics import (
    get_all_habits,
    get_habits_by_periodicity,
    get_longest_streak,
    get_longest_streak_for_habit,
)

#Example Habits
def create_example_habits():
    habit1 = Habit("Brush your teeth", Periodicity.DAILY)
    habit2 = Habit("Go for a run", Periodicity.WEEKLY)
    habit3 = Habit("Drink 8 glasses of water", Periodicity.DAILY)
    habit4 = Habit("Read a book", Periodicity.WEEKLY)
    habit5 = Habit("Meditate", Periodicity.DAILY)
    return [habit1, habit2, habit3, habit4, habit5]

#Example of Tracking data
def generate_example_tracking_data(habits):
    today = datetime.now()
    for habit in habits:
        for i in range(28):
            completion_date = today - timedelta(days=i)
            if (habit.periodicity == Periodicity.DAILY and i % 1 == 0) or (
                habit.periodicity == Periodicity.WEEKLY and i % 7 == 0
            ):
                habit.complete(completion_date)

#Entry Point of program
def main():
    habits = create_example_habits()
    generate_example_tracking_data(habits)

    while True:
        print("\nHabit Tracker Menu")
        print("1. List all habits")
        print("2. List habits by periodicity")
        print("3. Get longest streak for all habits")
        print("4. Get longest streak for a specific habit")
        print("5. Create a new habit")
        print("6. Complete a habit task")
        print("7. Delete a habit")
        print("8. Save habits")
        print("9. Load habits")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            for habit in get_all_habits(habits):
                print(habit)
        elif choice == "2":
            periodicity = int(input("Enter periodicity (1 for daily, 7 for weekly): "))
            for habit in get_habits_by_periodicity(habits, Periodicity(periodicity)):
                print(habit)
        elif choice == "3":
            longest_streak = get_longest_streak(habits)
            print(f"Longest streak for all habits: {longest_streak}")
        elif choice == "4":
            habit_id = input("Enter habit ID: ")
            habit = next((habit for habit in habits if str(habit.id) == habit_id), None)
            if habit:
                longest_streak = get_longest_streak_for_habit(habit)
                print(f"Longest streak for the habit '{habit.task}': {longest_streak}")
            else:
                print("Habit not found.")
        elif choice == "5":
            task = input("Enter habit task: ")
            periodicity = int(input("Enter periodicity (1 for daily,7 for weekly): "))
            start_date = input("Enter start date (YYYY-MM-DD, leave empty for today): ")
            if start_date:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
            habit = Habit(task, Periodicity(periodicity), start_date)
            habits.append(habit)
            print(f"New habit '{habit.task}' created with ID {habit.id}.")
        elif choice == "6":
            habit_id = input("Enter habit ID: ")
            habit = next((habit for habit in habits if str(habit.id) == habit_id), None)
            if habit:
                completion_date = input(
                    "Enter completion date (YYYY-MM-DD, leave empty for now): "
                )
                if completion_date:
                    completion_date = datetime.strptime(completion_date, "%Y-%m-%d")
                else:
                    completion_date = datetime.now()
                habit.complete(completion_date)
                print(f"Habit '{habit.task}' marked as completed.")
            else:
                print("Habit not found.")
        elif choice == "7":
            habit_id = input("Enter habit ID: ")
            habit = next((habit for habit in habits if str(habit.id) == habit_id), None)
            if habit:
                habits.remove(habit)
                print(f"Habit '{habit.task}' deleted.")
            else:
                print("Habit not found.")
        elif choice == "8":
            file_path = input("Enter file path (leave empty for 'habits.json'): ")
            if not file_path:
                file_path = "habits.json"
            save_habits_to_file(habits, file_path)
            print(f"Habits saved to {file_path}.")
        elif choice == "9":
            file_path = input("Enter file path (leave empty for 'habits.json'): ")
            if not file_path:
                file_path = "habits.json"
            habits = load_habits_from_file(file_path)
            print(f"Habits loaded from {file_path}.")
        elif choice == "0":
            print("Exiting Habit Tracker.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
