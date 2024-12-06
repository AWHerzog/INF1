import math

def work(hours, days, teen=False):
    max_vac = 25 if teen else 20
    percent = hours/42
    per_day = round(hours/days, 2)
    return {"per_day": per_day, "vacation_days": math.ceil(max_vac*percent)}

print(work(42, 5))