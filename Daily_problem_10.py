from time import sleep

def sample():
    print("hi")


def sheduler(f, delay):
    delay_in_s = delay / 1000
    sleep(delay_in_s)
    f()

sheduler(sample, 1000)