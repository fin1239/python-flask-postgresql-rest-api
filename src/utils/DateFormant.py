import datetime


class DateFormant():
    
    def convert_date(self,date):
        return datetime.datetime.striftime(date, '%d/%m/%Y')