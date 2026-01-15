import datetime

t_year, t_month, t_day = map(int, input().split())
n_year, n_month, n_day = map(int, input().split())

today = datetime.date(t_year, t_month, t_day)
dday = datetime.date(n_year, n_month, n_day)

gap = dday - today
limit_date = datetime.date(t_year + 1000, t_month, t_day)

if dday >= limit_date:
    print("gg")
else:
    print(f"D-{gap.days}")