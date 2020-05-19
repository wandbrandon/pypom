import click
import time
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Pypom")

def countdown(t):
    t = t*60
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

@click.command()
@click.option('-wt', default=25, help='Work time in minutes')
@click.option('-rt', default=5, help='Rest time in minutes')
@click.option('-ert', default=15, help='Extended rest time in minutes')
@click.option('-c', default=1, help='Cycle amount (one cycle is an hour and 40 mins)')
def timer(wt, rt, ert, c):    
    while c:
        Notify.Notification.new(countdown(wt)).show() 
        countdown(rt)
        Notify.Notification.new("Work Time!").show()
        countdown(wt)
        Notify.Notification.new("Break Time!").show()
        countdown(rt)
        Notify.Notification.new("Work Time!").show()
        countdown(wt)
        Notify.Notification.new("Big Break Time!").show()
        countdown(ert)

if __name__ == '__main__':
    timer()
    Notify.uninit()
