from dateutil import parser
from zoneinfo import ZoneInfo

class Event:
    event = {}
    date = None

    def month(self):
        '''Returns this Event's month as the locale’s full name.'''
        return self.date.strftime("%B")

    def __init__(self, event_obj):
        self.event = event_obj
        self.date = parser.parse(event_obj["startdatestring"]).astimezone(ZoneInfo("localtime"))
    def __str__(self):
        return self.date.strftime("%A %B %d") + " - " + self.event["item"] + ": " + str(self.event["myqty"]) + " volunteer(s) needed"
    def __lt__(self, other):
        return self.date < other.date
