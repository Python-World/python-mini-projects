import time


def countdown(t):
    while int(t):
        if t > 10:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        else:  # less than 10 seconds
            secs, ms = divmod(t * 100, 100)
            timer = '{:02d}:{:02d}:{:02d}'.format(0, int(secs), int(ms))
            print(timer, end="\r")
            time.sleep(0.01)
            t -= 0.01

    print('Timer completed!')


t = input('Enter the time in seconds: ')

countdown(int(t))
