import sqlite3
import traceback

class SqlTool(object):
    def __init__(self, db_name):
        self.__conn = sqlite3.connect(db_name)
        self.__cursor = self.__conn.cursor()
    
    def execute(self, statement):
        try:
            self.__cursor.execute(
                statement
            )
            self.__conn.commit()
            return 0, ''
        except Exception as e:
            self.__conn.rollback()
            return -1, str(e)
    
    def select(self, tablename, keylist="*", condition=""):
        try:
            if len(condition) > 0:
                condition = "where " + condition
            if keylist != "*":
                keys = ",".join(keylist)
            else:
                keys = "*"
            statement = "select {keys} from {tablename} {condition}".format(
                keys=keys, tablename=tablename, condition=condition
            )
            self.__cursor.execute(statement)
            if keys == "*":
                return 0, self.__cursor.fetchall()
            else:
                result = []
                for info in self.__cursor.fetchall():
                    resultdict = {}
                    for idx, key in enumerate(keylist):
                        resultdict[key] = info[idx]
                    result.append(resultdict)
                return 0, result
        except Exception as e:
            print(traceback.format_exc())
            return -1, str(e)
    
    def insert(self, table, valueDict):
        try:
            keys = ",".join('`{}`'.format(key) for key in valueDict.keys())
            values = ",".join("'{}'".format(valueDict[key]) for key in valueDict.keys())
            statement = "insert into {table} ({keys}) values ({values})".format(
                table=table,
                keys=keys,
                values=values
            )
            self.__cursor.execute(statement)
            self.__conn.commit()
            return self.__cursor.lastrowid, ""
        except Exception as e:
            print(traceback.format_exc())
            self.__conn.rollback()
            return -1, str(e)   
    
    def getCount(self, tablename):
        code, result = self.select(tablename=tablename,keylist=['count(*)'])
        if code == 0:
            return result[0]['count(*)']
        else:
            return -1

    def __del__(self):
        self.__cursor.close()
        self.__conn.close()