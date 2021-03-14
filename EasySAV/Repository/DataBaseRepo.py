import sqlite3
from EasySAV.Domain.Intervention import Intervention

class DataBaseRepo:
    def __init__(self, dbStore):
        self.conn = sqlite3.connect(dbStore)
        self.cursor = self.conn.cursor()

    def execute(self, sql) -> None:
        self.cursor.execute(sql)

    def list(self):
        res = []
        #self.execute(f"CREATE TABLE if NOT EXISTS intervention(" \
        #             f" code INTEGER PRIMARY KEY autoincrement UNIQUE ," \
        #             f" ref_client TEXT," \
        #             f" piece TEXT," \
        #             f" probleme TEXT)")
        #self.execute("INSERT INTO intervention(ref_client, piece, probleme) VALUES('CFGRRF', 'lave linge', 'fuite')")
        #self.execute("INSERT INTO intervention(ref_client, piece, probleme) VALUES('REFTY', 'TV', 'allumage')")
        #self.execute("INSERT INTO intervention(ref_client, piece, probleme) VALUES('YGTGDR', 'lave vaisselle', 'fuite')")
        #self.conn.commit()
        self.execute("select * from intervention")
        for row in self.cursor:
            res.append(Intervention(row[0], row[1], row[2], row[3]).to_dict())
        return res
