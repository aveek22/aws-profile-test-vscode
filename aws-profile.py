import boto3

def main(event,context):
    boto3.setup_default_session(profile_name='aveek2021')

    client = boto3.client('s3')

    response_json = client.list_buckets()
    for bucket in response_json['Buckets']:
        print(f"{bucket['Name']}")



if __name__ == '__main__':
    main('','')