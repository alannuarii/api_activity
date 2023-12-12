import os
import glob
from db import connection


class Check:
    def check_delete(self):
        dict_kode = self.get_kode()
        list_kode = [item["kode"] for item in dict_kode]
        for kode in list_kode:
            result = self.check_file(kode)
            return result

    def check_file(self, kode):
        # Tentukan path ke direktori app/static/img
        path_direktori = os.path.join(os.getcwd(), 'app', 'static', 'img')

        # Gunakan modul glob untuk mencari file dengan pola nama tertentu
        pola_file = os.path.join(path_direktori, '*' + kode + '*')
        files = glob.glob(pola_file)

        # Jika ada file yang sesuai dengan pola, kembalikan True
        if files:
            pass
        else:
            self.delete_file(kode)
    
    def delete_file(self, kode):
        query = f"DELETE FROM photo WHERE kode = %s"
        value = [kode]
        connection(query, 'delete', value)

    def get_kode(self):
        query = f"SELECT kode FROM photo GROUP BY kode"
        value = []
        result = connection(query, 'select', value)
        return result
    

