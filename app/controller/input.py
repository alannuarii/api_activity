import os
from app import app
from db import connection
from flask import request
from app.utils import generate_random_code


class Input:
    def upload_data(self):
        jenis = request.form.get('jenis')
        tanggal = request.form.get('tanggal')
        pekerjaan = request.form.get('pekerjaan')
        perusahaan = request.form.get('perusahaan')
        photos = request.files.getlist('foto')
        kode = generate_random_code()

        self.insert_data(tanggal, jenis, perusahaan, pekerjaan, kode)

        if photos[0].filename != 'undefined':
            for index, photo in enumerate(photos):
                name_photo = self.rename_photo(pekerjaan, tanggal, kode, index)
                self.insert_photo(tanggal, kode, name_photo)
                photo.save(os.path.join(app.config['FOTO'], name_photo))

    def rename_photo(self, pekerjaan, tanggal, random, index):
        rename = f"{pekerjaan.replace(' ','-')}-{tanggal}-{random}-{index + 1}.png"
        return rename

    def insert_data(self, tanggal, jenis, perusahaan, pekerjaan, kode):
        query = f"INSERT INTO activity (tanggal, jenis, perusahaan, pekerjaan, kode) VALUES (%s, %s, %s, %s, %s)"
        value = [tanggal, jenis, perusahaan, pekerjaan, kode]
        connection(query, 'insert', value)

    def insert_photo(self, tanggal, kode, foto):
        query = f"INSERT INTO photo (tanggal, kode, foto) VALUES (%s, %s, %s)"
        value = [tanggal, kode, foto]
        connection(query, 'insert', value)







