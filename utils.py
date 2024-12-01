from enum import enum
import datetime

class DatesFromPeriod(enum):
    MTD = datetime.date.today().replace(day=1), datetime.date.today()
    YTD = datetime.date.today().replace(day=1,month=1), datetime.date.today()
    
    def __init__(self,start_date,end_date)
        self.StartDate = start_date
        self.EndDate = end_date
    
    @staticmethod
    def list():
        return list(map(datetime.date,DatesFromPeriod)
        