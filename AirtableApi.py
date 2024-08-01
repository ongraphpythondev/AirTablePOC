import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class AirTableRequests():

    def __init__(self) -> None:
        headers = {
            'Authorization': f'Bearer {os.getenv('token')}',
            'Content-Type': 'application/json'
        }
        baseId = os.getenv('baseId')


    def createTable(self,description:str,schema:list,tableName:str) -> dict:
        url = f'https://api.airtable.com/v0/meta/bases/{self.baseId}/tables'
        data = {
            "description": description,
            "fields": schema,
            "name": tableName
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(data))
        return {"status":response.status_code,"response":response.json()}
    
    def searchRecords(self,query:dict,tableName:str)-> dict:
        url = f'https://api.airtable.com/v0/{self.baseId}/{tableName}'
        
        response = requests.get(url, headers=self.headers, params=query)
        if response.status_code == 200:
            records = response.json().get('records', [])
            return {"status":response.status_code,"response":records}
        else:
            return {"status":response.status_code,"response":response.json()}
    
    def insert_data(self,rawData:dict,tableName:str):
        url = f'https://api.airtable.com/v0/{self.baseId}/{tableName}'
        data = {
            "fields": rawData
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(data))
        return {"status":response.status_code,"response":response.json()}

    def delete_record(self,tableName,recordId):
        url = f'https://api.airtable.com/v0/{self.baseId}/{tableName}/{recordId}'
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 200:
            return {"status":response.status_code,"response":f'Record with ID {recordId} deleted successfully.'}    
        else:
            return {"status":response.status_code,"response":response.json()}
        
    def fetchAllRecords(self,tableName):
        url = f'https://api.airtable.com/v0/{self.baseId}/{tableName}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            records = response.json().get('records', [])
            return {"status":response.status_code,"response":records}
        else:
            return {"status":response.status_code,"response":response.json()}