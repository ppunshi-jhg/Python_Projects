import pandas as pd
from tabulate import tabulate
from datetime import datetime
from HabitTracker import track_habit, Habit

def main():
    habits: list[Habit] = [
        track_habit("No Smoking", datetime(2025, 8, 1), cost_per_day = 50.0, minutes_per_day = 10),
        track_habit('Alcohol', datetime(2023, 6, 5, 22), cost_per_day=5, minutes_per_day=15),
        track_habit('Sugar drinks', datetime(2023, 5, 16, 19), cost_per_day=1, minutes_per_day=3),
        track_habit('Being lazy', datetime(2021, 1, 1, 10), cost_per_day=1, minutes_per_day=3),
    ]
    
    df = pd.DataFrame(habits)
    print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
    
if __name__ == '__main__':
    main()