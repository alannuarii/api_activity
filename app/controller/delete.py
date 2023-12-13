import os
from db import connection


class Detele:
    def delete_data(self, kode):
        self.delete_activity(kode)
        self.delete_foto(kode)
        self.delete_file(kode)

    def delete_activity(self, kode):
        query = f"DELETE FROM activity WHERE kode = %s"
        value = [kode]
        connection(query, 'delete', value)

    def delete_foto(self, kode):
        query = f"DELETE FROM photo WHERE kode = %s"
        value = [kode]
        connection(query, 'delete', value)

    def delete_file(self, kode):
        path_direktori = os.path.join(os.getcwd(), 'app', 'static', 'img')
        for file_name in os.listdir(path_direktori):
            kode_file = file_name.split('-')[-2]
            if kode_file == kode:
                path_file = os.path.join(path_direktori, file_name)
                try:
                    os.remove(path_file)
                    print(f"File {file_name} telah dihapus")
                except FileNotFoundError:
                    print(f"File {file_name} tidak ditemukan")
                except Exception as e:
                    print(f"Terjadi kesalahan: {e}")