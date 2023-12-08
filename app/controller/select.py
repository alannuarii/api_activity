from db import connection

class Select:
    def get_all_data(self):
        query = f"""
        SELECT
            a.tanggal,
            a.jenis,
            a.perusahaan,
            a.pekerjaan,
            a.kode,
            p.foto
        FROM
            activity a
        JOIN
            photo p ON a.kode = p.kode;
        """
        value = []
        result = connection(query, 'select', value)
        return result
    
    def get_all_activity(self):
        query = f"SELECT tanggal, pekerjaan, kode FROM activity"
        value = []
        result = connection(query, 'select', value)
        return result
    

    def get_activity_param(self, kode):
        query = f"""
        SELECT
            a.tanggal,
            a.jenis,
            a.perusahaan,
            a.pekerjaan,
            a.kode,
            p.foto
        FROM
            activity a
        JOIN
            photo p ON a.kode = p.kode
        WHERE
            a.kode = %s
        """
        value = [kode]
        result = connection(query, 'select', value)
        return result
        