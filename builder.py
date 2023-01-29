from pathlib import Path
from typing import Union, Iterator, Iterable

from functions import filter_query, unique_query, limit_query, map_query, sort_query, regex_query

CMD_TO_FUNCTIONS: dict = {
	'filter': filter_query,
	'unique': unique_query,
	'limit': limit_query,
	'map': map_query,
	'sort': sort_query,
	'regex': regex_query
}
# print(type())


def read_file(file_name: Path) -> Iterator[str]:
	with open(file_name) as file:
		for line in file:
			yield line


def build_query(cmd: str, value: str, file_name: Path, data: Union[str, list]) -> list:
	if data == '':
		prepared_data: Iterable[str] = read_file(file_name)
	else:
		prepared_data: Iterable[str] = data

	return list(CMD_TO_FUNCTIONS[cmd](value=value, data=prepared_data))
