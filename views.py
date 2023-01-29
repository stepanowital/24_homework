from flask import Blueprint, request, jsonify, abort
from marshmallow import ValidationError
from builder import build_query
from models import BatchRequestSchema
from pathlib import Path

main_bp = Blueprint('main', __name__)


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.joinpath('data')


# нужно взять код из предыдущего ДЗ
# добавить команду regex
# добавить типизацию в проект, чтобы проходила утилиту mypy app.py


@main_bp.route("/perform_query", methods=['POST'])
def perform_query():
	# TODO Принять запрос от пользователя
	data = request.json

	# TODO Обработать запрос, валидировать значения
	try:
		validated_data = BatchRequestSchema().load(data)
	except ValidationError as error:
		return jsonify(error.messages), 400
	# TODO Выполнить запрос

	result = ''
	file_path: Path = DATA_DIR

	for query in validated_data['queries']:
		if query.get('file_name'):
			file_path = DATA_DIR.joinpath(query['file_name'])
		if not file_path.is_file():
			abort(400, 'File not exists')
		result = build_query(
			cmd=query['cmd'],
			value=query['value'],
			file_name=file_path,
			data=result,
		)

	return jsonify(result)

