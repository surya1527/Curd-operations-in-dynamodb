from importlib.metadata import files
import boto3


class dynamodb:
    def getTableScan(tblname):
        TableName = files
        client = boto3.client('dynamodb', region_name="ap-south-1")
        DB = boto3.resource('dynamodb', region_name="ap-south-1")
        table = DB.Table(TableName)

        response = table.scan()
        data = response['Items']

        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])

        print(response)


#dynamodb.getTableScan('cats')
