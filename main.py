from infra.entities.amusement_park import *
from datetime import datetime, timedelta

ap = amusement_park(datetime.today().replace(hour=9, minute=0, second=0, microsecond=0))

print(ap.get_working_hours())


