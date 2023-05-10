from flask import Blueprint, render_template

doc_bp = Blueprint('documentation', __name__)


@doc_bp.route('/galerasDoc', methods=['GET'])
def docGaleras():
    return render_template('galerasDoc.html')


@doc_bp.route('/lotesDoc', methods=['GET'])
def docLotes():
    return render_template('lotesDoc.html')


@doc_bp.route('/registerDoc', methods=['GET'])
def docRegister():
    return render_template('registerDoc.html')
