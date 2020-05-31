import click
import time
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Pypom")

#countdown code
def countdown(t):
    t = t*60
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

#click methodology
@click.command()
@click.option('-wt', default=25, help='Work time in minutes')
@click.option('-rt', default=5, help='Rest time in minutes')
@click.option('-lrt', default=15, help='Long rest time in minutes')
@click.option('-c', default=1, help='Cycle amount')
def timer(wt, rt, lrt, c):
    noti = Notify.Notification.new("")
    noti.set_urgency(0)
    ctemp = c
    while c:
        noti.update("cycle start")
        noti.show()
        countdown(wt)
        noti.update("break")
        noti.show()
        countdown(rt)
        noti.update("work")
        noti.show()
        countdown(wt)
        noti.update("break")
        noti.show()
        countdown(rt)
        noti.update("work")
        noti.show()
        countdown(wt)
        noti.update("long break")
        noti.show()
        countdown(lrt)
        noti.update("cycle complete")
        noti.show()
        c = c - 1
    sum = wt+wt+wt+rt+rt+lrt
    total = sum*ctemp
    print("finished {0} cycles for a total of {1} minutes".format(ctemp,total))

if __name__ == '__main__':
    timer()
    Notify.uninit()
