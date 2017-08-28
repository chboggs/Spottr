from flask import jsonify
from app import app

@app.route('/health')
def health():
	if app:
		return jsonify({ 'health': 'good' })
	else:
		return jsonify({ 'health': 'down'})