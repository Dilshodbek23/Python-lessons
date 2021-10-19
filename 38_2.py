# Python Standard Libraries

# Bringed the remaining days before New Year and International Women's Day to the console.

import datetime as dt


now = dt.datetime.now()
new_year = dt.datetime(2022, 1, 1)
womens_day = dt.datetime(2022, 3, 8)
days_ny = new_year - now
days_wd = womens_day - now
print(f"Until the new year {days_ny.days} days.")
print(f"There are {days_wd.days} days left until International Women's Day.")
