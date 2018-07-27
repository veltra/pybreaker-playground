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
2018-07-27 01:51:17 OK
2018-07-27 01:51:18 OK
2018-07-27 01:51:19 NG / <class 'Exception'> This is a sample Exception
2018-07-27 01:51:20 NG / <class 'pybreaker.CircuitBreakerError'> Failures threshold reached, circuit breaker opened
2018-07-27 01:51:21 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
2018-07-27 01:51:22 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
2018-07-27 01:51:23 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
2018-07-27 01:51:24 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
2018-07-27 01:51:25 NG / <class 'pybreaker.CircuitBreakerError'> Trial call failed, circuit breaker opened
2018-07-27 01:51:26 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
2018-07-27 01:51:27 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
2018-07-27 01:51:28 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
2018-07-27 01:51:29 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
2018-07-27 01:51:30 OK
2018-07-27 01:51:31 OK
```

### Multi Thread Script
```
$ docker-compose run --rm playground python scripts/multi_thread.py
#1 2018-07-27 01:57:33 OK
#2 2018-07-27 01:57:34 OK
#1 2018-07-27 01:57:35 NG / <class 'Exception'> This is a sample Exception
#2 2018-07-27 01:57:36 NG / <class 'pybreaker.CircuitBreakerError'> Failures threshold reached, circuit breaker opened
#1 2018-07-27 01:57:37 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#2 2018-07-27 01:57:38 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#1 2018-07-27 01:57:39 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#2 2018-07-27 01:57:40 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#1 2018-07-27 01:57:41 NG / <class 'pybreaker.CircuitBreakerError'> Trial call failed, circuit breaker opened
#2 2018-07-27 01:57:42 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#1 2018-07-27 01:57:43 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#2 2018-07-27 01:57:44 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#1 2018-07-27 01:57:45 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#2 2018-07-27 01:57:46 OK
#1 2018-07-27 01:57:47 OK
#2 2018-07-27 01:57:48 OK
#1 2018-07-27 01:57:49 OK
#2 2018-07-27 01:57:50 OK
#1 2018-07-27 01:57:51 NG / <class 'Exception'> This is a sample Exception
#2 2018-07-27 01:57:52 NG / <class 'pybreaker.CircuitBreakerError'> Failures threshold reached, circuit breaker opened
#1 2018-07-27 01:57:53 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#2 2018-07-27 01:57:54 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#1 2018-07-27 01:57:55 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#2 2018-07-27 01:57:56 <class 'pybreaker.CircuitBreakerError'> Timeout not elapsed yet, circuit breaker still open
#1 2018-07-27 01:57:57 OK
#2 2018-07-27 01:57:58 OK
```
