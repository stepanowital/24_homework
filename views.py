from flask import Blueprint, request, jsonify, abort, Response
from marshmallow import ValidationError
from builder import build_query
from models import BatchRequestSchema
from pathlib import Path

main_bp = Blueprint('main', __name__)


BASE_DIR: Path = Path(__file__).resolve().parent
DATA_DIR: Path = BASE_DIR.joinpath('data')

# нужно взять код из предыдущего ДЗ
# добавить команду regex
# добавить типизацию в проект, чтобы проходила утилиту mypy app.py


@main_bp.route("/perform_query", methods=['POST'])
def perform_query() -> Response:
	# TODO Принять запрос от пользователя
	data: dict = request.json

	# TODO Обработать запрос, валидировать значения
	try:
		validated_data: dict = BatchRequestSchema().load(data)
	except ValidationError as error:
		return jsonify(error.messages)
	# TODO Выполнить запрос

	result: str = ''
	file_path: Path = DATA_DIR

	for query in validated_data['queries']:
		if query.get('file_name'):
			file_path = DATA_DIR.joinpath(query['file_name'])
		if not file_path.is_file():
			abort(400, 'File not exists')
		result: list = build_query(
			cmd=query['cmd'],
			value=query['value'],
			file_name=file_path,
			data=result,
		)

	return jsonify(result)

