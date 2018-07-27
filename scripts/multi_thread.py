import pybreaker
import redis
import threading
from datetime import datetime
from random import randint
from time import sleep


def fragile_function():
    if randint(0, 1) == 1:
        print('OK', end='')
    else:
        print('NG / ', end='')
        raise Exception('This is a sample Exception')


def main(thread_id, breaker):
    while True:
        print('#{} {} '.format(thread_id,
                              datetime.now().strftime('%Y-%m-%d %H:%M:%S')), end='')

        try:
            breaker.call(fragile_function)
        except Exception as e:
            print('{} {}'.format(type(e), e), end='')
        finally:
            print('')
            sleep(2)


redis_conn = redis.StrictRedis(host='redis', port=6379)
breaker = pybreaker.CircuitBreaker(
    fail_max=2,
    reset_timeout=5,
    state_storage=pybreaker.CircuitRedisStorage(pybreaker.STATE_CLOSED, redis_conn))
breaker.close()

thread1 = threading.Thread(target=main, args=(1, breaker))
thread2 = threading.Thread(target=main, args=(2, breaker))

thread1.start()
sleep(1)
thread2.start()
