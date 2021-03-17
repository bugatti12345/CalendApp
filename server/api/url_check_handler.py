from flask import jsonify, Blueprint
from model.model import Users

url_check_handler = Blueprint('url_check_handler', __name__)


@url_check_handler.route('/user/<url>/event-type', methods=['GET'])
def url_is_unique(url):
    if Users.query.filter_by(url=url).first():
        return jsonify({'success': 'true', 'unique': 'false'}), 200
    return jsonify({'success': 'true', 'unique': 'true'}), 200
