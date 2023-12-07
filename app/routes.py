from app import app
from flask import jsonify, request
from app.controller.input import Input


@app.route('/input', methods=['GET','POST'])
def insert_data():
    if request.method == 'POST':
        try:
            obj_input = Input()
            obj_input.upload_data()

        except Exception as e:
            error_response = {"message": "Data gagal terkirim", "error": str(e)}
            return jsonify(error_response), 500

    response = {"message": "Data berhasil dikirim"}
    return jsonify(response), 200