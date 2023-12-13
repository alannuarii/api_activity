import os
import glob
from db import connection


class Check:
    def check_delete_data(self):
        dict_kode = self.get_kode()
        list_kode = [item["kode"] for item in dict_kode]
        for kode in list_kode:
            path_direktori = os.path.join(os.getcwd(), 'app', 'static', 'img')
            pola_file = os.path.join(path_direktori, '*' + kode + '*')
            files = glob.glob(pola_file)
            if files:
                pass
            else:
                self.delete_data(kode)

    def check_delete_file(self):
        dict_kode = self.get_kode()
        list_kode = [item["kode"] for item in dict_kode]
        path_direktori = os.path.join(os.getcwd(), 'app', 'static', 'img')
        for file_name in os.listdir(path_direktori):
            kode_file = file_name.split('-')[-2]
            if kode_file not in list_kode:
                path_file = os.path.join(path_direktori, file_name)
                try:
                    os.remove(path_file)
                    print(f"File {file_name} telah dihapus")
                except FileNotFoundError:
                    print(f"File {file_name} tidak ditemukan")
                except Exception as e:
                    print(f"Terjadi kesalahan: {e}")
    
    def delete_data(self, kode):
        query = f"DELETE FROM photo WHERE kode = %s"
        value = [kode]
        connection(query, 'delete', value)

    def get_kode(self):
        query = f"SELECT kode FROM photo GROUP BY kode"
        value = []
        result = connection(query, 'select', value)
        return result
    

