from flask import Blueprint, request, jsonify

from builder import build_query
from models import BatchRequestSchema

main_bp = Blueprint('main', __name__)


FILE_NAME = 'data/apache_logs.txt'

@main_bp.route("/perform_query", methods=['POST'])
def perform_query():
	# TODO Принять запрос от пользователя
	data = request.json

	# TODO Обработать запрос, валидировать значения
	validated_data = BatchRequestSchema().load(data)
	# TODO Выполнить запрос

	result = []
	for query in validated_data['queries']:
		result = build_query(
			cmd=query['cmd'],
			value=query['value'],
			file_name=FILE_NAME,
			data=result,
		)
	# return jsonify(
	# 	build_query(
	# 		cmd=validated_data['cmd'],
	# 		value=validated_data['value'],
	# 		file_name='data/apache_logs.txt'
	# 	)
	# )


	# return app.response_class('', content_type="text/plain")
