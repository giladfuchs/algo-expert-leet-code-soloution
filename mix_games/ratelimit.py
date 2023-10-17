import time


# Throttler: limits the rate at which a function can be called, ensuring that it's called at most N times within a specified time interval
# Rate limiter: limits the number of requests or operations a user can perform within a certain time frame. It's often used in API rate limiting or controlling access to resources.

class BaseThrottler:
    def __init__(self, max_calls, interval):
        self.max_calls = max_calls
        self.interval = interval
        self.calls = []

    def can_call(self):
        current_time = time.time()
        # Remove old calls that are outside the time interval
        self.calls = [call for call in self.calls if current_time - call < self.interval]
        # Check if the number of calls within the interval is less than the limit
        return len(self.calls) < self.max_calls


class RateLimiter:
    throttler: BaseThrottler

    def __init__(self, max_calls, interval):
        self.max_calls = max_calls
        self.interval = interval
        self.users = {}

    def call(self, user: str):
        if not self.users.get(user):
            self.users[user] = BaseThrottler(self.max_calls, self.interval)
        return self.users[user].can_call()
