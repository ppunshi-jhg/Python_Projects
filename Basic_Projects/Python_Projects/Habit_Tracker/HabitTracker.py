from dataclasses import dataclass
from datetime import datetime
import math

@dataclass
class Habit:
    name: str
    time_since: str  #since we started this habit
    remaining_days: str
    total_minutes_saved: int
    money_saved: str
    
def track_habit(name: str, start_date: datetime, cost_per_day: float, minutes_per_day: float,
                goal_days: int = 60, hourly_wage: float = 30.0) -> Habit:
    # 1. Calculate days since start
    elapsed_sec = max(0.0, (datetime.now() - start_date).total_seconds())
    hours = round(elapsed_sec / 3600, 1)
    days = round(hours / 24, 2)
    
    # 2. Savings
    
    direct_money_saved = cost_per_day * days
    total_minutes_saved = int(round(minutes_per_day * days))
    time_value = (total_minutes_saved / 60) * hourly_wage
    total_money = direct_money_saved + time_value
    money_saved = f"${total_money:,.2f}"
    
    # 3 Progress to Goal
    
    days_to_go = max(0, math.ceil(goal_days - days))
    remaining_days = "Cleared" if days_to_go == 0 else f"{days_to_go} days to go"


    # 4 human time label
    
    time_since = f"{days} days" if hours > 72 else f"{hours} hours"
    
    return Habit(name = name, time_since= time_since, remaining_days= remaining_days, total_minutes_saved= total_minutes_saved, money_saved= money_saved)