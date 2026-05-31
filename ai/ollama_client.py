from ollama import chat

def analyze_aws_report(report):

    prompt = f"""
You are an AWS Cloud Monitoring Expert.

Analyze this AWS report and provide:

1. Infrastructure Summary
2. Any Issues Found
3. Cost Optimization Suggestions
4. Security Recommendations

AWS Report:

{report}
"""

    response = chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]