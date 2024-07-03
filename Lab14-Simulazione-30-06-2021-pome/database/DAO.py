from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getLoc():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select DISTINCT  Localization 
            from classification c 
            """
        cursor.execute(query)
        for row in cursor:
            result.append(row["Localization"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def esisteArco(n1, n2):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select count(*) as c
                    from interactions i , classification c , classification c2 
                    where c2.Localization =%s and c.Localization = %s
                    and i.GeneID1 =c2.GeneID and i.GeneID2 = c.GeneID"""
        cursor.execute(query,(n1,n2))
        for row in cursor:
            result.append(row["c"])
        cursor.close()
        conn.close()
        return result
        pass

    @staticmethod
    def getPesi(n1, n2):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select COUNT(DISTINCT i.`Type` ) as c 
                from interactions i , classification c , classification c2 
                where c2.Localization =%s and c.Localization = %s
                and i.GeneID1 =c2.GeneID and i.GeneID2 = c.GeneID"""
        cursor.execute(query, (n1, n2,))
        for row in cursor:
            result.append(row["c"])
        cursor.close()
        conn.close()
        return result
        pass