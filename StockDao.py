

import mysql.connector

class StockDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'datarep'
        )
        # print("connection made")
        
    def create(self,stock_item):
        cursor = self.db.cursor()
        sql = "INSERT INTO STOCK (Item_number, Item_name, supplier, Price) values (%s,%s,%s,%s)"
        values = [
            stock_item['Item_number'],
            stock_item['Item_name'],
            stock_item['supplier'],
            stock_item['Price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
    
    def getAll(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM STOCK"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
            
        return returnArray
        
    def findById(self, Item_number):
        cursor = self.db.cursor()
        sql = "SELECT * FROM STOCK WHERE Item_number = %s"
        values = [Item_number]
        cursor.execute(sql,values)
        result = cursor.fetchone()
       
        return self.convertToDict(result)
        
    def update(self,stock_item):
        cursor = self.db.cursor()
        sql = "UPDATE STOCK SET Item_number = %s, supplier = %s, Price = %s WHERE Item_number  = %s"
        values = [
            stock['Item_number'],
            stock['Item_name'],
            stock['supplier'],
            stock['Price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return stock
        
    def delete(self,Item_number):
        cursor = self.db.cursor()
        sql = "DELETE FROM STOCK WHERE Item_number = %s"
        values = [Item_number]
        cursor.execute(sql,values)

        return {}
    
    def convertToDict(self,result):
        colnames = ['Item_number','Item_name','supplier','Price']
        stock_item = {}
            
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                stock_item[colName] = value
        return stock_item
stockDao = StockDao()