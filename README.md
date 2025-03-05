# 🚀 AWS EC2 Auto Shutdown

## Overview
This project provides an **AWS Lambda function** that **automatically stops all running EC2 instances** after business hours. It helps optimize cloud costs and enforce security policies by ensuring that no instances are left running unnecessarily.

## Features
✅ Automatically stops all running EC2 instances <br>
✅ Uses AWS Lambda and EventBridge for scheduling <br>
✅ Cost-effective and secure cloud resource management <br>
✅ Deployed using AWS CloudFormation <br>

## Deployment
Follow these steps to deploy the stack using AWS CloudFormation:

### **1. Clone the Repository**
```bash
 git clone https://github.com/Judewakim/LUIT-Python3.git
 cd LUIT-Python3
```

### **2. Deploy the CloudFormation Stack**
Run the following AWS CLI command to create the Lambda function and scheduled rule:
```bash
aws cloudformation create-stack \
  --stack-name StopInstancesLambda \
  --template-body file://stop-instances-lambda.yaml \
  --capabilities CAPABILITY_IAM
```

### **3. Verify Deployment**
- Go to **AWS Console → CloudFormation** and check the stack status.
- Navigate to **AWS Lambda** to see the deployed function.
- Check **Amazon EventBridge** (CloudWatch Events) for the scheduled trigger.

## Usage
- The Lambda function is triggered **daily** by **EventBridge** (customizable in the YAML file).
- It scans for **running EC2 instances** and stops them automatically.
- Logs are available in **Amazon CloudWatch Logs** for monitoring.

## Manual Testing
You can manually invoke the function to test it:
```bash
aws lambda invoke \
  --function-name StopInstancesFunction \
  --log-type Tail \
  output.log
```
Check `output.log` for results.

## License
This project is open-source under the **MIT License**.

---
📌 **Maintained by [Judewakim](https://github.com/Judewakim)**  | 🤖 **Powered by AWS Lambda & Python**

