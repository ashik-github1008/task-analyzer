import datetime

def score_task(task):
    today = datetime.date.today()

    # Urgency (days until due)
    due_date = task["due_date"]
    if isinstance(due_date, str):
        due_date = datetime.date.fromisoformat(due_date)

    days_left = (due_date - today).days

    # past due penalty
    urgency_score = -50 if days_left < 0 else max(0, 30 - days_left)

    # importance weight
    importance_score = task.get("importance", 5) * 2

    # effort weight (less effort = higher priority)
    effort_score = 10 - task.get("estimated_hours", 1)

    # dependency penalty
    dependency_penalty = -10 * len(task.get("dependencies", []))

    total_score = urgency_score + importance_score + effort_score + dependency_penalty
    return total_score
