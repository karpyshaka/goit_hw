from datetime import datetime, date, timedelta

def get_days_from_today(goal_date):
    
    try: 
        formatted_date = datetime.strptime(goal_date, "%Y-%m-%d").date()
        today_date = date.today()
        diff_date = today_date - formatted_date
        print(int(diff_date.days))
        return int(diff_date.days)
    except ValueError:
        print("Wrong format. Enter YY-MM-DD")
        return None

   
get_days_from_today("2026-08-21")