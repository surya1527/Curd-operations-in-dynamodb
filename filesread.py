from pprint import pprint
import boto3
from botocore.exceptions import ClientError

def get_file(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='ap-south-1')
    TableName = 'files'
    table = dynamodb.Table(TableName)

    try:
        response = table.scan()
        
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


    


