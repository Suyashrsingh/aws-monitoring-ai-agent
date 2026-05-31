# AWS Monitoring AI Agent

## Overview

AWS Monitoring AI Agent is an AI-powered cloud monitoring solution built using Python, AWS Services, Boto3, Ollama, and Qwen 2.5.

The agent can:

* Monitor EC2 instances
* Monitor S3 buckets
* Monitor CloudWatch alarms
* Generate AI-powered infrastructure summaries
* Provide AWS best-practice recommendations
* Suggest cost optimization opportunities

---

# Architecture

```text
AWS Account
│
├── EC2
├── S3
├── CloudWatch
│
└── AWS API
      │
      ▼
Python + Boto3
      │
      ▼
AWS Monitoring Agent
      │
      ▼
Ollama + Qwen2.5
      │
      ▼
AI Analysis & Recommendations
```
Vs Code
<img width="1907" height="928" alt="image" src="https://github.com/user-attachments/assets/5594bc06-c3e9-4e0d-ac6a-a692c9391fd4" />

Model Running 
<img width="1907" height="330" alt="Screenshot 2026-05-31 112719" src="https://github.com/user-attachments/assets/cc2ae650-6838-4e47-9c35-b525e2f0346b" />

AWS-AGENT RUNNING ON NEW TAB 
<img width="1903" height="680" alt="Screenshot 2026-05-31 112327" src="https://github.com/user-attachments/assets/ae0f59d9-9ee4-4a5a-a21b-5de1c08a8493" />

<img width="1907" height="1087" alt="Screenshot 2026-05-31 112706" src="https://github.com/user-attachments/assets/3752cdd8-0db2-48fa-8397-708c37bcf19f" />

---

# Features

* EC2 Monitoring
* S3 Monitoring
* CloudWatch Alarm Monitoring
* AI-Based Infrastructure Analysis
* Cost Optimization Suggestions
* Security Recommendations
* Interactive Chat Agent

---

# Prerequisites

Before starting, ensure you have:

* AWS Account
* Windows 10/11
* Python 3.11+
* Git
* AWS CLI
* Ollama
* VS Code

---

# AWS Setup

## Step 1: Create IAM User

Open AWS Console.

Navigate:

```text
IAM
→ Users
→ Create User
```

User Name:

```text
admin-user
```

Permissions:

```text
AdministratorAccess
```

OR

```text
AmazonEC2ReadOnlyAccess
AmazonS3ReadOnlyAccess
CloudWatchReadOnlyAccess
```

---

## Step 2: Create Access Keys

Navigate:

```text
IAM
→ Users
→ admin-user
→ Security Credentials
→ Create Access Key
```

Select:

```text
Command Line Interface (CLI)
```

Save:

```text
Access Key ID
Secret Access Key
```

---

## Step 3: Launch EC2 Instance

Navigate:

```text
EC2
→ Launch Instance
```

Configuration:

```text
Name: monitor-test

AMI:
Ubuntu 24.04

Instance Type:
t3.micro

Storage:
8GB
```

Launch instance.

---

## Step 4: Create S3 Bucket

Navigate:

```text
S3
→ Create Bucket
```

Example:

```text
aws-agent-reports
```

---

## Step 5: Create CloudWatch Alarm

Navigate:

```text
CloudWatch
→ Alarms
→ Create Alarm
```

Metric:

```text
CPUUtilization
```

Threshold:

```text
80%
```

Create alarm.

---

# Local Machine Setup

## Step 1: Install Python

Verify:

```bash
python --version
```

Expected:

```text
Python 3.x
```

---

## Step 2: Install Git

Verify:

```bash
git --version
```

---

## Step 3: Install AWS CLI

Verify:

```bash
aws --version
```

---

## Step 4: Configure AWS CLI

```bash
aws configure
```

Provide:

```text
Access Key ID
Secret Access Key
Region: ap-south-1
Output: json
```

Verify:

```bash
aws sts get-caller-identity
```

---

## Step 5: Install Ollama

Verify:

```bash
ollama --version
```

---

## Step 6: Download AI Model

Recommended:

```bash
ollama pull qwen2.5:7b
```

Verify:

```bash
ollama run qwen2.5:7b
```

---

# Project Setup

## Clone Repository

```bash
git clone https://github.com/Suyashrsingh/aws-monitoring-ai-agent.git
```

Move into project:

```bash
cd aws-monitoring-ai-agent
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Project Structure

```text
aws-agent/
│
├── ai/
│   └── ollama_client.py
│
├── tools/
│   ├── ec2_status.py
│   ├── s3_status.py
│   └── cloudwatch_status.py
│
├── chat_agent.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── AGENTS.md
```

---

# Running the Project

## Start Ollama

Open terminal:

```bash
ollama serve
```

If Ollama is already running, skip this step.

---

## Run Monitoring Report

```bash
python main.py
```

---

## Run AI Chat Agent

```bash
python chat_agent.py
```

---

# Example Questions

## EC2

```text
Show my EC2 instances
```

```text
How many EC2 instances are running?
```

```text
Summarize my EC2 infrastructure
```

---

## S3

```text
List all S3 buckets
```

```text
Analyze my S3 storage
```

---

## CloudWatch

```text
Show CloudWatch alarms
```

```text
Are any alarms in ALARM state?
```

---

## AI Analysis

```text
Analyze my AWS environment
```

```text
Suggest cost optimization opportunities
```

```text
Generate a security report
```

```text
Provide AWS best practices
```

---

# Future Enhancements

* Cost Explorer Integration
* IAM Security Audits
* AWS Config Support
* CloudTrail Analysis
* Daily Email Reports
* Slack Integration
* Multi-Account Monitoring

---

# Technologies Used

* Python
* AWS EC2
* AWS S3
* AWS CloudWatch
* Boto3
* Ollama
* Qwen2.5 7B
* Git
* GitHub

---

# Author

Suyash Singh
AWS Monitoring AI Agent Project
