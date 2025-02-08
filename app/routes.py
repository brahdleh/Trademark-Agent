from flask import Blueprint, request, jsonify
from .trademark import check_infringements_function

check_infringements = Blueprint('check_infringements', __name__)

@check_infringements.route('/check_infringements', methods=['POST'])
def inspector():
    data = request.get_json()
    name = data.get('name', [])
    summary = data.get('summary', [])
    
    report = check_infringements_function()
    
    return jsonify(report)
