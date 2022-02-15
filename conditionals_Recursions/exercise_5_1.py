""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 5, Exercise 5-1
by Allen Downey
    Code written by Mustafa Ali.
"""


import time

if __name__ == '__main__':
    seconds = time.time()
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    l_hours = round(hours - int(days) * 24)   # Local hours.
    l_minutes = int(minutes - int(hours) * 60)  # Local minutes.
    l_seconds = int(seconds - int(minutes) * 60)    # Local seconds.
    print('It has been ' + str(int(days))+' days, ' + 
           str(l_hours) +' hours, ' + str(l_minutes)
           + ' minutes and ' + str(l_seconds) + ' seconds since the epoch')
