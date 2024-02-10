import boto3

# Specify the AWS region
region = 'us-east-1'  # Replace with your actual region

# Specify AWS access key ID and secret access key
aws_access_key_id = 'AKIAZBO674JSJL55LUP4'
aws_secret_access_key = '25oXruTtgDFr6+SPhigsf8bIhm10A6wwQ2h861UW'

# Create RDS client with provided credentials
rds = boto3.client('rds', region_name=region,
                   aws_access_key_id=aws_access_key_id,
                   aws_secret_access_key=aws_secret_access_key)

# Describe RDS instance to get endpoint
response = rds.describe_db_instances(DBInstanceIdentifier='contactlistproject')

# Extract endpoint from response
endpoint = response['DBInstances'][0]['Endpoint']['Address']

# Write endpoint to file
with open('/home/ec2-user/dbserver.endpoint', 'w') as f:
    f.write(endpoint)
