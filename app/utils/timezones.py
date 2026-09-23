from functools import lru_cache
from zoneinfo import available_timezones


@lru_cache(maxsize=1)
def _known_timezones() -> frozenset[str]:
    return frozenset(available_timezones())


def is_valid_timezone(name: str) -> bool:
    """True if `name` is an IANA time zone identifier, e.g. 'America/New_York'."""
    return name in _known_timezones()