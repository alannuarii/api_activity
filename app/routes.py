from app import app
from flask import jsonify, request
from app.controller.input import Input
from app.controller.select import Select


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


@app.route('/get-all-data')
def get_all_data():
    try:
        obj_select = Select()
        result = obj_select.get_all_data()

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500
    

@app.route('/get-all-activity')
def get_all_activity():
    try:
        obj_select = Select()
        result = obj_select.get_all_activity()

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500