import boto3


def create_file_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='ap-south-1')

    table = dynamodb.create_table(
        TableName='files',         #Enter your table name
        KeySchema=[
            {
                'AttributeName': 'user_id',             #partition key
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'user_id',
                'AttributeType': 'N'
            }

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    return table






if __name__ == '__main__':
    file_table = create_file_table()
    print("Table status:", file_table.table_status)
