import boto3

cloudwatch = boto3.client("cloudwatch")

def get_alarms():
    response = cloudwatch.describe_alarms()

    alarms = []

    for alarm in response["MetricAlarms"]:
        alarms.append({
            "AlarmName": alarm["AlarmName"],
            "State": alarm["StateValue"]
        })

    return alarms


if __name__ == "__main__":
    for alarm in get_alarms():
        print(alarm)