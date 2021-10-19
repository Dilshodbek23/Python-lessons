# Python Standard Libraries

# Starting from today, 10 dates have been released on the console with a difference of 2 weeks.

import datetime as dt


now = dt.datetime.now()
twoWeeks = dt.timedelta(weeks=2)
for i in range(10):
    print(now)
    now = now + twoWeeks

