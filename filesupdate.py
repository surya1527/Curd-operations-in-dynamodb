from decimal import Decimal
from pprint import pprint
import boto3


def update_file(user_id, Trained, age, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='ap-south-1')

    table = dynamodb.Table('files')

    response = table.update_item(
        Key={
            'user_id': user_id
        },
        UpdateExpression="set Trained=:r, age=:a",
        ExpressionAttributeValues={
            ':r': Trained,
            ':a': age
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    update_response = update_file(6,"Self_trained", 1500)
    print("Update file succeeded:")
    pprint(update_response, sort_dicts=False)
