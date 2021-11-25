from StockDao import stockDao

stock1 = {
    'Item_number': 3,
    'Item_name': 'Tyre',
    'supplier': 'Dunlop',
    'Price': 19
    }
    
stock2 = {
    'Item_number': 3,
    'Item_name': 'Tyre',
    'supplier': 'Michelin',
    'Price': 21
    }
   
    
#returnValue = stockDao.create(stock) 
returnValue = stockDao.getAll()   
print(returnValue)
returnValue = stockDao.findById(stock2['Item_number']) 
print("find By Id")  
print(returnValue) 
returnValue = stockDao.update(stock2)   
print(returnValue)
returnValue = stockDao.findById(stock2['Item_number'])   
print(returnValue)
returnValue = stockDao.delete(stock2['Item_number'])   
print(returnValue) 
returnValue = stockDao.getAll()   
print(returnValue) 
    
