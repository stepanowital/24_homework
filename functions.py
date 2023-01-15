from typing import Iterable


def filter_query(value: str, data: Iterable[str]):
	return filter(lambda x: value in x, data)
