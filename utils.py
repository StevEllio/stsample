from enum import enum
import datetime

class DatesFromPeriod(enum):
    MTD = datetime.date.today(), datetime.date.today()
    
    def __init__(self,start_date,end_date)
        self.StartDate = start_date
        self.EndDate = end_date
        
        