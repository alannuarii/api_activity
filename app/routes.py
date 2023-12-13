from app import app
from flask import jsonify, request
from app.controller.input import Input
from app.controller.select import Select
from app.controller.check import Check
from app.controller.delete import Detele


@app.route('/input', methods=['POST'])
def insert_data():
    try:
        obj_input = Input()
        obj_input.upload_data()

        response_message = {"message": "Data berhasil dikirim"}
        return jsonify(response_message), 200

    except Exception as e:
        error_response = {"message": "Data gagal terkirim", "error": str(e)}
        return jsonify(error_response), 500


@app.route('/input-photos/<kode>', methods=['POST'])
def insert_photos(kode):
        try:
            obj_input = Input()
            obj_input.upload_foto(kode)

            response_message = {"message": "Data berhasil dikirim"}
            return jsonify(response_message), 200

        except Exception as e:
            error_response = {"message": "Data gagal terkirim", "error": str(e)}
            return jsonify(error_response), 500


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
    

@app.route('/get-activity-param/<kode>')
def get_activity_param(kode):
    try:
        obj_select = Select()
        result = obj_select.get_activity_param(kode)

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500
    

@app.route('/check-data')
def check_data():
    try:
        obj_check = Check()
        obj_check.check_delete_data()
        obj_check.check_delete_file()

        response = {"message": "Sukses"}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500
    

@app.route('/delete-data/<kode>', methods=['DELETE'])
def delete_data(kode):
    try:
        obj_del = Detele()
        obj_del.delete_data(kode)
        response = {"message": "Data berhasil dihapus"}
        return jsonify(response), 200 

    except Exception as e:
        error_response = {"message": "Data gagal dihapus", "error": str(e)}
        return jsonify(error_response), 500
