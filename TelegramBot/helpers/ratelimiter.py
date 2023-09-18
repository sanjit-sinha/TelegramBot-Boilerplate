from typing import Union
from pyrate_limiter import (
    BucketFullException,
    Duration,
    Limiter,
    MemoryListBucket,
    RequestRate,
)


class RateLimiter:
    """
    Implement rate limit logic using leaky bucket
    algorithm, via pyrate_limiter library.
    (https://pypi.org/project/pyrate-limiter/)
    """

    def __init__(self, seconds: int, minutes: int) -> None:

        # 2 requests per seconds (default).
        self.second_rate = RequestRate(seconds, Duration.SECOND)

        # 19 requests per minute (default).
        self.minute_rate = RequestRate(minutes, Duration.MINUTE)

        self.limiter = Limiter(
            self.second_rate,
            self.minute_rate,
            bucket_class=MemoryListBucket)

    async def acquire(self, update_id: Union[int, str]) -> bool:
        """
        Acquire rate limit per update_id and return True / False
        based on update_id ratelimit status.

        params:
            update_id (int | str): unique identifier for update.

        returns:
            bool: True if update_id is ratelimited else False.
        """

        try:
            self.limiter.try_acquire(update_id)
            return False
        except BucketFullException:
            return True
