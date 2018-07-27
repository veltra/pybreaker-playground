import pybreaker
from datetime import datetime
from random import randint
from time import sleep


def fragile_function():
    if randint(0, 1) == 1:
        print(' / OK', end='')
    else:
        print(' / NG', end='')
        raise Exception('This is a sample Exception')


def main(breaker):
    while True:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), end='')

        try:
            breaker.call(fragile_function)
        except Exception as e:
            print(' / {} {}'.format(type(e), e), end='')
        finally:
            print('')
            sleep(1)


breaker = pybreaker.CircuitBreaker(fail_max=2, reset_timeout=5)
main(breaker)
