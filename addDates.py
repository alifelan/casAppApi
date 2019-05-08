from datetime import datetime, timedelta
from casApp.models import Date

"""Add dates to database."""
Date.objects.all().delete()
days = [0, 1, 2, 3, 4, 5]
x = datetime(1, 1, 1, 7)
for day in days:
    for i in range(8):
        time = (x + timedelta(hours=1, minutes=30) * i).time()
        Date(day=day, time=time).save()
    Date(day=day, time=datetime(1, 1, 1, 18).time()).save()
    Date(day=day, time=datetime(1, 1, 1, 19, 30).time()).save()
