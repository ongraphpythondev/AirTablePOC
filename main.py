from AirTablePOC.AirtableApi import AirTableRequests

airObj = AirTableRequests()

def createTable()->dict:
    schema = [
            {
                "description": "Name of the apartment",
                "name": "Name",
                "type": "singleLineText"
            },
            {
                "name": "Address",
                "type": "singleLineText"
            },
            {
                "name": "Visited",
                "options": {
                    "color": "greenBright",
                    "icon": "check"
                },
                "type": "checkbox"
            }
        ]
    description = "Apartment Info Table"
    tableName = "Apartments"
    tableInfo = airObj.createTable(schema=schema,description=description,tableName=tableName)
    return tableInfo

def addRecords(name:str, address:str, visited:bool, tableName:str)->dict:
    rawData = {
        "fields": {
            "Name": name,
            "Address": address,
            "Visited": visited
        }
    }
    recordInfo = airObj.insert_data(rawData=rawData,tableName=tableName)
    return recordInfo

def searchRecordByName(subString:str,tableName:str)->dict:
    query = {
            'filterByFormula': "FIND('"+subString+"', {Name})"
        }
    result = airObj.searchRecords(query=query,tableName=tableName)
    return result

def fetchAllRecords(tableName:str)->dict:
    result = airObj.fetchAllRecords(tableName=tableName)
    return result

    
if __name__ == "__main__":
    createTable()
    addRecords(name="Test",address="Noida,Near Delhi",visited=True,tableName='Apartments')
    searchRecordByName(subString='T',tableName="Apartments")
    fetchAllRecords(tableName="Apartments")

