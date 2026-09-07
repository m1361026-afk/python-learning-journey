# Store daily step counts for analysis
daily_steps = [2999, 8200, 9500, 2800, 3000, 7999, 8000]

# Analyze the data only when at least one day is recorded
if len(daily_steps) > 0:
    print(f"Number of days: {len(daily_steps)}")
    # Calculate the total once so it can be reused for the average
    total_steps = 0
    for steps in daily_steps:
        total_steps = total_steps + steps
    print(f"Total steps: {total_steps}")
    average_steps = total_steps / len(daily_steps)
    print(f"Average steps: {average_steps:.2f}")
    print(f"Highest steps: {max(daily_steps)}")
    print(f"Lowest steps: {min(daily_steps)}")

    goal_met_count = 0
    day_number = 0
    low_steps_days = []
    below_average_count = 0
    consecutive_days = 0
    longest_consecutive_days = 0
    # Track goal performance, low-activity days, and consecutive goal streaks
    for steps in daily_steps:
        day_number += 1
        if steps >= 8000:
            goal_met_count += 1
            consecutive_days += 1
        else:
            consecutive_days = 0
        if consecutive_days > longest_consecutive_days:
            longest_consecutive_days = consecutive_days
        if steps < 3000:
            low_steps_days.append(day_number)
        if steps < average_steps:
            below_average_count += 1

    print(f"Goal met count: {goal_met_count}")
    print(f"Low-activity days: {low_steps_days}")
    print(f"Days below average: {below_average_count}")
    print(f"Longest consecutive goal streak: {longest_consecutive_days}")

else:
    print("目前沒有步數資料。")
