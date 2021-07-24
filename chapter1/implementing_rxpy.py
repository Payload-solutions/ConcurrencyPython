#!/usr/bin/python3


"""On such example would be an event that only triggers if the temperature
fpr a specific part of the data center gets to warm. When this event is
triggered, we could then automatically react and increase the flow of any
cooling system to that particular area, and thus bring the temperature back 
down again"""

# from rx import Observable, Observer
from rx.core import observable, observer

# Here w define our custom observer which 
# contains an on_next method, an on_error method
# and an on_completed method

class TemperatureObserver(observer):
    # Every time we receive a temperature reading
    # this methid is called

    def on_next(self, x):
        print("Temperature is: %s degress centigrade"%x)
        if x > 6:
            print("Warning: temperature is exceeding recommended limit")
        if x == 9:
            print("Datacenter is shutting down. Temperature is too high")

    # if we create to receive an errer message
    # we would handle it here
    def on_error(self, e):
        print("Error: %s"%e)


    # This is calles when the stream is finished

    def on_completed(self):
        print("All temps Read")

# Publish some fake temperature readings
xs = observable.from_iterable(range(10))

# suscribe t these temperature readings
d = xs.subscribe(TemperatureObserver())
