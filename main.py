from tools.ec2_status import get_instances
from tools.s3_status import get_buckets
from tools.cloudwatch_status import get_alarms

from ai.ollama_client import analyze_aws_report


instances = get_instances()
buckets = get_buckets()
alarms = get_alarms()

report = f"""
EC2 Instances:
{instances}

S3 Buckets:
{buckets}

CloudWatch Alarms:
{alarms}
"""

print("Generating AI Analysis...\n")

analysis = analyze_aws_report(report)

print(analysis)