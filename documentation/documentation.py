from flask import Blueprint, render_template

doc_bp = Blueprint('documentation', __name__)


@doc_bp.route('/galerasDoc', methods=['GET'])
def docGaleras():
    return render_template('galerasDoc.html')
