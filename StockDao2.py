


import mysql.connector

class StockDao2:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'datarep'
        )
        
        # 2nd table
        
    def create2(self,stock_item):
        cursor = self.db.cursor()
        sql = "INSERT INTO STOCKK (Item_number, Item_name, supplier, Price) values (%s,%s,%s,%s)"
        values = [
            stock_item['Item_number'],
            stock_item['Item_name'],
            stock_item['supplier'],
            stock_item['Price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
    
    def getAll2(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM STOCKK"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict2(result)
            returnArray.append(resultAsDict)
            
        return returnArray
        
    def findById2(self, Item_number):
        cursor = self.db.cursor()
        sql = "SELECT * FROM STOCKK WHERE Item_number = %s"
        values = [Item_number]
        cursor.execute(sql,values)
        result = cursor.fetchone()
       
        return self.convertToDict2(result)
        
    def update2(self,stock_item):
        cursor = self.db.cursor()
        sql = "UPDATE STOCKK SET Item_number = %s, supplier = %s, Price = %s WHERE Item_number  = %s"
        values = [
            stockk['Item_number'],
            stockk['Item_name'],
            stockk['supplier'],
            stockk['Price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return stockk
        
    def delete2(self,Item_number):
        cursor = self.db.cursor()
        sql = "DELETE FROM STOCKK WHERE Item_number = %s"
        values = [Item_number]
        cursor.execute(sql,values)

        return {}
    
    def convertToDict2(self,result):
        colnames = ['Item_number','Item_name','supplier','Price']
        stock_item = {}
            
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                stock_item[colName] = value
        return stock_item
        
stockDao2 = StockDao2()
