from ollama import chat
from tools.ec2_status import get_instances
from tools.s3_status import get_buckets
from tools.cloudwatch_status import get_alarms

print("AWS Monitoring Agent Started")
print("Type 'exit' to quit\n")

while True:

    question = input("Ask AWS Agent: ")

    if question.lower() == "exit":
        break

    if "ec2" in question.lower():

        data = get_instances()

        prompt = f"""
User Question: {question}

AWS EC2 Data:
{data}

Answer based on the actual AWS data.
"""

    elif "s3" in question.lower():

        data = get_buckets()

        prompt = f"""
User Question: {question}

AWS S3 Data:
{data}

Answer based on the actual AWS data.
"""

    elif "alarm" in question.lower() or "cloudwatch" in question.lower():

        data = get_alarms()

        prompt = f"""
User Question: {question}

CloudWatch Alarm Data:
{data}

Answer based on the actual AWS data.
"""

    else:
        prompt = question

    response = chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("\nAgent:")
    print(response["message"]["content"])
    print()