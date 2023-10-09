from cassandra.cluster import Cluster

class DataAccess :

    @classmethod
    def connexion(cls) :
        cls.cluster = Cluster(['cas1'],port=9042)
        cls.session = cls.cluster.connect('resto', wait_for_all_pools=True)

    @classmethod
    def deconnexion(cls) :
        cls.cluster.shutdown()

    @classmethod
    def inforesto(cls, id):
        rows = cls.session.execute('SELECT * FROM restaurant WHERE id = %s', [id])
        return list(rows)

    @classmethod
    def noms_resto_par_type_de_cuisine(cls, cuisine_type):
        rows = cls.session.execute('SELECT name FROM restaurant WHERE cuisinetype = %s', [cuisine_type])
        return list(rows)

    @classmethod
    def nombre_inspection_pour_ce_resto(cls, id):
        rows = cls.session.execute('SELECT COUNT(*) FROM inspection WHERE idrestaurant = %s', [id])
        return rows[0]

    @classmethod
    def top_10(cls, grade):
        rows = cls.session.execute('SELECT idrestaurant FROM inspection WHERE grade = %s', [grade])
        idrestaurants = list(set(row.idrestaurant for row in rows))[:10]
        names = []
        for idrestaurant in idrestaurants:
            rows = cls.session.execute(f"SELECT name FROM restaurant WHERE id = {idrestaurant}")
            for row in rows:
                names.append(row.name)
        return names


