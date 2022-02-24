from decimal import Decimal
import json
import boto3


def load_files(files, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='ap-south-1')

    table = dynamodb.Table('files')
    for file in files:
        user_id = int(file['user_id'])
        print("Adding file:", user_id)
        table.put_item(Item=file)


if __name__ == '__main__':
    with open("sampledata.json") as json_file:
        file_list = json.load(json_file, parse_float=Decimal)
    load_files(file_list)