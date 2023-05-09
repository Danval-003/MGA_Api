from flask import Blueprint, render_template

doc_bp = Blueprint('documentation', __name__)


@doc_bp.route('/galeriasDoc', methods=['GET'])
def docGalerias():
    return render_template('galeriasDoc.html')
