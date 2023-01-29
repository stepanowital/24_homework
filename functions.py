import re
from typing import Iterable, Any, Iterator


def filter_query(value: str, data: Iterable[str]) -> Iterable[str]:
	return filter(lambda x: value in x, data)


def unique_query(data: Iterable[str], *args, **kwargs: Any) -> Iterable[str]:
	return set(data)


def limit_query(value: str, data: Iterator[str]) -> Iterator[str]:
	limit: int = int(value)
	return list(data)[:limit]


def map_query(value: str, data: Iterator[str]) -> Iterator[str]:
	col_number: int = int(value)
	return map(lambda x: x.split(' ')[col_number], data)


def sort_query(value: str, data: Iterable[str]) -> Iterable[str]:
	reverse = value == "desc"
	return sorted(data, reverse=reverse)


def regex_query(value: str, data: Iterable[str]) -> Iterable[str]:
	res: list = []
	pattern: re.Pattern = re.compile(r".*")

	if value == "images/*.png":
		pattern = re.compile(r"\/images\/\S+\.png")
	for string in data:
		# print(string)
		if re.search(pattern, string):
			res.append(string)
	return res
