# pybreaker-playground
Playground for using PyBreaker https://github.com/danielfm/pybreaker

## Requirements
- [Docker Compose](https://docs.docker.com/compose/)

## How to play
```
# Clone this repository
$ git clone git@github.com:veltra/pybreaker-playground.git
$ cd pybreaker-playground

# Build images
$ docker-compose build

# Run a single thread script (Send Ctrl+C to stop)
$ docker-compose run --rm playground python scripts/single_thread.py

# Start a Redis server
$ docker-compose up -d redis

# Run a multi thread script (Send Ctrl+C to stop)
$ docker-compose run --rm playground python scripts/multi_thread.py

# Stop the Redis server
$ docker-compose down
```

## Sample Output

### Single Thread Script
```
$ docker-compose run --rm playground python scripts/single_thread.py
2018-07-27 08:05:12 / OK
2018-07-27 08:05:13 / NG / <class 'Exception'> This is a sample Exception
2018-07-27 08:05:14 / OK
2018-07-27 08:05:15 / OK
2018-07-27 08:05:16 / NG / <class 'Exception'> This is a sample Exception
2018-07-27 08:05:17 / NG / <class 'pybreaker.CircuitBreakerError'> Failures threshold reached, circuit breaker opened
2018-07-27 08:05:18 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
2018-07-27 08:05:19 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
2018-07-27 08:05:20 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
2018-07-27 08:05:21 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
2018-07-27 08:05:22 / NG / <class 'pybreaker.CircuitBreakerError'> Trial call failed, circuit breaker opened
2018-07-27 08:05:23 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
2018-07-27 08:05:24 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
2018-07-27 08:05:25 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
2018-07-27 08:05:26 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
2018-07-27 08:05:27 / OK
2018-07-27 08:05:28 / OK
```

### Multi Thread Script
```
$ docker-compose run --rm playground python scripts/multi_thread.py
#1 2018-07-27 08:06:40 / OK
#2 2018-07-27 08:06:41 / OK
#1 2018-07-27 08:06:42 / NG / <class 'Exception'> This is a sample Exception
#2 2018-07-27 08:06:43 / NG / <class 'pybreaker.CircuitBreakerError'> Failures threshold reached, circuit breaker opened
#1 2018-07-27 08:06:44 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#2 2018-07-27 08:06:45 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#1 2018-07-27 08:06:46 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#2 2018-07-27 08:06:47 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#1 2018-07-27 08:06:48 / NG / <class 'pybreaker.CircuitBreakerError'> Trial call failed, circuit breaker opened
#2 2018-07-27 08:06:49 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#1 2018-07-27 08:06:50 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#2 2018-07-27 08:06:51 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#1 2018-07-27 08:06:52 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#2 2018-07-27 08:06:53 / NG / <class 'pybreaker.CircuitBreakerError'> Trial call failed, circuit breaker opened
#1 2018-07-27 08:06:54 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#2 2018-07-27 08:06:55 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#1 2018-07-27 08:06:56 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#2 2018-07-27 08:06:57 / <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#1 2018-07-27 08:06:58 / OK
#2 2018-07-27 08:06:59 / OK
```
