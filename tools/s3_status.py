import boto3

s3 = boto3.client("s3")

def get_buckets():
    response = s3.list_buckets()

    return [bucket["Name"] for bucket in response["Buckets"]]


if __name__ == "__main__":
    print(get_buckets())