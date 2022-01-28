from decimal import Decimal
from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def delete_unwanted_file(user_id, age, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='ap-south-1')

    table = dynamodb.Table('files')

    try:
        response = table.delete_item(
            Key={
                'user_id': user_id
            },
            ConditionExpression="age >= :val",
            ExpressionAttributeValues={
                ":val": age
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        return response


if __name__ == '__main__':
    print("Attempting a conditional delete...")
    delete_response = delete_unwanted_file(6,1000)
    if delete_response:
        print("Delete movie succeeded:")
        pprint(delete_response, sort_dicts=False)
